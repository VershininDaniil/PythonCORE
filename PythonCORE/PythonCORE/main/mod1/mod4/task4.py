def make_palindrome(s):
    
    letter_counts = {}
    for letter in s:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    
    odd_count = 0
    middle_letter = ''
    for letter, count in letter_counts.items():
        if count % 2 != 0:
            odd_count += 1
            middle_letter = letter
            if odd_count > 1:
                return "Нельзя составить палиндром"

    half = ''
    for letter, count in sorted(letter_counts.items()):
        half += letter * (count // 2)
    
    palindrome = half + middle_letter + half[::-1]
    return palindrome


word = input().strip()


result = make_palindrome(word)
print(result)