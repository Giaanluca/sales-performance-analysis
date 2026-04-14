from scripts.etl import run_pipeline
import sqlite3
import pandas as pd
import os

DB_PATH = "data/sales.db"


def run_analysis():
    print("\nRunning SQL analysis...\n")

    conn = sqlite3.connect(DB_PATH)

    queries = {
        "Revenue by Product": """
            SELECT product_name, SUM(quantity * price) AS total_revenue
            FROM sales
            GROUP BY product_name
            ORDER BY total_revenue DESC;
        """,

        "Revenue by Category": """
            SELECT category, SUM(quantity * price) AS total_revenue
            FROM sales
            GROUP BY category
            ORDER BY total_revenue DESC;
        """,

        "Top Customers": """
            SELECT customer_id, SUM(quantity * price) AS total_revenue
            FROM sales
            GROUP BY customer_id
            ORDER BY total_revenue DESC;
        """,

        "Monthly Revenue": """
            SELECT strftime('%Y-%m', order_date) AS month,
                   SUM(quantity * price) AS total_revenue
            FROM sales
            GROUP BY month
            ORDER BY month;
        """
    }

    for title, query in queries.items():
        df = pd.read_sql_query(query, conn)
        print(f"{title}:\n")
        print(df.head(10))
        print("\n" + "-" * 40 + "\n")

    conn.close()


if __name__ == "__main__":
    print("Starting pipeline...\n")

    # 1. Ejecutar ETL
    run_pipeline()

    # 2. Ejecutar análisis SQL
    run_analysis()

    print("Process completed successfully.")