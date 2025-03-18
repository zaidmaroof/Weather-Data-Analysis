import pandas as pd

def save_to_csv(df, filename="weather.csv"):
    df.to_csv(filename, index=False)