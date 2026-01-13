text = input("enter text:").lower()

vowel = "aeiou"

count = 0

for i in text:
    if i in vowel:
        count = count +1
        
print( count)
