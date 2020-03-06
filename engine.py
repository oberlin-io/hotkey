import yaml

with open('data.yaml', 'r') as f:
    d = f.read()
    y = yaml.safe_load(d)
    print(type(y))
