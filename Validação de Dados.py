import psycopg2
import pandas as pd

# =========================================
# CONEXÃO COM POSTGRESQL
# =========================================

conn = psycopg2.connect(
    host="localhost",
    database="ecommerce",
    user="postgres",
    password="SUA_SENHA_AQUI",
    port="5432"
)

print("✅ Conexão com PostgreSQL realizada com sucesso.")


# =========================================
# 1️⃣ TOTAL DE VENDAS
# =========================================

query_total_vendas = """
SELECT COUNT(*) AS total_vendas
FROM vendas;
"""

df_total = pd.read_sql(query_total_vendas, conn)
print("\nTotal de vendas:")
print(df_total)


# =========================================
# 2️⃣ PERÍODO DAS VENDAS
# =========================================

query_periodo = """
SELECT
    MIN(data_venda) AS primeira_venda,
    MAX(data_venda) AS ultima_venda
FROM vendas;
"""

df_periodo = pd.read_sql(query_periodo, conn)
print("\nPeríodo das vendas:")
print(df_periodo)


# =========================================
# 3️⃣ VENDAS POR STATUS
# =========================================

query_status = """
SELECT
    status_venda,
    COUNT(*) AS total
FROM vendas
GROUP BY status_venda
ORDER BY total DESC;
"""

df_status = pd.read_sql(query_status, conn)
print("\nStatus das vendas:")
print(df_status)


# =========================================
# 4️⃣ FATURAMENTO TOTAL
# =========================================

query_faturamento = """
SELECT
    SUM(valor_pago) AS faturamento_total
FROM pagamentos
WHERE status = 'pago';
"""

df_faturamento = pd.read_sql(query_faturamento, conn)
print("\nFaturamento total:")
print(df_faturamento)


# =========================================
# 5️⃣ TOP 10 PRODUTOS MAIS VENDIDOS
# =========================================

query_produtos = """
SELECT
    p.nome,
    SUM(iv.quantidade) AS total_vendido
FROM itens_venda iv
JOIN produtos p ON p.produto_id = iv.produto_id
GROUP BY p.nome
ORDER BY total_vendido DESC
LIMIT 10;
"""

df_produtos = pd.read_sql(query_produtos, conn)
print("\nTop 10 produtos vendidos:")
print(df_produtos)


# =========================================
# 6️⃣ VENDAS POR CANAL
# =========================================

query_canais = """
SELECT
    c.nome AS canal,
    COUNT(v.venda_id) AS total_vendas
FROM vendas v
JOIN canais_venda c ON c.canal_id = v.canal_id
GROUP BY c.nome
ORDER BY total_vendas DESC;
"""

df_canais = pd.read_sql(query_canais, conn)
print("\nVendas por canal:")
print(df_canais)


# =========================================
# FECHAR CONEXÃO
# =========================================

conn.close()
print("\n🔒 Conexão encerrada.")