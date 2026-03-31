#Proyecto de Analisis de ventas para el portfolio
#SITUACION: Una empresa de e-commerce quiere entender qué productos venden más, cuáles generan más ingresos y cuáles parecen menos rentables, para tomar mejores decisiones comerciales.
#PREGUNTA: ¿Qué productos y categorías generan más ingresos, y cuáles parecen tener bajo rendimiento comercial?
#HERRAMIENTAS: Python, Pandas, SQLite, SQL.

import pandas as pd
import sqlite3

# Leer el archivo CSV
df = pd.read_csv("data/sales_data.csv")

# Crear conexión a base de datos SQLite
conn = sqlite3.connect("sales_database.db")

# Guardar el DataFrame como tabla SQL
df.to_sql("sales", conn, if_exists="replace", index=False)

# -------------------------------
# Consulta 1: ingresos por producto
# -------------------------------
query_product = """
SELECT 
    product_name,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product_name
ORDER BY total_revenue DESC;
"""

result_product = pd.read_sql_query(query_product, conn)

print("Ingresos por producto:\n")
print(result_product)
print("\n" + "-"*40 + "\n")

# -------------------------------
# Consulta 2: ingresos por categoría
# -------------------------------
query_category = """
SELECT 
    category,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY category
ORDER BY total_revenue DESC;
"""

result_category = pd.read_sql_query(query_category, conn)

print("Ingresos por categoría:\n")
print(result_category)
print("\n" + "-"*40 + "\n")

# -------------------------------
# Consulta 3: cantidad vendida por producto
# -------------------------------
query_quantity = """
SELECT 
    product_name,
    SUM(quantity) AS total_units_sold
FROM sales
GROUP BY product_name
ORDER BY total_units_sold DESC;
"""

result_quantity = pd.read_sql_query(query_quantity, conn)

print("Cantidad vendida por producto:\n")
print(result_quantity)
print("\n" + "-"*40 + "\n")

# -------------------------------
# Consulta 4: ingresos por cliente
# -------------------------------
query_customer = """
SELECT 
    customer_id,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY customer_id
ORDER BY total_revenue DESC;
"""

result_customer = pd.read_sql_query(query_customer, conn)

print("Ingresos por cliente:\n")
print(result_customer)

# Cerrar conexión
conn.close()