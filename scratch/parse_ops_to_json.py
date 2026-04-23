import re
import json

file_path = r'c:\Users\91635\Documents\programmes\assignment\aviation website\scratch\ops_raw_text.txt'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

questions = []
current_q = None

# Pattern for question start: Q1: or Q 1/602:
q_pattern = re.compile(r'^Q\s*(\d+)(?:/\d+)?[:\s]+(.*)', re.IGNORECASE)

for i, line in enumerate(lines):
    line = line.strip()
    if not line: continue
    
    m = q_pattern.match(line)
    if m:
        if current_q:
            questions.append(current_q)
        current_q = {
            'id': m.group(1),
            'questionText': m.group(2),
            'options': [],
            'correctAnswerIndex': -1
        }
    elif current_q:
        # Check if it's an option or more question text
        # If it contains (Correct), it's definitely an option
        if "(Correct)" in line:
            text = line.replace("(Correct)", "").strip()
            # If text starts with "1 ", "1. ", "1) ", remove it
            text = re.sub(r'^\d+[\s\.)]*\s*', '', text)
            current_q['options'].append(text)
            current_q['correctAnswerIndex'] = len(current_q['options']) - 1
        else:
            # If it starts with a number, it's likely an option
            opt_m = re.match(r'^(\d+)\s*[\).]*\s*(.*)', line)
            if opt_m:
                current_q['options'].append(opt_m.group(2).strip())
            else:
                # If we have no options yet, it's likely more question text
                if not current_q['options']:
                    current_q['questionText'] += " " + line
                else:
                    # If we have options, it might be more text for the last option
                    # OR it might be an option that doesn't start with a number
                    # Heuristic: if the line is short or looks like an option, or if we have < 4 options and the next line is a question...
                    # Let's assume for now any non-empty line after the question starts is an option if it's not a question itself.
                    # BUT wait, some questions are multi-line.
                    
                    # Check if next non-empty line is a question
                    is_next_q = False
                    for j in range(i + 1, len(lines)):
                        next_line = lines[j].strip()
                        if next_line:
                            if q_pattern.match(next_line):
                                is_next_q = True
                            break
                    
                    if is_next_q and len(current_q['options']) == 0:
                         # This question has no options at all? Unusual.
                         pass
                    elif len(current_q['options']) > 0:
                        # Append to last option
                        current_q['options'][-1] += " " + line
                    else:
                        # Still question text
                        current_q['questionText'] += " " + line

if current_q:
    questions.append(current_q)

# Post-processing: clean up IDs and ensure each has a correct answer
# Some questions might have indices as options (e.g. "1", "2", "3", "4") 
# and then a line "Correct Option: 2"
# My parser might have missed that. Let's fix.

for q in questions:
    # If question text contains "Correct Option: X"
    match = re.search(r'Correct Option:\s*([\d,]+)', q['questionText'])
    if match:
        indices = match.group(1).split(',')
        try:
            q['correctAnswerIndex'] = int(indices[0]) - 1
            # Remove the "Correct Option" part from question text
            q['questionText'] = q['questionText'].split('Correct Option:')[0].strip()
        except:
            pass
            
    # Clean up options
    q['options'] = [re.sub(r'^\d+[\s\.)]*\s*', '', opt).strip() for opt in q['options']]
    
    # If correct index is still -1 but there's only one option, assume it's the correct one
    if q['correctAnswerIndex'] == -1 and len(q['options']) == 1:
        q['correctAnswerIndex'] = 0

# Final check: count those needing options
needing_options = [q for q in questions if len(q['options']) < 4]

print(f"Total questions: {len(questions)}")
print(f"Questions needing more options: {len(needing_options)}")

with open(r'c:\Users\91635\Documents\programmes\assignment\aviation website\scratch\parsed_ops_v1.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2)
