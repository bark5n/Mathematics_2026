import glob
import re

files = glob.glob('solutions/1_Algebra/02_determinants/*.md') + \
        glob.glob('solutions/1_Algebra/03_matrix_inversion/*.md') + \
        glob.glob('solutions/1_Algebra/04_systems_of_equations/*.md')

for f in sorted(files):
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    
    for i, line in enumerate(lines):
        # Check if \begin{pmatrix} and \end{pmatrix} are on the same line
        if r'\begin{pmatrix}' in line and r'\end{pmatrix}' in line:
            print(f"{f}:{i+1} single line pmatrix: {line.strip()}")
        # Check if \begin{pmatrix} has entries on the same line
        elif r'\begin{pmatrix}' in line:
            after = line.split(r'\begin{pmatrix}')[1].strip()
            if after and after != r'\\':
                print(f"{f}:{i+1} entries on same line as \\begin{{pmatrix}}: {line.strip()}")
        # Check if \end{pmatrix} has entries before it on the same line
        elif r'\end{pmatrix}' in line:
            before = line.split(r'\end{pmatrix}')[0].strip()
            if before:
                print(f"{f}:{i+1} entries before \\end{{pmatrix}}: {line.strip()}")

