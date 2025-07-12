import pandas as pd

def clean_column_names(df):
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return df

def load_csv(filepath):
    try:
        df = pd.read_csv(filepath)
        return clean_column_names(df)
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return pd.DataFrame()