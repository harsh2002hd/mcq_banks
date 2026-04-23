import re

file_path = r'c:\Users\91635\Documents\programmes\assignment\aviation website\scratch\ops_raw_text.txt'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

questions = []
current_question = None

for line in lines:
    line = line.strip()
    if not line:
        continue
        
    # Match Q1:, Q 1:, Q1/602:, Q 482/602: etc.
    q_match = re.match(r'^Q\s*(\d+)(?:/\d+)?[:\s]*(.*)', line, re.IGNORECASE)
    if q_match:
        if current_question:
            questions.append(current_question)
        current_question = {
            'id': q_match.group(1),
            'text': q_match.group(2),
            'options': [],
            'correctIndex': -1
        }
        continue
    
    if current_question:
        # Check if it's an option
        # Options often look like "1", "2 (Correct)", "text", "1) text", etc.
        # This is tricky because the format varies.
        
        # If it looks like a new question already started (sometimes they are multiline)
        # But we handled that with q_match.
        
        # Try to identify options
        if "(Correct)" in line:
            clean_opt = line.replace("(Correct)", "").strip()
            # If the option is just a number like "1", and there was a previous line with the text for 1...
            # but in this file, it seems the text is often in the same line or the line before.
            current_question['options'].append(clean_opt)
            current_question['correctIndex'] = len(current_question['options']) - 1
        elif "Correct Option:" in line:
            # Handle "Correct Option: 1,3" or "Correct Option: 2"
            ans_match = re.search(r'Correct Option:\s*([\d,]+)', line)
            if ans_match:
                # This usually means the options were listed before, and this line tells which one is correct.
                # But sometimes it's "Correct Option: 1 (text)"
                # Let's see if we can parse the indices.
                indices = ans_match.group(1).split(',')
                # If only one index, set it. If multiple, it might be a multi-choice question.
                # For now, let's just mark the first one as correct for the sake of simplicity or handled later.
                try:
                    idx = int(indices[0]) - 1
                    current_question['correctIndex'] = idx
                except:
                    pass
        else:
            # It's either an option or part of the question text.
            # If we don't have any options yet, and the text is not a number, it might be more question text.
            # But let's assume if it starts with 1, 2, 3, 4 or 1), 2), 3), 4) it's an option.
            opt_match = re.match(r'^(\d+)\s*[\).]*\s*(.*)', line)
            if opt_match:
                current_question['options'].append(opt_match.group(2).strip())
            else:
                # Append to question text if no options yet
                if not current_question['options']:
                    current_question['text'] += " " + line
                else:
                    # Append to last option
                    current_question['options'][-1] += " " + line

if current_question:
    questions.append(current_question)

# Analyze
total = len(questions)
missing_options = [q for q in questions if len(q['options']) < 4]

print(f"Total questions found: {total}")
print(f"Questions with < 4 options: {len(missing_options)}")

for i, q in enumerate(missing_options[:20]):
    print(f"{i+1}. Q{q['id']}: {q['text'][:100]}... (Options: {len(q['options'])}, Correct: {q['correctIndex']})")
