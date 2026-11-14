import os
import re

study_notes_path = "/Users/stevenli/Documents/University of toronto/STA237/W3/Study-Notes-Markdown/Study-Notes.md"
answers_path = "/Users/stevenli/Documents/University of toronto/STA237/W3/Study-Notes-Markdown/Answers-and-Practice.md"

def verify_file(filepath):
    print(f"\n================ Verifying {os.path.basename(filepath)} ================")
    if not os.path.exists(filepath):
        print(f"ERROR: File {filepath} does not exist!")
        return False
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    lines = content.splitlines()
    print(f"Total lines: {len(lines)}")
    print(f"Total characters: {len(content)}")
    
    # Check LaTeX math delimiter balance
    # Count $$
    dd_matches = re.findall(r'\$\$', content)
    if len(dd_matches) % 2 != 0:
        print(f"WARNING: Odd number of '$$' delimiters: {len(dd_matches)}")
    else:
        print(f"LaTeX $$ display math delimiters balanced ({len(dd_matches)} occurrences = {len(dd_matches)//2} blocks).")
        
    # Check image links
    img_matches = re.findall(r'!\[.*?\]\((.*?)\)', content)
    print(f"Found {len(img_matches)} image references:")
    for img in img_matches:
        img_full = os.path.normpath(os.path.join(os.path.dirname(filepath), img))
        exists = os.path.exists(img_full)
        print(f"  - {img} -> Exists? {exists} ({img_full})")
        
    return True

verify_file(study_notes_path)
verify_file(answers_path)

# Check Answers-and-Practice specific sections
with open(answers_path, "r", encoding="utf-8") as f:
    ans_content = f.read()

sections = ["## Section A: Solutions to Concept Teaching Examples",
            "## Section B: Source / Lecture Slide Question Solutions",
            "## Section C: Solutions to Requested Textbook Exercises",
            "### C.1 MMSA Exercises",
            "### C.2 PAR Exercises",
            "## Section D: Original Self-Test Questions",
            "## Section E: Solutions to Self-Test Questions",
            "## Section F: Coverage & Unresolved-Items Appendix"]

print("\n================ Section Presence Check ================")
for s in sections:
    present = s in ans_content
    print(f"  [{'OK' if present else 'FAIL'}] {s}")

# Check PT coverage in Study Notes
with open(study_notes_path, "r", encoding="utf-8") as f:
    sn_content = f.read()

print("\n================ Study Notes PT Check ================")
for i in range(1, 11):
    pt_tag = f"PT-{i:02d}"
    present = pt_tag in sn_content
    print(f"  [{'OK' if present else 'FAIL'}] {pt_tag} in Study-Notes.md")

print("\n================ Answers-and-Practice PT Check in Section A ================")
for i in range(1, 11):
    pt_sol = f"Teaching Example PT-{i:02d}"
    present = pt_sol in ans_content
    print(f"  [{'OK' if present else 'FAIL'}] {pt_sol} in Answers-and-Practice.md")

print("\n================ Self-Test Check ================")
for i in range(1, 11):
    st_q = f"Question ST-{i:02d}"
    st_a = f"Solution ST-{i:02d}"
    q_present = st_q in ans_content
    a_present = st_a in ans_content
    print(f"  [{'OK' if q_present else 'FAIL'}] {st_q} | [{'OK' if a_present else 'FAIL'}] {st_a}")

# Check MMSA & PAR exercises
print("\n================ Selected Textbook Exercise Check ================")
sample_exercises = [
    "Exercise 2.4-1", "Exercise 2.4-11", "Exercise 2.4-19",
    "Exercise 2.5-1", "Exercise 2.5-9", "Exercise 2.5-15", "Exercise 2.5-21",
    "Exercise 3.1-1", "Exercise 3.1-7", "Exercise 3.1-15",
    "Exercise 2.1", "Exercise 2.7", "Exercise 2.14", "Exercise 2.17", "Exercise 2.22",
    "Exercise 2.26", "Exercise 2.29", "Exercise 2.33", "Exercise 2.32", "Exercise 2.36",
    "Exercise 3.1", "Exercise 3.2", "Exercise 3.5", "Exercise 3.6", "Exercise 3.7"
]
for ex in sample_exercises:
    present = ex in ans_content
    print(f"  [{'OK' if present else 'FAIL'}] {ex}")
