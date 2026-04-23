import json

with open(r'c:\Users\91635\Documents\programmes\assignment\aviation website\scratch\parsed_ops_v2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

needing = [q for q in data if len(q['options']) < 4]

with open(r'c:\Users\91635\Documents\programmes\assignment\aviation website\scratch\needing_distractors.txt', 'w', encoding='utf-8') as f:
    for q in needing:
        correct_text = q['options'][q['correctAnswerIndex']] if q['options'] and q['correctAnswerIndex'] != -1 else "MISSING"
        f.write(f"{q['id']}|{q['questionText']}|{correct_text}\n")

print(f"Saved {len(needing)} questions to needing_distractors.txt")
