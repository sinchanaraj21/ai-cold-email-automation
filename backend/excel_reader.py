import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXCEL_FILE = os.path.join(BASE_DIR, "uploads", "HRs.xlsx")

REQUIRED_COLUMNS = [
    "First Name",
    "Email",
    "Company Name",
    "Title",
    "Full Name",
    "Company Website Full",
    "Email Status",
]

def load_hr_data():
    if not os.path.exists(EXCEL_FILE):
        raise FileNotFoundError(f"{EXCEL_FILE} not found.")

    df = pd.read_excel(EXCEL_FILE)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Ensure required columns exist
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise Exception(f"Missing columns: {missing}")

    # Keep only required columns
    df = df[REQUIRED_COLUMNS]

    # Remove rows without email
    df = df.dropna(subset=["Email"])

    # Remove duplicate emails
    df = df.drop_duplicates(subset=["Email"])

    # Keep only verified emails (if available)
    df["Email Status"] = df["Email Status"].fillna("").str.lower()
    df = df[df["Email Status"] == "verified"]

    return df.reset_index(drop=True)


if __name__ == "__main__":
    df = load_hr_data()

    print("\n===== CLEANED HR DATA =====")
    print(f"Total Verified HRs: {len(df)}")
    print(df.head())