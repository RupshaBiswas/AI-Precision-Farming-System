#!/usr/bin/env python
# Fix indentation in app_test.py

with open('app_test.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Fix the indentation from line 1836 onwards (0-indexed: 1835 onwards)
for i in range(1835, min(1880, len(lines))):
    line = lines[i]
    # Add 4 spaces to align with the else block structure
    if (line.startswith('    #') or line.startswith('    if ') or 
        line.startswith('    st.') or line.startswith('    login') or 
        line.startswith('    with ')):
        lines[i] = '    ' + line

with open('app_test.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('✓ Indentation fixed')
