import json
import random
import re
import sys

# Ensure UTF-8 output if possible
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def parse_block1(text):
    questions = []
    lines = text.strip().split('\n')
    parsed_count = 0
    fail_count = 0
    for line in lines:
        if not line.strip(): continue
        if not re.match(r'^Q\d+', line): continue
        
        parts = line.split('\t')
        if len(parts) >= 4:
            q_text = parts[1].strip()
            options_str = parts[2].strip()
            correct_text = parts[3].strip()
        else:
            match = re.match(r'^Q\d+/?Q?\d*\s+(.+?)\s{2,}(.+?)\s{2,}(.+)$', line)
            if match:
                q_text = match.group(1).strip()
                options_str = match.group(2).strip()
                correct_text = match.group(3).strip()
            else:
                fail_count += 1
                continue

        options = [o.strip() for o in options_str.split(';')]
        if not options:
            fail_count += 1
            continue
            
        correct_index = -1
        # Try exact match
        for i, opt in enumerate(options):
            if opt == correct_text:
                correct_index = i
                break
        
        # Try cleaning artifact digits
        if correct_index == -1:
            clean_correct = re.sub(r'\d+$', '', correct_text).strip()
            for i, opt in enumerate(options):
                if opt == clean_correct:
                    correct_index = i
                    break
        
        # Try substring
        if correct_index == -1:
            for i, opt in enumerate(options):
                if opt in correct_text or correct_text in opt:
                    correct_index = i
                    break

        if correct_index == -1:
            # print(f"DEBUG: Failed to find answer index for line: {line[:50]}")
            fail_count += 1
            continue

        questions.append({
            "questionText": q_text,
            "options": options,
            "correctAnswerIndex": correct_index,
            "hasDetectedAnswer": False
        })
        parsed_count += 1
    
    print(f"Block 1: Parsed {parsed_count}, Failed {fail_count}")
    return questions

def parse_block2(text):
    questions = []
    segments = re.split(r'\*\*Q\d+\*\*', text)
    parsed_count = 0
    for segment in segments:
        if not segment.strip(): continue
        lines = segment.strip().split('\n')
        q_text = lines[0].strip()
        options = []
        correct_index = -1
        for line in lines[1:]:
            line = line.strip()
            if re.match(r'^[A-D]\.', line):
                options.append(line[2:].strip())
            elif "Answer:" in line:
                ans_char = re.search(r'Answer:\s*([A-D])', line)
                if ans_char:
                    correct_index = ord(ans_char.group(1)) - ord('A')
        if q_text and len(options) >= 2 and correct_index != -1:
            questions.append({
                "questionText": q_text,
                "options": options,
                "correctAnswerIndex": correct_index,
                "hasDetectedAnswer": False
            })
            parsed_count += 1
    print(f"Block 2: Parsed {parsed_count}")
    return questions

with open('scratch/raw_questions.txt', 'r', encoding='utf-8') as f:
    raw_content = f.read()

parts = raw_content.split('###NEW_QUESTIONS###')
block1_text = parts[0]
block2_text = parts[1] if len(parts) > 1 else ""

new_questions = parse_block1(block1_text)
new_questions += parse_block2(block2_text)

random.shuffle(new_questions)
for i, q in enumerate(new_questions):
    q["id"] = f"fligh-plan-{i+1}"

with open('src/data/questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

found = False
for subject in data['subjects']:
    if subject['id'] == 'fligh-plan':
        subject['questions'] = new_questions
        found = True
        break

if found:
    with open('src/data/questions.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Successfully updated fligh-plan with {len(new_questions)} total questions.")
else:
    print("Error: Could not find fligh-plan subject.")
