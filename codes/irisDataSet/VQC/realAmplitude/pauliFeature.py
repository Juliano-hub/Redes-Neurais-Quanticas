import time
from qiskit_machine_learning.algorithms import VQC
from qiskit.circuit.library import pauli_feature_map, RealAmplitudes
from qiskit_algorithms.optimizers import SPSA
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

# CONFIGURAÇÕES
max_iter = 500
show_loss = True
reps = 3
seed = 42

# DADOS (Iris binário)
iris = load_iris()
X = iris.data[iris.target != 2][:, :4] # usa 4 qubits/features
y = iris.target[iris.target != 2]
X = MinMaxScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=seed)

# CIRCUITOS
feature_map = pauli_feature_map(feature_dimension=X.shape[1], reps=reps)
ansatz = RealAmplitudes(num_qubits=X.shape[1], reps=reps)

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
vqc.fit(X_train, y_train)

# AVALIAÇÃO
y_pred = vqc.predict(X_test)
acc = accuracy_score(y_test, y_pred)
fim = time.time()
tempo_total = fim - inicio

print(f"\n✅ Acurácia final do pauliFeature: {acc:.2f}")
print(f"⏱️ Tempo total de execução: {tempo_total:.2f} segundos")
