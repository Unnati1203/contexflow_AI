from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

def preprocess_data(X):

    imputer = SimpleImputer(strategy="mean")
    X = imputer.fit_transform(X)

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    return X
