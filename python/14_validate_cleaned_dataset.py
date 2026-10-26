
from pathlib import Path
import pandas as pd

project_folder = Path(__file__).resolve().parent.parent

cleaned_file = (
    project_folder
    / "data"
    / "processed"
    / "supply_chain_cleaned.csv"
)

df = pd.read_csv(cleaned_file, encoding="utf-8")

print("--- CLEANED DATASET VALIDATION ---")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Exact duplicate rows:", df.duplicated().sum())

sensitive_columns = [
    "Customer Email",
    "Customer Password",
    "Customer Fname",
    "Customer Lname",
    "Customer Street",
    "Customer Zipcode",
    "Order Zipcode",
]

remaining_sensitive = [
    column for column in sensitive_columns
    if column in df.columns
]

print("Customer-identifying columns remaining:", remaining_sensitive)

print("\nDelivery Timing counts:")
print(df["Delivery Timing"].value_counts().to_string())

print("\nColumn names:")
print(df.columns.tolist())

print("\nValidation completed.")
