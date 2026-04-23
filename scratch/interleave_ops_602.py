import json
import os

# Paths
questions_path = r'c:\Users\91635\Documents\programmes\assignment\aviation website\src\data\questions.json'
batch_files = [
    r'c:\Users\91635\Documents\programmes\assignment\aviation website\scratch\ops_batch_1.json',
    r'c:\Users\91635\Documents\programmes\assignment\aviation website\scratch\ops_batch_2.json',
    r'c:\Users\91635\Documents\programmes\assignment\aviation website\scratch\ops_batch_3.json'
]

# Load original data
with open(questions_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find 'ops' subject
ops_subject = next((s for s in data['subjects'] if s['id'] == 'ops'), None)
if not ops_subject:
    print("Error: 'ops' subject not found.")
    exit(1)

existing_questions = ops_subject['questions']
print(f"Existing questions: {len(existing_questions)}")

# Load new questions
new_questions = []
for bf in batch_files:
    with open(bf, 'r', encoding='utf-8') as f:
        new_questions.extend(json.load(f))

print(f"New questions: {len(new_questions)}")

# Interleave
total_target = len(existing_questions) + len(new_questions)
interleaved = []
e_idx = 0
n_idx = 0

# Calculate steps
# We want to distribute len(new_questions) over total_target slots.
# Every total_target / len(new_questions) slots, we insert a new one.
for i in range(total_target):
    # Determine if we should pick a new question
    # Heuristic: if i * len(new_questions) // total_target > n_idx, pick new
    if n_idx < len(new_questions) and (i * len(new_questions) // total_target) > n_idx:
        interleaved.append(new_questions[n_idx])
        n_idx += 1
    elif e_idx < len(existing_questions):
        interleaved.append(existing_questions[e_idx])
        e_idx += 1
    elif n_idx < len(new_questions):
        interleaved.append(new_questions[n_idx])
        n_idx += 1

# Final adjustment if n_idx < len(new_questions)
while n_idx < len(new_questions):
    interleaved.append(new_questions[n_idx])
    n_idx += 1

# Re-index
for i, q in enumerate(interleaved):
    q['id'] = f"ops-{i+1}"
    q['hasDetectedAnswer'] = False

# Update data
ops_subject['questions'] = interleaved
print(f"Total questions now: {len(interleaved)}")

# Save
with open(questions_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Successfully interleaved and saved to {questions_path}")
