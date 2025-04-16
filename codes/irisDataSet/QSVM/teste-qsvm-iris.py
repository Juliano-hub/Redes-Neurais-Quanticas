import time
from qiskit_machine_learning.algorithms import QSVC
from qiskit_machine_learning.kernels import FidelityStatevectorKernel
from qiskit.circuit.library import ZFeatureMap, ZZFeatureMap, PauliFeatureMap
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd

def avaliar_kernel(nome, feature_map, X_train, X_test, y_train, y_test):
    print(f"\n🔷 Testando feature map: {nome}")
    inicio = time.time()

    kernel = FidelityStatevectorKernel(feature_map=feature_map)
    modelo = QSVC(quantum_kernel=kernel)

    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)

    print(f"Acurácia:  {accuracy_score(y_test, y_pred):.2f}")
    print(f"Precisão:  {precision_score(y_test, y_pred, average='weighted', zero_division=0):.2f}")
    print(f"Recall:    {recall_score(y_test, y_pred, average='weighted', zero_division=0):.2f}")
    print(f"F1-Score:  {f1_score(y_test, y_pred, average='weighted', zero_division=0):.2f}")
    print(f"⏱️ Tempo de execução: {time.time() - inicio:.2f} segundos")

def main():
    # Carrega o dataset Iris com 3 features
    data = load_iris()
    X = data.data[:, :3]  # usar 3 qubits
    y = data.target

    # Divide e normaliza
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    num_qubits = X_train.shape[1]

    # Define os 3 feature maps
    feature_maps = {
        "ZFeatureMap": ZFeatureMap(feature_dimension=num_qubits, reps=1),
        "ZZFeatureMap": ZZFeatureMap(feature_dimension=num_qubits, reps=1),
        "PauliFeatureMap": PauliFeatureMap(feature_dimension=num_qubits, reps=1, paulis=['X', 'Y', 'Z']),
    }

    for nome, fmap in feature_maps.items():
        avaliar_kernel(nome, fmap, X_train, X_test, y_train, y_test)

if __name__ == "__main__":
    main()
