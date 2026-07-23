import pandas as pd

df = pd.read_csv("data/products.csv")
print(df.head(20).to_string())