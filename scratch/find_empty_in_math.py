import glob

files = glob.glob('solutions/1_Algebra/02_determinants/*.md') + \
        glob.glob('solutions/1_Algebra/03_matrix_inversion/*.md') + \
        glob.glob('solutions/1_Algebra/04_systems_of_equations/*.md')

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    in_disp = False
    for i, line in enumerate(lines):
        if line.strip() == '$$':
            if not in_disp:
                in_disp = True
                if i+1 < len(lines) and lines[i+1].strip() == '':
                    print(f"{f}:{i+1} has blank line after opening $$")
            else:
                in_disp = False
                if i-1 >= 0 and lines[i-1].strip() == '':
                    print(f"{f}:{i+1} has blank line before closing $$")

