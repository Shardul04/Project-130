import pandas as pd
import csv

df = pd.read_csv("Merged_dataset.csv")

del df["Luminosity"]
del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]

df.to_csv("Final.csv")
print(df.shape)