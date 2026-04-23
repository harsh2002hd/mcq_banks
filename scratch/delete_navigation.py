import json

# Path
questions_path = r'c:\Users\91635\Documents\programmes\assignment\aviation website\src\data\questions.json'

# Load original data
with open(questions_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find 'Navigation' subject (id: img_3146)
original_count = len(data['subjects'])
data['subjects'] = [s for s in data['subjects'] if s['id'] != 'img_3146']
new_count = len(data['subjects'])

if original_count > new_count:
    print(f"Successfully removed 'Navigation' subject (img_3146).")
else:
    print("Warning: 'Navigation' subject (img_3146) was not found.")

# Save
with open(questions_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Updated dataset saved to {questions_path}")
