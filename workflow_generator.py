def generate_workflow(task):

    workflows = {
        "classification": [
            "Preprocessing",
            "Random Forest",
            "SHAP Explanation"
        ],

        "regression": [
            "Preprocessing",
            "XGBoost Regressor",
            "SHAP Explanation"
        ],

        "clustering": [
            "Preprocessing",
            "KMeans"
        ]
    }

    return workflows.get(task)
