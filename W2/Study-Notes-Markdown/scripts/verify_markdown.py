import re
import os

notes_file = "W2/Study-Notes-Markdown/Study-Notes.md"
answers_file = "W2/Study-Notes-Markdown/Answers-and-Practice.md"

def check_file(filepath):
    print(f"Checking {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Check for unclosed math delimiters
    # Double $$ checks
    double_dollars = content.count("$$")
    if double_dollars % 2 != 0:
        print(f"  WARNING: Odd number of $$ ({double_dollars}) in {filepath}")
    else:
        print(f"  $$ delimiters balanced: {double_dollars // 2} pairs.")

    # Check image paths
    img_matches = re.findall(r'!\[.*?\]\((.*?)\)', content)
    for img in img_matches:
        img_path = os.path.join(os.path.dirname(filepath), img)
        if not os.path.exists(img_path):
            print(f"  ERROR: Image not found: {img_path}")
        else:
            print(f"  Image OK: {img}")

    # Check relative file links
    link_matches = re.findall(r'\[.*?\]\((.*?\.md.*?)\)', content)
    for link in link_matches:
        parts = link.split("#")
        target_file = parts[0]
        if target_file:
            target_path = os.path.join(os.path.dirname(filepath), target_file)
            if not os.path.exists(target_path):
                print(f"  ERROR: Linked file not found: {target_path}")
            else:
                print(f"  Link file target OK: {link}")

check_file(notes_file)
check_file(answers_file)

# Check exercise count in Answers-and-Practice.md
with open(answers_file, "r", encoding="utf-8") as f:
    text = f.read()

mmsa_expected = ["31", "33", "34", "35", "37", "38", "39", "40", "43", "44", "45", "47"]
par_expected = ["16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "29", "41", "49"]

print("\nVerifying MMSA exercises:")
for ex in mmsa_expected:
    if f"Exercise {ex}" in text:
        print(f"  MMSA #{ex} found.")
    else:
        print(f"  ERROR: MMSA #{ex} MISSING!")

print("\nVerifying PAR exercises:")
for ex in par_expected:
    if f"Exercise {ex}" in text:
        print(f"  PAR #{ex} found.")
    else:
        print(f"  ERROR: PAR #{ex} MISSING!")

print("\nVerifying Problem Types:")
for i in range(1, 10):
    pt = f"PT-0{i}"
    if pt in text:
        print(f"  {pt} found in Answers-and-Practice.md")
    else:
        print(f"  ERROR: {pt} MISSING in Answers-and-Practice.md")
