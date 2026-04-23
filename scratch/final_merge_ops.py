import json
import re

with open(r'c:\Users\91635\Documents\programmes\assignment\aviation website\scratch\parsed_ops_v2.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

def fix_question(q):
    text = q['questionText']
    options = q['options']
    correct_idx = q['correctAnswerIndex']
    
    # 1. Check if distractors are hidden in questionText
    # Pattern: text ending in : then followed by options separated by . or ;
    if ":" in text and len(options) <= 1:
        parts = text.split(":")
        main_text = parts[0] + ":"
        rest = ":".join(parts[1:]).strip()
        
        # Try splitting by common patterns
        # If rest has multiple sentences
        potential_opts = re.split(r'\.\s+', rest)
        if len(potential_opts) >= 2:
            # Clean up potential_opts
            potential_opts = [opt.strip() for opt in potential_opts if opt.strip()]
            if len(potential_opts) >= 2:
                # If we have 1 option currently, append these to it
                all_opts = potential_opts
                if options:
                    # If the current option is already in the split list, don't duplicate
                    if options[0] not in all_opts:
                        all_opts.append(options[0])
                
                # Update
                q['questionText'] = main_text
                q['options'] = all_opts
                # We need to find which one is correct. 
                # This is hard without (Correct) marker, but usually it's the one we had before.
                if options:
                    try:
                        q['correctAnswerIndex'] = q['options'].index(options[0])
                    except:
                        q['correctAnswerIndex'] = 0
                return q

    # 2. Hardcoded fixes for common patterns seen in the doc
    if "ICAO letter for weight" in text:
        q['options'] = ["L (Light)", "M (Medium)", "H (Heavy)", "S (Super)"]
        q['correctAnswerIndex'] = 1
    elif "non-radar separation of 2 minutes" in text:
        q['options'] = ["1 minute", "2 minutes", "3 minutes", "5 minutes"]
        q['correctAnswerIndex'] = 1
    elif "LIGHT aircraft landing behind a MEDIUM" in text:
        q['options'] = ["1 minute", "2 minutes", "3 minutes", "5 minutes"]
        q['correctAnswerIndex'] = 2
    elif "Wake turbulence category 'L'" in text:
        q['options'] = ["Less than 7,000 kg", "7,000 kg to 136,000 kg", "More than 136,000 kg", "Exactly 5,700 kg"]
        q['correctAnswerIndex'] = 0
    elif "squawk code" in text and "hijack" in text.lower():
        q['options'] = ["7500", "7600", "7700", "7000"]
        q['correctAnswerIndex'] = 0
    elif "microburst" in text and "increase in headwind" in text:
        q['options'] = ["An increase in headwind", "An increase in tailwind", "A decrease in airspeed", "A sudden updraft"]
        q['correctAnswerIndex'] = 0
        q['questionText'] = "Just after take-off an aircraft encounters a 'microburst' situated directly ahead. The initial indications will be:"
        
    # 3. If still only 1 option, generate generic distractors
    if len(q['options']) == 1:
        correct = q['options'][0]
        # AI-like generation of distractors based on common types
        if any(unit in correct.lower() for unit in ["ft", "feet", "m", "meters"]):
            num_match = re.search(r'(\d+)', correct)
            if num_match:
                val = int(num_match.group(1))
                q['options'] = [correct, f"{val+200} ft", f"{val-200} ft", f"{val+500} ft"]
                q['correctAnswerIndex'] = 0
        elif any(unit in correct.lower() for unit in ["min", "minutes"]):
            num_match = re.search(r'(\d+)', correct)
            if num_match:
                val = int(num_match.group(1))
                q['options'] = [correct, f"{val+5} minutes", f"{val-5} minutes", f"{val*2} minutes"]
                q['correctAnswerIndex'] = 0
        elif "yes" in correct.lower():
            q['options'] = ["Yes", "No", "Only in emergency", "With ATC approval"]
            q['correctAnswerIndex'] = 0
        elif "no" in correct.lower():
            q['options'] = ["No", "Yes", "Only in emergency", "With ATC approval"]
            q['correctAnswerIndex'] = 0
        else:
            # Fallback
            q['options'] = [correct, "Depends on the operator", "As specified in the AIP", "Only during IFR flights"]
            q['correctAnswerIndex'] = 0

    # Ensure exactly 4 options
    while len(q['options']) < 4:
        q['options'].append(f"Option {len(q['options'])+1}")
    if len(q['options']) > 4:
        q['options'] = q['options'][:4]
        
    return q

fixed_questions = [fix_question(q) for q in questions]

# Final merge into questions.json
questions_file = r'c:\Users\91635\Documents\programmes\assignment\aviation website\src\data\questions.json'
with open(questions_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create new subject entry
new_subject = {
    "id": "ops",
    "name": "Operational Procedures",
    "questions": fixed_questions
}

# Re-index ops questions
for i, q in enumerate(new_subject['questions']):
    q['id'] = f"ops-{i+1}"

# Check if subject already exists
found = False
for i, s in enumerate(data['subjects']):
    if s['id'] == 'ops':
        data['subjects'][i] = new_subject
        found = True
        break

if not found:
    data['subjects'].append(new_subject)

with open(questions_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Successfully integrated 'ops' subject with {len(fixed_questions)} questions.")
