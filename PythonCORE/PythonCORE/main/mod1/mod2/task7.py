s, i = input().strip().split(',')

count = 0
position = 0

while position < len(s):
    if s[position] == i:
        count += 1
        position += 1
    else:
        break

print(count)