import json


def load_config(path):
    try:
        with open(path) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"{path}: invalid JSON — {e}") from e

    if not isinstance(data, list):
        raise ValueError(f"{path}: expected a JSON array, got {type(data).__name__}")

    return data
