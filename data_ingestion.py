import pandas as pd
import os

folder = "data/raw"

files = [f for f in os.listdir(folder) if f.endswith(".csv")]

print("Total CSV files:", len(files))

for file in files:
    print("\n" + "="*50)
    print("Dataset:", file)

    df = pd.read_csv(os.path.join(folder, file))

    print("Shape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nHead:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())