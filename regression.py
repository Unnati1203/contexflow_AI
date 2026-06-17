from xgboost import XGBRegressor

def train_regressor(X_train, y_train):

    model = XGBRegressor()

    model.fit(X_train, y_train)

    return model
