import json

with open('resource/userdata.json', 'r', encoding='utf-8') as file:
    parsed_data = json.load(file)

print("Manager" in parsed_data)
print(parsed_data)