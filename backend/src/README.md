# Backend

## 📝 Descrição

Módulo responsável pela API e lógica de backend do projeto de Data Science.

## 🚀 Funcionalidades

- API REST para servir modelos de ML
- Endpoints para processamento de dados
- Integração com banco de dados
- Autenticação e autorização
- Documentação automática da API

## 🛠️ Tecnologias Sugeridas

- **FastAPI** - Framework web moderno e rápido
- **SQLAlchemy** - ORM para Python
- **Pydantic** - Validação de dados
- **Uvicorn** - Servidor ASGI
- **PostgreSQL/SQLite** - Banco de dados

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

## 🔧 Configuração

1. Configure as variáveis de ambiente no arquivo `.env`
2. Execute as migrações do banco de dados
3. Inicie o servidor de desenvolvimento

```bash
# Exemplo de execução
uvicorn main:app --reload
```

## 📋 Estrutura Sugerida

```text
backend/src/
├── api/              # Endpoints da API
├── core/            # Configurações centrais
├── models/          # Modelos do banco de dados
├── schemas/         # Esquemas Pydantic
├── services/        # Lógica de negócio
├── utils/           # Utilitários
└── main.py          # Ponto de entrada da aplicação
```

## 📚 Documentação da API

Após executar a aplicação, a documentação estará disponível em:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`