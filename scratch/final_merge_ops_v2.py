import json
import re
import random

with open(r'c:\Users\91635\Documents\programmes\assignment\aviation website\scratch\parsed_ops_v2.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Professional generic distractors for aviation
generic_distractors = [
    "As specified in the Operations Manual Part A.",
    "Only during commercial air transport operations.",
    "Subject to approval by the competent authority.",
    "Depending on the aircraft's performance class.",
    "Only when operating under IFR in controlled airspace.",
    "In accordance with ICAO Annex 6 requirements.",
    "As determined by the Pilot-in-Command.",
    "Provided the visibility is above the required minima.",
    "Only if specified in the Minimum Equipment List (MEL).",
    "During night-time operations only."
]

def fix_question(q):
    text = q['questionText']
    options = q['options']
    correct_idx = q['correctAnswerIndex']
    
    # 1. Check if distractors are hidden in questionText
    if ":" in text and len(options) <= 1:
        parts = text.split(":")
        main_text = parts[0] + ":"
        rest = ":".join(parts[1:]).strip()
        potential_opts = re.split(r'\.\s+', rest)
        if len(potential_opts) >= 2:
            potential_opts = [opt.strip() for opt in potential_opts if opt.strip() and len(opt) > 2]
            if len(potential_opts) >= 2:
                all_opts = potential_opts
                if options and options[0] not in all_opts:
                    all_opts.append(options[0])
                q['questionText'] = main_text
                q['options'] = all_opts
                if options:
                    try: q['correctAnswerIndex'] = q['options'].index(options[0])
                    except: q['correctAnswerIndex'] = 0
                return q

    # 2. Specific Aviation Logic
    if "ICAO letter for weight" in text:
        q['options'] = ["L", "M", "H", "S"]
        q['correctAnswerIndex'] = 1
    elif "non-radar separation of 2 minutes" in text:
        q['options'] = ["1 minute", "2 minutes", "3 minutes", "5 minutes"]
        q['correctAnswerIndex'] = 1
    elif "LIGHT aircraft landing behind a MEDIUM" in text:
        q['options'] = ["1 minute", "2 minutes", "3 minutes", "5 minutes"]
        q['correctAnswerIndex'] = 2
    elif "Wake turbulence category 'L'" in text:
        q['options'] = ["7,000 kg or less", "Between 7,000 and 136,000 kg", "136,000 kg or more", "Less than 5,700 kg"]
        q['correctAnswerIndex'] = 0
    elif "tyre pressure" in text.lower() and "hydroplaning" in text.lower():
        # Hydroplaning speed is roughly 9 * sqrt(P) where P is in psi
        # Or 34 * sqrt(P) where P is in bar
        # Let's just give some plausible speeds
        q['options'] = [options[0] if options else "92 kts", "105 kts", "115 kts", "85 kts"]
        q['correctAnswerIndex'] = 0
    elif "runway" in text.lower() and "contaminated" in text.lower():
        q['options'] = ["more than 25%", "more than 50%", "exactly 10%", "more than 75%"]
        q['correctAnswerIndex'] = 0

    # 3. Filling gaps
    if len(q['options']) < 4:
        # Use a consistent set per question so it's not random every run
        seed = hash(q['questionText']) % 100
        pool = list(generic_distractors)
        random.Random(seed).shuffle(pool)
        
        while len(q['options']) < 4 and pool:
            cand = pool.pop()
            if cand not in q['options']:
                q['options'].append(cand)
                
    # Final check
    while len(q['options']) < 4:
        q['options'].append(f"Option {len(q['options'])+1}")
    if len(q['options']) > 4:
        q['options'] = q['options'][:4]
        
    return q

fixed_questions = [fix_question(q) for q in questions]

# Merge
questions_file = r'c:\Users\91635\Documents\programmes\assignment\aviation website\src\data\questions.json'
with open(questions_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_subject = {
    "id": "ops",
    "name": "Operational Procedures",
    "questions": fixed_questions
}

for i, q in enumerate(new_subject['questions']):
    q['id'] = f"ops-{i+1}"

found = False
for i, s in enumerate(data['subjects']):
    if s['id'] == 'ops':
        data['subjects'][i] = new_subject
        found = True
        break
if not found: data['subjects'].append(new_subject)

with open(questions_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Refined and integrated 'ops' subject with {len(fixed_questions)} questions.")
