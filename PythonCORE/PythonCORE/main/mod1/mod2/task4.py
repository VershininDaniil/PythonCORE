def is_natural(num_str):
    if len(num_str) == 0:
        return False
    for ch in num_str:
        if not ('0' <= ch <= '9'):
            return False
    return num_str != '0'

def decimal_to_base(num, base):
    if num == 0:
        return '0'
    digits = []
    while num > 0:
        remainder = num % base
        if remainder < 10:
            digits.append(str(remainder))
        else:
            # For hexadecimal (base 16)
            digits.append(chr(ord('A') + remainder - 10))
        num = num // base
    return ''.join(reversed(digits))

input_str = input().strip()

if not is_natural(input_str):
    print("Неверный ввод")
else:
    num = int(input_str)
    binary = decimal_to_base(num, 2)
    octal = decimal_to_base(num, 8)
    hexa = decimal_to_base(num, 16)
    print(f"{binary}, {octal}, {hexa}")
