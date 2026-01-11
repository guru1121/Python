name = "Gurunand"
age = 24
height =  5.6

print(f"my name is {name}, I am {age} yrs old and {height} ft tall ")


fruits = ["apple" , "banana", "pineapple", "Kiwi"]
fruits.append("orange")

for item in fruits:
   # print(item)
    print(f"i like {item.lower()}")


age = int(input("Enter your age: "))
if age < 12:
    print("your are kid")
elif age <= 18:
    print("You are teenager")
else :
    print("you are an adult")


