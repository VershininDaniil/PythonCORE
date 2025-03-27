input_str = input()
space1 = 0
space2 = 0
for i in range(len(input_str)):
    if input_str[i] == ' ':
        if space1 == 0:
            space1 = i
        else:
            space2 = i
            break
num1 = ''
for j in range(0, space1):
    num1 += input_str[j]
num1 = int(num1)
num2 = ''
for k in range(space1 + 1, space2):
    num2 += input_str[k]
num2 = int(num2)
num3 = ''
for l in range(space2 + 1, len(input_str)):
    num3 += input_str[l]
num3 = int(num3)
case1 = num1 <= num2 and num2 <= num3
case2 = num1 <= num3 and num3 <= num2
case3 = num2 <= num1 and num1 <= num3
case4 = num2 <= num3 and num3 <= num1
case5 = num3 <= num1 and num1 <= num2
case6 = num3 <= num2 and num2 <= num1
middle = 0
if case1:
    middle = num2
elif case2:
    middle = num3
elif case3:
    middle = num1
elif case4:
    middle = num3
elif case5:
    middle = num1
elif case6:
    middle = num2
print(middle)