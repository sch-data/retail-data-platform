import pandas as pd
import psycopg2
from psycopg2.extras import execute_values


# Load cleaned data
df = pd.read_csv(
    "data/processed/online_retail_clean.csv",
    parse_dates=["InvoiceDate"],
    dtype={"Invoice": str}
)


# Connect to PostgreSQL
conn = psycopg2.connect(dbname="retail_data")
cur = conn.cursor()

# Clear existing data so the load can be rerun safely
cur.execute(
    """
    TRUNCATE TABLE invoice_items, invoices, products
    RESTART IDENTITY;
    """
)

# -------------------------
# Products
# -------------------------

products = (
    df[["StockCode", "Description"]]
    .drop_duplicates(subset=["StockCode"])
)

product_rows = list(products.itertuples(index=False, name=None))

execute_values(
    cur,
    """
    INSERT INTO products (stock_code, description)
    VALUES %s
    ON CONFLICT (stock_code) DO NOTHING
    """,
    product_rows,
)


# -------------------------
# Invoices
# -------------------------

invoices = (
    df[["Invoice", "InvoiceDate", "Customer ID", "Country"]]
    .drop_duplicates(subset=["Invoice"])
)

invoice_rows = [
    (
        row["Invoice"],
        row["InvoiceDate"],
        None if pd.isna(row["Customer ID"]) else int(row["Customer ID"]),
        row["Country"],
    )
    for _, row in invoices.iterrows()
]

execute_values(
    cur,
    """
    INSERT INTO invoices (
        invoice_id,
        invoice_date,
        customer_id,
        country
    )
    VALUES %s
    ON CONFLICT (invoice_id) DO NOTHING
    """,
    invoice_rows,
)


# -------------------------
# Invoice items
# -------------------------

invoice_items = df[
    ["Invoice", "StockCode", "Quantity", "Price"]
]

item_rows = list(invoice_items.itertuples(index=False, name=None))

execute_values(
    cur,
    """
    INSERT INTO invoice_items (
        invoice_id,
        stock_code,
        quantity,
        price
    )
    VALUES %s
    """,
    item_rows,
)


conn.commit()

cur.close()
conn.close()

print("Data loaded successfully.")