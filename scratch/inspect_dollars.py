with open('solutions/1_Algebra/02_determinants/problem_03_solution.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if l.strip() == '$$':
        print(f"Line {i+1}: {repr(l)}")

