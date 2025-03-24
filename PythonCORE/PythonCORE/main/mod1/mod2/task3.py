number_str = input().strip()

if number_str.isdigit() and int(number_str) > 0:
    number = int(number_str)

    binary = ""
    n = number
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2

    octal = ""
    n = number
    while n > 0:
        octal = str(n % 8) + octal
        n //= 8

    hex_digits = "0123456789ABCDEF"
    hex_number = ""
    n = number
    while n > 0:
        hex_number = hex_digits[n % 16] + hex_number
        n //= 16

    print(binary, octal, hex_number)
else:
    print("Неверное значение.")
    