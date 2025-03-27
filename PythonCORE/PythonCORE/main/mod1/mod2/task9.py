phone = input().strip()
clean_phone = ''

for char in phone:
    if char in '0123456789+':
        clean_phone += char

print(clean_phone)