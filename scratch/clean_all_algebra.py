import glob
import re

def expand_matrix(mat_match):
    """Expands a single-line pmatrix into multi-line pmatrix as required by hints.md."""
    inner = mat_match.group(1).strip()
    rows = [r.strip() for r in inner.split(r'\\') if r.strip()]
    res = ["\\begin{pmatrix}"]
    for r in rows:
        res.append(f"{r} \\\\")
    res.append("\\end{pmatrix}")
    return "\n".join(res)

def clean_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Normalize line breaks
    text = text.replace('\r\n', '\n')
    
    # 2. Fix single-line pmatrix: \begin{pmatrix} ... \end{pmatrix}
    # Pattern: \begin{pmatrix}(.*?)\end{pmatrix} where it is all on one line or compressed
    def replace_pmatrix(match):
        content = match.group(1)
        # split by \\
        raw_rows = content.split(r'\\')
        rows = [r.strip() for r in raw_rows if r.strip()]
        out = ["\\begin{pmatrix}"]
        for r in rows:
            out.append(f"{r} \\\\")
        out.append("\\end{pmatrix}")
        return "\n".join(out)
    
    # Replace single line pmatrix
    text = re.sub(r'\\begin\{pmatrix\}(.*?)\\end\{pmatrix\}', replace_pmatrix, text)

    lines = text.split('\n')
    new_lines = []
    
    in_display = False
    for i, line in enumerate(lines):
        s = line.strip()
        
        # Check if line is $$
        if s == '$$':
            if not in_display:
                # opening $$
                # ensure previous line is empty
                if new_lines and new_lines[-1].strip() != '':
                    new_lines.append('')
                new_lines.append('$$')
                in_display = True
            else:
                # closing $$
                # remove any trailing empty lines inside display
                while new_lines and new_lines[-1].strip() == '' and new_lines[-1] != '$$':
                    new_lines.pop()
                new_lines.append('$$')
                in_display = False
                # ensure next line will have empty line if not already
        else:
            if in_display:
                # Inside display: do NOT add empty lines!
                if s == '':
                    continue
                # Also check bare operator
                if s in ('=', '+', '-'):
                    continue
                new_lines.append(line)
            else:
                new_lines.append(line)

    # Now clean up consecutive empty lines outside display
    res = []
    in_disp = False
    for i, l in enumerate(new_lines):
        s = l.strip()
        if s == '$$':
            if not in_disp:
                # opening
                if res and res[-1].strip() != '':
                    res.append('')
                res.append('$$')
                in_disp = True
            else:
                # closing
                res.append('$$')
                in_disp = False
                if i + 1 < len(new_lines) and new_lines[i+1].strip() != '':
                    res.append('')
        else:
            if s == '':
                if res and res[-1].strip() == '':
                    continue
            res.append(l)

    # Ensure single trailing newline
    final_text = '\n'.join(res).strip() + '\n'
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(final_text)

sections = ['02_determinants', '03_matrix_inversion', '04_systems_of_equations']
for sec in sections:
    for f in sorted(glob.glob(f'solutions/1_Algebra/{sec}/*.md')):
        clean_file(f)

print("All 45 files cleaned!")

