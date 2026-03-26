import time
from qiskit_machine_learning.algorithms import VQC
from qiskit.circuit.library import ZZFeatureMap, RealAmplitudes
from qiskit_algorithms.optimizers import SPSA
from qiskit.circuit.library import EfficientSU2
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

import pandas as pd
import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from DatasetCases import getExecutionCase, LoadCSV, SMOTESampling
import membership.membershipfunction


# CONFIGURAÇÕES
max_iter = 2
show_loss = True
reps = 3
seed = 42
testSize = 0.2
ExecutionCase = 0

# DADOS
FileName, CSVFile, ColumnsX, ColumnsY, mf, conj = getExecutionCase(int(ExecutionCase))
X, Y, lastLabel, header = LoadCSV(CSVFile, ColumnsX, ColumnsY)
X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=seed, test_size=testSize)

sc_X = MinMaxScaler() # método de normalização
X_trainscaled=sc_X.fit_transform(X_train)
X_test = X_test.astype(float).to_numpy()
X_test_scaled = sc_X.transform(X_test)

XSMOTE, YSMOTE = SMOTESampling(X_trainscaled, y_train, seed, header.copy(), lastLabel)

mfc = membership.membershipfunction.MemFuncs(mf)

# Fuzzificação do conjunto de treino (XSMOTE)
X_train_fuzzified = [mfc.evaluateMF(row) for row in XSMOTE]

# Fuzzificação do conjunto de teste (X_test_scaled)
X_test_fuzzified = [mfc.evaluateMF(row) for row in X_test_scaled]

# CIRCUITOS
print("Running...")
YSMOTE = YSMOTE.to_numpy()
y_test = y_test.to_numpy()
X_train_fuz_array = np.array(X_train_fuzzified)

# Achata para 2D (Amostras x Graus de Pertinência)
X_train_vqc = X_train_fuz_array.reshape(len(X_train_fuz_array), -1)

feature_map = ZZFeatureMap(feature_dimension=X_train_vqc.shape[1], reps=reps)
ansatz = EfficientSU2(num_qubits=X_train_vqc.shape[1], reps=reps)

# CALLBACK
def callback(eval_count, parameters, loss, stepsize, accepted):
    if show_loss:
        print(f"Iteração {eval_count} - Loss: {loss:.4f}")

# OTIMIZADOR
optimizer = SPSA(maxiter=max_iter, callback=callback)

# CRONÔMETRO
inicio = time.time()

# VQC atualizado (sem input_gradients)
vqc = VQC(
    feature_map=feature_map,
    ansatz=ansatz,
    optimizer=optimizer
)

# TREINAMENTO
vqc.fit(X_train_vqc, YSMOTE)

# AVALIAÇÃO

X_test_fuz_array = np.array(X_test_fuzzified)
X_test_vqc = X_test_fuz_array.reshape(len(X_test_fuz_array), -1)

y_pred = vqc.predict(X_test_vqc)
acc = accuracy_score(y_test, y_pred)
fim = time.time()
tempo_total = fim - inicio

print(f"\n✅ Acurácia final do VQC efficient: {acc:.2f}")
print(f"⏱️ Tempo total de execução: {tempo_total:.2f} segundos")

