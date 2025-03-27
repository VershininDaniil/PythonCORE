words = input().split()  
new_word = ""  
for word in words:   
    if len(word) > 0:      
        last_letter = word[-1]
        new_word += last_letter
print(new_word)