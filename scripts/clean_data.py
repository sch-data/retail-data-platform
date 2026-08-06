import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA = BASE_DIR / "data" / "raw" / "online_retail" / "online_retail_II.xlsx"
OUTPUT_DIR = BASE_DIR / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "online_retail_clean.csv"

def load_data():
    """Load the raw retail dataset."""
    return pd.read_excel(RAW_DATA, sheet_name="Year 2009-2010")

def clean_data(df):
    """Clean the raw retail dataset."""

    # Remove duplicate rows
    df = df.drop_duplicates().copy()

    # Remove rows without a product description
    df = df.dropna(subset=["Description"])

    # Remove returned or cancelled transactions
    df = df[df["Quantity"] > 0].copy()

    # Remove invalid negative prices
    df = df[df["Price"] > 0].copy()

    # Add transaction revenue
    df["Revenue"] = df["Quantity"] * df["Price"]

    return df


def save_data(df):
    """Save the cleaned dataset."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)


def main():
    df = load_data()
    df = clean_data(df)
    save_data(df)

    print(f"Cleaned data saved to: {OUTPUT_FILE}")
    print(f"Rows saved: {len(df):,}")


if __name__ == "__main__":
    main()