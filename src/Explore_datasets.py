import pandas as pd
from pathlib import Path

data_dir = Path("data")
csv_files = data_dir.glob("*.csv")

for file in csv_files:
    df = pd.read_csv(file)
    
    print("\n" + "=" * 50)
    print(f"\ndataset: {file.name}")
    print("=" * 50)
    
    print(f"rows: {df.shape[0]}")
    print(f"columns: {df.shape[1]}")
    print(f"column names: {list(df.columns)}")

    print("\nduplicate records:")
    print(df.duplicated().sum())
        
    print("\nmissing records:")
    print(df.isnull().sum())
        
    print("\ndataset information:")
    df.info()


