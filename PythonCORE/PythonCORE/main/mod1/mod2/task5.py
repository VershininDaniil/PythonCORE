domain = input().strip()
dot_positions = []
for i in range(len(domain)):
    if domain[i] == '.':
        dot_positions.append(i)

parts = []
start = 0
for pos in dot_positions:
    part = ''
    for i in range(start, pos):
        part += domain[i]
    parts.append(part)
    start = pos + 1
last_part = ''
for i in range(start, len(domain)):
    last_part += domain[i]
parts.append(last_part)

for i in range(len(parts)-1, -1, -1):
    print(parts[i])