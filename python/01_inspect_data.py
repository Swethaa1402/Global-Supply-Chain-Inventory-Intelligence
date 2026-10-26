
from pathlib import Path
import pandas as pd

# Find our project folder
project_folder = Path(__file__).resolve().parent.parent

# Locate the original CSV
data_file = (
    project_folder
    / "data"
    / "raw"
    / "DataCoSupplyChainDataset.csv"
)

# Check whether the file exists
if not data_file.exists():
    print("ERROR: Dataset file not found.")
else:
    print("Dataset file found!")

    # Read only the first 5 rows
    df = pd.read_csv(
        data_file,
        nrows=5,
        encoding="latin1"
    )

    print("\n--- FIRST 5 ROWS ---")
    print(df.head())

    print("\n--- DATASET COLUMNS ---")
    print(df.columns.tolist())

    print("\n--- DATA TYPES ---")
    print(df.dtypes)
