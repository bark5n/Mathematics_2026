import glob

for section in ['02_determinants', '03_matrix_inversion', '04_systems_of_equations']:
    files = glob.glob(f'solutions/1_Algebra/{section}/*.md')
    for f in sorted(files):
        with open(f, 'r', encoding='utf-8') as fp:
            lines = fp.readlines()
        
        # count occurrences of $$
        num_display = sum(1 for line in lines if line.strip() == '$$')
        if num_display % 2 != 0:
            print(f"ODD DISPLAY BLOCKS ({num_display}): {f}")
        else:
            # check pairs
            in_disp = False
            for idx, line in enumerate(lines):
                if line.strip() == '$$':
                    in_disp = not in_disp
            if in_disp:
                print(f"FAILED PARITY IN {f}")

print("Check finished.")

