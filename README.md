# JSONPlaceholder API Tutorial 📊

Tutorial completo para consumir APIs REST usando Python, demonstrando integração com JSONPlaceholder para operações GET e POST com manipulação de dados usando Pandas.

## 📋 Pré-requisitos

- Python 3.12 ou superior
- Git
- Pipenv ou venv (para gerenciamento de dependências)

## ✨ Tecnologias Utilizadas

- **Python 3.12** - Linguagem principal
- **Requests** - Biblioteca para requisições HTTP
- **Pandas** - Manipulação e análise de dados
- **JSONPlaceholder** - API REST fake para testes
- **Ruff** - Linting e formatação de código

## 🔧 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/Rhogger/json-placeholder-test.git
cd json-placeholder-test
```

### 2. Configure o ambiente virtual

Escolha uma das opções abaixo:

#### Opção A: Usando Pipenv (Recomendado)

```bash
# Instale o Pipenv (se não tiver instalado)
pip install pipenv

# Instale as dependências
pipenv install

# Ative o ambiente virtual
pipenv shell
```

#### Opção B: Usando venv

```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Linux/Mac:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

## 📁 Estrutura do Projeto

```text
json-placeholder-test/
├── backend/                 # Scripts de tutorial para APIs
│   ├── src/                # Código fonte dos exemplos
│   │   ├── api_data_extractor.py  # Tutorial GET com Pandas
│   │   ├── api_post_creator.py    # Tutorial POST
│   │   └── README.md       # Documentação dos exemplos
├── .vscode/                # Configurações do VS Code
├── .gitattributes          # Configuração para diffs do Git
├── .gitignore              # Arquivos ignorados pelo Git
├── Pipfile                 # Dependências do projeto
├── Pipfile.lock            # Lock das dependências
├── ruff.toml              # Configuração do Ruff
├── DEV.md                 # Instruções de desenvolvimento
└── README.md              # Este arquivo
```

## 🚀 Como Executar

### 1. Tutorial de Extração de Dados (GET)

Execute o script que demonstra como obter dados de usuários da API JSONPlaceholder:

```bash
# Com Pipenv
pipenv run python backend/src/api_data_extractor.py

# Com venv (após ativar)
python backend/src/api_data_extractor.py
```

### 2. Tutorial de Criação de Posts (POST)

Execute o script que demonstra como criar novos posts via API:

```bash
# Com Pipenv
pipenv run python backend/src/api_post_creator.py

# Com venv (após ativar)
python backend/src/api_post_creator.py
```

## 👨‍💻 Desenvolvimento

Instruções para desenvolvimento estão [aqui](./DEV.md)

## 📚 Documentação Adicional

- [Backend README](./backend/src/README.md) - Documentação específica dos tutoriais

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---
