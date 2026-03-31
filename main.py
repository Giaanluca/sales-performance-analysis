import pandas as pd
import sqlite3
import matplotlib.pyplot as plt


# Load sales dataset
df = pd.read_csv("data/sales_data.csv")

# Prepare date fields for monthly analysis
df["order_date"] = pd.to_datetime(
    df["order_date"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
)
df["month"] = df["order_date"].dt.to_period("M").astype(str)

# Create SQLite connection and load data
conn = sqlite3.connect("sales_database.db")
df.to_sql("sales", conn, if_exists="replace", index=False)


# Revenue by product
query_product = """
SELECT 
    product_name,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product_name
ORDER BY total_revenue DESC;
"""
product_revenue = pd.read_sql_query(query_product, conn)

print("Revenue by product:\n")
print(product_revenue)
print("\n" + "-" * 40 + "\n")


# Revenue by category
query_category = """
SELECT 
    category,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY category
ORDER BY total_revenue DESC;
"""
category_revenue = pd.read_sql_query(query_category, conn)

print("Revenue by category:\n")
print(category_revenue)
print("\n" + "-" * 40 + "\n")


# Units sold by product
query_units = """
SELECT 
    product_name,
    SUM(quantity) AS total_units_sold
FROM sales
GROUP BY product_name
ORDER BY total_units_sold DESC;
"""
product_units = pd.read_sql_query(query_units, conn)

print("Units sold by product:\n")
print(product_units)
print("\n" + "-" * 40 + "\n")


# Revenue by customer
query_customer = """
SELECT 
    customer_id,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY customer_id
ORDER BY total_revenue DESC;
"""
customer_revenue = pd.read_sql_query(query_customer, conn)

print("Revenue by customer:\n")
print(customer_revenue)
print("\n" + "-" * 40 + "\n")


# Monthly revenue trend
query_monthly = """
SELECT 
    month,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY month
ORDER BY month;
"""
monthly_revenue = pd.read_sql_query(query_monthly, conn)

print("Monthly revenue trend:\n")
print(monthly_revenue)
print("\n" + "-" * 40 + "\n")


# Revenue by product chart
print("\nGenerating revenue by product chart...\n")
plt.figure(figsize=(10, 6))
plt.bar(product_revenue["product_name"], product_revenue["total_revenue"])
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/revenue_by_product.png")
plt.show()


# Revenue by category chart
print("\nGenerating revenue by category chart...\n")
plt.figure(figsize=(8, 5))
plt.bar(category_revenue["category"], category_revenue["total_revenue"])
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.savefig("images/revenue_by_category.png")
plt.show()


# Revenue by customer chart
print("\nGenerating revenue by customer chart...\n")
plt.figure(figsize=(10, 6))
plt.bar(customer_revenue["customer_id"], customer_revenue["total_revenue"])
plt.title("Revenue by Customer")
plt.xlabel("Customer ID")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/revenue_by_customer.png")
plt.show()


# Monthly revenue trend chart
print("\nGenerating monthly revenue trend chart...\n")
plt.figure(figsize=(10, 6))
plt.plot(monthly_revenue["month"], monthly_revenue["total_revenue"], marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/monthly_revenue_trend.png")
plt.show()


conn.close()