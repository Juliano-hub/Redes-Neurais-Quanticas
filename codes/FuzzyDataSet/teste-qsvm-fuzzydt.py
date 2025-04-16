import time
from qiskit_machine_learning.algorithms import QSVC
from qiskit_machine_learning.kernels import FidelityStatevectorKernel
from qiskit.circuit.library import ZZFeatureMap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    inicio = time.time()  

    file_path = 'simulation_3cops_with_direct_labels.xlsx'
    df = pd.read_excel(file_path)

    X = df[['Police Officer 1', 'Police Officer 2', 'Police Officer 3']].values
    y = LabelEncoder().fit_transform(df['Rotulo'].values)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Feature map e kernel
    num_qubits = X_train.shape[1]
    feature_map = ZZFeatureMap(feature_dimension=num_qubits, reps=1)
    quantum_kernel = FidelityStatevectorKernel(feature_map=feature_map)

    # Modelo QSVC
    qsvc = QSVC(quantum_kernel=quantum_kernel)

    print("Treinando modelo QSVC com kernel quântico...")
    qsvc.fit(X_train, y_train)
    print("Treinamento finalizado!")

    # Previsões e métricas
    y_pred = qsvc.predict(X_test)

    print("\nResultados gerais:")
    print(f"Acurácia:  {accuracy_score(y_test, y_pred):.2f}")
    print(f"Precisão:  {precision_score(y_test, y_pred, average='weighted', zero_division=0):.2f}")
    print(f"Recall:    {recall_score(y_test, y_pred, average='weighted', zero_division=0):.2f}")
    print(f"F1-Score:  {f1_score(y_test, y_pred, average='weighted', zero_division=0):.2f}")

    # Relatório por classe
    print("\nRelatório por classe:")
    print(classification_report(y_test, y_pred, zero_division=0))

    # Matriz de confusão
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, cmap='Blues', fmt='g')
    plt.title('Matriz de Confusão - QSVC')
    plt.xlabel('Classe prevista')
    plt.ylabel('Classe real')
    plt.tight_layout()
    plt.show()

    # Tempo total
    fim = time.time()
    tempo_total = fim - inicio
    print(f"\n⏱️ Tempo total de execução: {tempo_total:.2f} segundos")


if __name__ == "__main__":
    main()
