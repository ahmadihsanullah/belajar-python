import json
# mekanisme konteks manager
with open('fileku.json', 'r') as fileku:
    dict = json.load(fileku)
    print(f'dictionary ku: {dict}')