text = input("Enter your text: ")

vowels = ""

if "a" in text:
    vowels += "a"
if "e" in text:
    vowels += "e"
if "i" in text:
    vowels += "i"
if "o" in text:
    vowels += "o"
if "u" in text:
    vowels += "u"
    
print("Vowels :" ,vowels)

# time complexity of this program is O(n)
# Because for each vowel it runs n times 
