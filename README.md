# Validação de Dados com Python e PostgreSQL

Projeto de validação de dados de um banco de e-commerce utilizando Python e PostgreSQL.

## Tecnologias
- Python
- PostgreSQL
- Pandas
- Psycopg2

## Objetivo
Automatizar verificações de qualidade dos dados, como:
- total de vendas
- valores nulos
- consistência das informações

## Como executar

1. Clone o repositório
2. pip install -r requirements.txt
3. Configure a conexão com o banco no arquivo `config.py`

```python
DB_CONFIG = {
    "host": "localhost",
    "database": "ecommerce",
    "user": "postgres",
    "password": "SUA_SENHA_AQUI",
    "port": 5432
}
```

