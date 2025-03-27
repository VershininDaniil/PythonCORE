def fast_pow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:  # если степень четная
        temp = fast_pow(a, n // 2)
        return temp * temp
    else:  # если степень нечетная
        return a * fast_pow(a, n - 1)
        
    
a, n = map(int, input().split())

print(fast_pow(a, n))