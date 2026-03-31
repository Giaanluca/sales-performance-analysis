#Proyecto de Analisis de ventas para el portfolio
#SITUACION: Una empresa de e-commerce quiere entender qué productos venden más, cuáles generan más ingresos y cuáles parecen menos rentables, para tomar mejores decisiones comerciales.
#PREGUNTA: ¿Qué productos y categorías generan más ingresos, y cuáles parecen tener bajo rendimiento comercial?
#HERRAMIENTAS: Python, Pandas, SQLite, SQL.

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Load transactional sales dataset
df = pd.read_csv("data/sales_data.csv")
# Store dataset in SQLite for SQL-based analysis
conn = sqlite3.connect("sales_database.db")
df.to_sql("sales", conn, if_exists="replace", index=False)

# -------------------------------
# Query 1: Revenue by product
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

print("Revenue by product:\n")
print(result_product)
print("\n" + "-"*40 + "\n")

# -------------------------------
# Query 2: Revenue by category
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

print("Revenue by category:\n")
print(result_category)
print("\n" + "-"*40 + "\n")

# -------------------------------
# Query 3: Units sold by product
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

print("Units sold by product:\n")
print(result_quantity)
print("\n" + "-"*40 + "\n")

# -------------------------------
# Query 4: Revenue by customer
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

print("Revenue by customer:\n")
print(result_customer)

# -------------------------------
# Visualization: Revenue by product
# -------------------------------
plt.figure(figsize=(10, 6))
plt.bar(result_product["product_name"], result_product["total_revenue"])
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/revenue_by_product.png")
plt.show()

# -------------------------------
# Visualization: Revenue by category
# -------------------------------
plt.figure(figsize=(8, 5))
plt.bar(result_category["category"], result_category["total_revenue"])
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.savefig("images/revenue_by_category.png")
plt.show()

print("\nGenerating customer revenue chart...\n")

# -------------------------------
# Visualization: Revenue by customer
# -------------------------------
plt.figure(figsize=(10, 6))
plt.bar(result_customer["customer_id"], result_customer["total_revenue"])
plt.title("Revenue by Customer")
plt.xlabel("Customer ID")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/revenue_by_customer.png")
plt.show()

conn.close()