
from pathlib import Path
import pandas as pd

# Locate the project and dataset
project_folder = Path(__file__).resolve().parent.parent
data_file = (
    project_folder
    / "data"
    / "raw"
    / "DataCoSupplyChainDataset.csv"
)

# Load the full dataset
df = pd.read_csv(data_file, encoding="latin1")

print("=" * 50)
print("DATASET SIZE")
print("=" * 50)
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n" + "=" * 50)
print("DUPLICATE ROWS")
print("=" * 50)
print("Exact duplicate rows:", df.duplicated().sum())

print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)
missing = df.isnull().sum()
print(missing[missing > 0].sort_values(ascending=False))

print("\n" + "=" * 50)
print("COLUMN DATA TYPES")
print("=" * 50)
print(df.dtypes.to_string())

print("\nData-quality inspection completed.")
print("Original dataset was not modified.")
