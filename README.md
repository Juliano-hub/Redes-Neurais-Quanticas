# 🌌 Quantum Neural Networks - VQC & QSVM Experiments

Este repositório reúne experimentos com modelos de **aprendizado de máquina quântica** aplicados a conjuntos de dados clássicos e fuzzy. Os algoritmos testados foram **QSVM** e **VQC**, utilizando diferentes combinações de *feature maps* (Pauli, ZZ) e *ansatz* (EfficientSU2, RealAmplitudes).

---

## 📁 Estrutura do Projeto

```
.
├── .venv/                     # Ambiente virtual
├── codes/                    # Scripts de código
│   ├── FuzzyDataSet/         # Experimentos com dados fuzzy
│   │   └── teste-qsvm-fuzzy.py      
│
│   ├── irisDataSet/          
│   │   ├── QSVM/             
│   │   │   └── teste-qsvm-iris.py   
│   │   │
│   │   └── VQC/              
│   │       ├── EfficientSU2/
│   │       │   ├── pauliFeature.py       
│   │       │   └── zzFeauremap.py        
│   │       │
│   │       └── realAmplitude/
│   │           ├── pauliFeature.py       
│   │           └── zzFeaturemap.py       
│
├── datasets/                 
├── readme                    # (Este arquivo)
└── requirements.txt          
```

---

## 🔍 Descrição dos Experimentos

### ✅ QSVM (Quantum Support Vector Machine)

- `teste-qsvm-iris.py`  
  Modelo QSVM com `FidelityQuantumKernel` usando `ZZFeatureMap` para classificar duas classes do dataset Iris.

- `teste-qsvm-fuzzy.py`  
  QSVM aplicado a um conjunto de dados fuzzy. Ideal para avaliar comportamento em ambientes incertos.

---

### 🧪 VQC (Variational Quantum Classifier)

Treinamento via `SPSA`, testando 2 tipos de *feature map* e *ansatz*:

#### 🔹 EfficientSU2

- `pauliFeature.py`: `EfficientSU2` + `PauliFeatureMap`
- `zzFeauremap.py`: `EfficientSU2` + `ZZFeatureMap`

#### 🔹 RealAmplitudes

- `pauliFeature.py`: `RealAmplitudes` + `PauliFeatureMap`
- `zzFeaturemap.py`: `RealAmplitudes` + `ZZFeatureMap`

---

## 📊 Comparativo de Resultados (Iris dataset)

| Ansatz            | Feature Map     | Acurácia | Tempo (s) |
|------------------|------------------|----------|-----------|
| EfficientSU2     | ZZFeatureMap     | 0.90     | 254.47    |
| EfficientSU2     | PauliFeatureMap  | 0.80     | 220.04    |
| RealAmplitudes   | ZZFeatureMap     | 0.80     | 264.99    |
| RealAmplitudes   | PauliFeatureMap  | 0.75     | 226.56    |

✅ **Conclusão**: O `ZZFeatureMap` produziu melhores resultados em geral, com destaque para a combinação com `EfficientSU2`.

---

## 🤔 Entendendo melhor

### O que são os *Feature Maps*?

- **PauliFeatureMap**: codifica cada feature de forma independente. Não possui emaranhamento.
- **ZZFeatureMap**: aplica operações de emaranhamento entre os qubits já na fase de entrada. Isso permite capturar relações entre as variáveis.

### E os *Ansatz*?

- **EfficientSU2**: ansatz mais expressivo, incluindo entanglement (`cx`) e rotações com diferentes eixos (X, Y).
- **RealAmplitudes**: ansatz mais simples e rápido, baseado em rotações Rx + entanglement linear.

---

## ⚙️ Requisitos

Instale as dependências com:

```bash
pip install -r requirements.txt
```

Bibliotecas principais:
- `qiskit`
- `qiskit-machine-learning`
- `scikit-learn`

---

## 👩‍💻 Autora

Desenvolvido por **Cecilia Botelho**  
Pesquisadora em Computação Quântica aplicada à Inteligência Artificial.  
Universidade Federal de Pelotas (UFPel)

---
