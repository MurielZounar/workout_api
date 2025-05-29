# Workout API

Este projeto é uma API RESTful desenvolvida em Python, utilizando o framework FastAPI, com o objetivo de gerenciar rotinas de treino. A API permite o cadastro, consulta, atualização e exclusão de exercícios físicos, facilitando a organização de treinos personalizados.

## Funcionalidades

* CRUD completo para exercícios físicos.
* Integração com banco de dados relacional via SQLAlchemy.
* Migrações de banco de dados gerenciadas pelo Alembic.
* Documentação automática dos endpoints com Swagger UI.
* Containerização com Docker e orquestração com Docker Compose.

## Tecnologias Utilizadas

* [Python 3.10](https://www.python.org/downloads/release/python-3100/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Alembic](https://alembic.sqlalchemy.org/)
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)

## Pré-requisitos

* [Python 3.10](https://www.python.org/downloads/release/python-3100/)
* [Docker](https://www.docker.com/get-started) e [Docker Compose](https://docs.docker.com/compose/install/)

## Instalação e Execução

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/MurielZounar/workout_api.git
   cd workout_api
   ```

2. **Configure as variáveis de ambiente:**

   Crie um arquivo `.env` na raiz do projeto e defina as variáveis necessárias, como as credenciais do banco de dados.

3. **Construa e inicie os containers:**

   ```bash
   docker-compose up --build
   ```

   A API estará disponível em `http://localhost:8000`.

4. **Acesse a documentação interativa:**

   Visite `http://localhost:8000/docs` para visualizar e testar os endpoints disponíveis.

## Estrutura do Projeto

```bash
├── alembic/                 # Diretório de migrações do Alembic
├── workout_api/             # Código-fonte da aplicação
│   ├── models/              # Definições das classes de modelo (ORM)
│   ├── schemas/             # Definições dos schemas (Pydantic)
│   ├── routers/             # Definições das rotas/endpoints
│   └── main.py              # Ponto de entrada da aplicação
├── alembic.ini              # Configuração do Alembic
├── docker-compose.yml       # Configuração do Docker Compose
├── Dockerfile               # Dockerfile para a aplicação
├── requirements.txt         # Dependências do projeto
└── README.md                # Documentação do projeto
```

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
