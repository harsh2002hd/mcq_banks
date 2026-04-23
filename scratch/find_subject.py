import json

with open('src/data/questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i, subject in enumerate(data['subjects']):
    print(f"Index: {i}, ID: {subject['id']}, Name: {subject['name']}, Questions: {len(subject['questions'])}")
