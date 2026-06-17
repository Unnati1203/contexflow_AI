import json

FILE = "workflow_history.json"

def save_workflow(info):

    try:
        with open(FILE, "r") as f:
            data = json.load(f)

    except:
        data = []

    data.append(info)

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)
