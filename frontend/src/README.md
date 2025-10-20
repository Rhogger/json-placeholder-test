# Frontend

## 📝 Descrição

Interface web para visualização e interação com os modelos de Data Science.

## 🚀 Funcionalidades

- Dashboard interativo
- Visualizações de dados
- Interface para upload de datasets
- Resultados de predições em tempo real
- Métricas e performance dos modelos

## 🛠️ Tecnologias Sugeridas

### Opção 1: Streamlit (Recomendado para prototipagem rápida)
- **Streamlit** - Framework para aplicações de ML
- **Plotly** - Gráficos interativos
- **Pandas** - Manipulação de dados

### Opção 2: Aplicação Web Tradicional
- **React/Vue/Angular** - Framework frontend
- **D3.js/Chart.js** - Visualizações
- **Bootstrap/Tailwind** - Estilização

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

## 🔧 Execução

### Com Streamlit

```bash
streamlit run app.py
```

### Com framework tradicional

```bash
# Instalar dependências específicas do frontend
npm install

# Executar em modo desenvolvimento
npm run dev
```

## 📋 Estrutura Sugerida

### Para Streamlit
```text
frontend/src/
├── components/      # Componentes reutilizáveis
├── pages/          # Páginas da aplicação
├── utils/          # Funções utilitárias
├── styles/         # Estilos customizados
└── app.py          # Aplicação principal
```

### Para framework tradicional
```text
frontend/src/
├── components/     # Componentes React/Vue
├── pages/         # Páginas/Views
├── services/      # Chamadas para API
├── styles/        # CSS/SCSS
├── utils/         # Utilitários
└── index.js       # Ponto de entrada
```

## 🎨 Features Implementadas

- [ ] Dashboard principal
- [ ] Upload de arquivos
- [ ] Visualização de dados
- [ ] Interface de predição
- [ ] Métricas dos modelos
- [ ] Exportação de resultados