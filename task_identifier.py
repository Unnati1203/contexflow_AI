def identify_task(df):

    if "target" in df.columns:
        unique = df["target"].nunique()

        if unique <= 10:
            return "classification"

        return "regression"

    return "clustering"
