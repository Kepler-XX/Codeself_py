import yaml
import os


def get_ya():
    cur_path = os.path.dirname(os.path.realpath(__file__))
    yaml_path = os.path.join(cur_path, "main.yaml")

    with open(yaml_path, 'r', encoding='utf-8') as f:
        ya = f.read()

    ya_json = yaml.safe_load(ya)
    return ya_json
