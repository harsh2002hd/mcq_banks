import json
import re

def parse_v12(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [l.strip() for l in f.readlines()]

    questions = []
    correct_indices = [i for i, l in enumerate(lines) if '(Correct)' in l or '(correct)' in l]
    
    last_end = 0
    
    for idx in correct_indices:
        if idx < last_end: continue
        
        # 1. Identify options block
        # Look up from idx for consecutive option-like lines
        opt_start = idx
        for k in range(1, 12):
            prev_i = idx - k
            if prev_i < last_end: break
            l = lines[prev_i]
            if not l: 
                opt_start = prev_i + 1
                break
            
            # If it's a header, it's NOT an option
            if re.match(r'^(?:N\s*\d+|Question|Q\s*\d+|\[|\d+\s*/\s*\d+|\*\*Q)', l):
                break
            
            # If it looks like an option
            if re.match(r'^[A-D]\.\s*', l) or re.match(r'^[1-4]\)\s*', l) or len(l) < 150:
                opt_start = prev_i
            else:
                break
                
        # 2. Identify question text
        # Everything from last_end to opt_start - 1
        q_text_parts = []
        for i in range(last_end, opt_start):
            l = lines[i]
            if not l: continue
            
            # Strip headers but keep the rest of the line
            l_clean = re.sub(r'^(?:N\s*\d+\s*:?|Question\s*(?:\d+)?\s*\(?N?\s*\d*\)?\s*:?|Q\s*\d+\s*/\s*\d+|\[.*\]|\d+\s*/\s*\d+|\*\*Q\d+\*\*)\s*', '', l)
            if l_clean:
                q_text_parts.append(l_clean)
            elif l:
                # If the line was JUST a header, maybe the header itself is the question?
                # Usually no, but let's keep it if we have nothing else.
                pass
        
        q_text = " ".join(q_text_parts).strip()
        
        # 3. Identify options
        opt_end = idx
        for k in range(1, 6):
            next_i = idx + k
            if next_i >= len(lines): break
            # Stop if we hit next question's correct answer
            if any(next_i == nxt for nxt in correct_indices if nxt > idx): break
            l = lines[next_i]
            if not l: break
            if re.match(r'^(?:N\s*\d+|Question|Q\s*\d+|\[|\d+\s*/\s*\d+|\*\*Q)', l): break
            if len(l) > 200: break
            opt_end = next_i
            
        raw_options = [lines[i] for i in range(opt_start, opt_end + 1) if lines[i]]
        options = []
        c_idx_final = -1
        for opt in raw_options:
            is_c = '(Correct)' in opt or '(correct)' in opt
            clean_opt = opt.replace('(Correct)', '').replace('(correct)', '').strip()
            clean_opt = re.sub(r'^[A-D]\.\s*', '', clean_opt)
            clean_opt = re.sub(r'^[1-4]\)\s*', '', clean_opt)
            if clean_opt:
                options.append(clean_opt)
                if is_c:
                    c_idx_final = len(options) - 1
        
        # 4. Final check
        # If q_text is still empty, maybe use the last line of the previous question block?
        # No, that's wrong. Let's just be more aggressive.
        if not q_text and opt_start > 0:
            # Maybe the header IS the question text
            q_text = lines[opt_start - 1]
            q_text = re.sub(r'^(?:N\s*\d+\s*:?|Question\s*(?:\d+)?\s*\(?N?\s*\d*\)?\s*:?|Q\s*\d+\s*/\s*\d+|\[.*\]|\d+\s*/\s*\d+|\*\*Q\d+\*\*)\s*', '', q_text)
            if not q_text: q_text = lines[opt_start - 1] # Take header as is

        if q_text and len(options) >= 2 and c_idx_final != -1:
            questions.append({
                "questionText": q_text,
                "options": options,
                "correctAnswerIndex": c_idx_final,
                "hasDetectedAnswer": False
            })
            last_end = opt_end + 1
        else:
            last_end = idx + 1
            
    return questions

new_questions = parse_v12('scratch/docx_content.txt')
print(f"Parsed {len(new_questions)} questions.")

# Update questions.json
with open('src/data/questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for subject in data['subjects']:
    if subject['id'] == 'agk-pdf':
        for i, q in enumerate(new_questions):
            q['id'] = f"agk-pdf-{i+1}"
        subject['questions'] = new_questions
        break

with open('src/data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)
print("Updated questions.json")
