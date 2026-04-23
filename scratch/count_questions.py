import json
import os

file_path = r'c:\Users\91635\Documents\programmes\assignment\aviation website\src\data\questions.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"{'Subject ID':<20} | {'Subject Name':<40} | {'Count':<5}")
print("-" * 70)

total_count = 0
for subject in data.get('subjects', []):
    count = len(subject.get('questions', []))
    print(f"{subject.get('id'):<20} | {subject.get('name'):<40} | {count:<5}")
    total_count += count

print("-" * 70)
print(f"{'Total':<63} | {total_count:<5}")
