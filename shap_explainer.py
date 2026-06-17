import shap

def create_explainer(model, X):

    explainer = shap.Explainer(model)

    shap_values = explainer(X)

    return shap_values
