import pandas as pd


def load(df, path):
  print(df)
  df.to_parquet(path)