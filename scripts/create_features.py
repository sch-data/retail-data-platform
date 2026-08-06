import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "online_retail_clean.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "online_retail_features.csv"


def load_data():
    """Load the cleaned retail dataset."""
    return pd.read_csv(
        INPUT_FILE,
        low_memory=False,
        parse_dates=["InvoiceDate"]
    )


def create_features(df):
    """Create features for analysis."""
    df = df.copy()

    df["Year"] = df["InvoiceDate"].dt.year
    df["Month"] = df["InvoiceDate"].dt.month
    df["YearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)

    return df


def save_data(df):
    """Save the feature-engineered dataset."""
    df.to_csv(OUTPUT_FILE, index=False)


def main():
    df = load_data()
    df = create_features(df)
    save_data(df)

    print(f"Feature data saved to: {OUTPUT_FILE}")
    print(f"Rows saved: {len(df):,}")


if __name__ == "__main__":
    main()