import json

# Path
questions_path = r'c:\Users\91635\Documents\programmes\assignment\aviation website\src\data\questions.json'

# Load original data
with open(questions_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find 'ops' subject
ops_subject = next((s for s in data['subjects'] if s['id'] == 'ops'), None)
if not ops_subject:
    print("Error: 'ops' subject not found.")
    exit(1)

# Attach images to first 5 questions
for i in range(5):
    if i < len(ops_subject['questions']):
        q = ops_subject['questions'][i]
        q['image'] = f"images/opsQ{i+1}.png"
        print(f"Attached images/opsQ{i+1}.png to {q['id']}")

# Save
with open(questions_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Updated dataset saved to {questions_path}")
