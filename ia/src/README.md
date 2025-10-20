# IA/Machine Learning

## 📝 Descrição

Módulo responsável pelos modelos de Machine Learning, análise exploratória de dados e notebooks de pesquisa.

## 🚀 Funcionalidades

- Análise exploratória de dados (EDA)
- Pré-processamento e feature engineering
- Treinamento de modelos de ML
- Avaliação e validação de modelos
- Otimização de hiperparâmetros
- Notebooks de pesquisa e experimentação

## 🛠️ Tecnologias Sugeridas

### Core ML
- **Scikit-learn** - Algoritmos de ML tradicionais
- **XGBoost/LightGBM** - Gradient boosting
- **TensorFlow/PyTorch** - Deep learning
- **Statsmodels** - Análises estatísticas

### Processamento de Dados
- **Pandas** - Manipulação de dados
- **NumPy** - Computação numérica
- **Polars** - Processamento rápido de dados

### Visualização
- **Matplotlib/Seaborn** - Visualizações estáticas
- **Plotly** - Visualizações interativas
- **Yellowbrick** - Visualizações para ML

### Experimentação
- **MLflow** - Tracking de experimentos
- **Weights & Biases** - Monitoramento de experimentos
- **Optuna** - Otimização de hiperparâmetros

## 📦 Instalação

As dependências são gerenciadas pelo arquivo raiz do projeto. Certifique-se de ter o ambiente virtual ativo:

```bash
# Se usando Pipenv
pipenv shell

# Se usando venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

## 📋 Estrutura Sugerida

```text
ia/src/
├── datasets/
│   ├── data_clean.csv          # Dados limpos
│   ├── pre_processing.csv/     # Dados pré-processados
│   └── model.csv/              # Dados prontos para modelagem
├── notebooks/
│   ├── data_clean.ipynb      # Limpeza de dados
│   └── eda.ipynb             # Análise exploratória
│   ├── pre_processing.ipynb  # Desenvolvimento de modelos
│   └── model.ipynb           # Modelagem e avaliação de modelos
├── models/
    ├── trained/       # Modelos treinados
    └── artifacts/     # Artefatos dos modelos
```

## 🔬 Pipeline de ML Sugerido

1. **Coleta de Dados**
   - Importação e validação
   - Análise de qualidade dos dados

2. **Análise Exploratória**
   - Estatísticas descritivas
   - Visualizações
   - Identificação de padrões

3. **Pré-processamento**
   - Limpeza de dados
   - Tratamento de valores ausentes
   - Feature engineering

4. **Modelagem**
   - Seleção de algoritmos
   - Treinamento de modelos
   - Validação cruzada

5. **Avaliação**
   - Métricas de performance
   - Análise de erros
   - Interpretabilidade

6. **Deployment**
   - Serialização de modelos
   - Testes de produção
   - Monitoramento

## 📊 Notebooks Disponíveis

- `data_clean.ipynb` - Limpeza e preparação dos dados
- `eda.ipynb` - Análise exploratória inicial
- `pre_processing.ipynb` - Pré-Processamento dos dados
- `model.ipynb` - Treinamento e avaliação de modelos
