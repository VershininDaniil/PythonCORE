def check_numbers(numbers_str):
    numbers = numbers_str.split()
    all_same = True
    first_num = numbers[0]
    for num in numbers:
        if num != first_num:
            all_same = False
            break
    all_different = True
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                all_different = False
                break
        if not all_different:
            break

    if all_same:
        print("Все числа равны")
    elif all_different:
        print("Все числа разные")
    else:
        print("Есть равные и неравные числа")
