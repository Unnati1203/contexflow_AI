import pandas as pd

def profile_dataset(df):
    profile = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": df.isnull().sum().sum(),
        "numeric_columns": list(df.select_dtypes(include=['number']).columns),
        "categorical_columns": list(df.select_dtypes(exclude=['number']).columns)
    }

    return profile
