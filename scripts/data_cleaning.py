import pandas as pd
import os
import sqlite3

# Rutas
import os

# Base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_PATH = os.path.join(BASE_DIR, "data", "raw", "sales_data.csv")
PROCESSED_PATH = os.path.join(BASE_DIR, "data", "processed", "clean_sales.csv")
DB_PATH = os.path.join(BASE_DIR, "data", "sales.db")

def extract():
    print("Extracting data...")
    df = pd.read_csv(RAW_PATH)
    return df

def transform(df):
    print("Transforming data...")

    # Eliminar filas sin customer_id
    df = df.dropna(subset=["customer_id"])

    # Convertir fechas
    df["order_date"] = pd.to_datetime(
        df["order_date"],
        format="mixed",
        dayfirst=True,
        errors="coerce"
    )

    df = df.dropna(subset=["order_date"])

    df["revenue"] = df["quantity"] * df["price"]

    df = df[df["quantity"] > 0]
    df = df[df["price"] > 0]

    df["month"] = df["order_date"].dt.to_period("M").astype(str)

    return df

def load_csv(df):
    print("Saving cleaned CSV...")
    os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)

def load_sql(df):
    print("Loading data into SQLite...")

    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    df.to_sql(
        "sales",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

def run_pipeline():
    df = extract()
    df = transform(df)
    load_csv(df)
    load_sql(df)
    print("ETL pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()