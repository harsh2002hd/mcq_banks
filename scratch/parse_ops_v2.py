import re
import json

file_path = r'c:\Users\91635\Documents\programmes\assignment\aviation website\scratch\ops_raw_text.txt'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

questions = []
current_q = None

q_pattern = re.compile(r'^Q\s*(\d+)(?:/\d+)?[:\s]+(.*)', re.IGNORECASE)

for line in lines:
    line = line.strip()
    if not line: continue
    
    m = q_pattern.match(line)
    if m:
        if current_q:
            questions.append(current_q)
        current_q = {
            'id': m.group(1),
            'questionText': m.group(2),
            'raw_options': []
        }
    elif current_q:
        current_q['raw_options'].append(line)

if current_q:
    questions.append(current_q)

# Now process each question's raw options
final_questions = []
for q in questions:
    options = []
    correct_idx = -1
    q_text = q['questionText']
    
    # Sometimes options are buried in the question text or the raw_options are messy
    # Heuristic: 
    # 1. Check for lines that look like options (start with numbers, have (Correct), etc.)
    # 2. If a line is "Correct Option: X", it's a pointer.
    
    potential_options = []
    for line in q['raw_options']:
        # If it's a pointer to a previous option
        if "Correct Option:" in line:
            # We'll handle this after collecting all options
            q_text += " " + line
            continue
            
        # If it's an option
        if "(Correct)" in line:
            clean = line.replace("(Correct)", "").strip()
            # If it starts with a number like "1. ", remove it but remember it
            opt_m = re.match(r'^(\d+)\s*[\).]*\s*(.*)', clean)
            if opt_m:
                text = opt_m.group(2).strip()
                if not text: text = opt_m.group(1) # e.g. "1 (Correct)" -> option is "1"
            else:
                text = clean
            
            potential_options.append(text)
            correct_idx = len(potential_options) - 1
        else:
            opt_m = re.match(r'^(\d+)\s*[\).]*\s*(.*)', line)
            if opt_m:
                text = opt_m.group(2).strip()
                if not text: text = opt_m.group(1)
                potential_options.append(text)
            else:
                # If it's not a numbered option and we haven't seen any numbered options yet, 
                # it's likely more question text.
                if not potential_options:
                    q_text += " " + line
                else:
                    # Append to last option
                    potential_options[-1] += " " + line
                    
    # Handle "Correct Option: X" if correct_idx is still -1
    if correct_idx == -1:
        ans_match = re.search(r'Correct Option:\s*([\d,]+)', q_text)
        if ans_match:
            try:
                indices = ans_match.group(1).split(',')
                correct_idx = int(indices[0]) - 1
                q_text = q_text.split('Correct Option:')[0].strip()
            except:
                pass
                
    # Final cleanup of options
    # If only one option and it's marked as correct (by default or index), we have our "needs distractors" case.
    if correct_idx == -1 and len(potential_options) == 1:
        correct_idx = 0
        
    final_questions.append({
        'id': f"ops-{q['id']}",
        'questionText': q_text.strip(),
        'options': potential_options,
        'correctAnswerIndex': correct_idx,
        'hasDetectedAnswer': False
    })

# Identify questions needing distractors
needing_distractors = [q for q in final_questions if len(q['options']) < 4]

print(f"Total questions: {len(final_questions)}")
print(f"Needing distractors: {len(needing_distractors)}")

# Output for AI processing
with open(r'c:\Users\91635\Documents\programmes\assignment\aviation website\scratch\parsed_ops_v2.json', 'w', encoding='utf-8') as f:
    json.dump(final_questions, f, indent=2)
