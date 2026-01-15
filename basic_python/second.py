# movies = []

# for i in range(5):
#     movie = input("Name of movie: ")
#     movies.append(movie)

# for movie in movies:
#     print(f"i watch {movie}")

# def greet(name):
#     print(f"Hello {name}")

# greet("guru")

# def add(a, b):
#     return a + b

# result = add(4, 6)

# print(result)

# def check_age(age):
#     if(age < 12):
#       return"you are kid"  
#     elif(age <= 18):
#        return "you are teenager"
#     else:
#         return("you are Adult")

# msg = check_age(10)

# print(msg)

# def describe_person(name, age):
#       print(f"My name is {name},I am {age} old")

# describe_person("guru", 25)

# total = 0
# for i in range(10, 0, -1):
#     print(i, end=" ")
#     total += i

# Print all numbers from 1 to 20

# for i in range(1, 21):
#     print(i)

# Print only even numbers from 1 to 20

# for i in range(1, 21):
#     if i%2 == 0:
#         print(i) 

# Print numbers from 10 down to 1

# for i in range(10, 0, -1):
#     print(i)

# Print the sum of all numbers from 1–50

# total = 0

# for i in range(1, 51):
#     total += i

# print(total)

# table of 2 

# for i in range(1, 11):
#     print(f"7 X {i} = ",7*i)

# def table(numb):
#     for i in range(1, 11):
#         res =  (numb*i)
#         print(res)

# table(6)

# rev = ""

# for ch in word:
#     rev = ch + rev
    
# print(rev)

# print(word[::-1])
# vowel = ["a", "e", "i", "o", "u"]


#word = input("Please enter your name :")
# count = 0

# for ch in word:
#     for i in vowel:
#         if ch == i:
#             count +=1

# print(count)

# check a if a word is palidrome 

# rev = word[::-1]

# if word == rev:
#     print("string is palindrome")
# else:
#     print("string is not palindrome")

# list = [3, 5, 8, 6, 2]

# max =  list[0]
# min = list[0]
# sum = 0
# for i in list:
#     if i > max:
#         max = i 
#     elif i < min:
#         min = i
#     sum += i
        
# print("Max number :", max)
# print("Min number :", min)
# print("sum of number :", sum)


fruits = []

# for i in range(5):
#  fruit = input("Enter fruit name :")
#  fruits.append(fruit)


# for fruit in fruits[::-1]:
#  print(fruit, end=", ")

# each no squared in list 

# numb = [1, 2, 3, 4, 5]

# for i in numb:
#     print (i*2, end=", ")

# number = int(input("Enter a number:"))

# if number > 0:
#     print("number is positive")
# elif number < 0:
#     print("number is negative")
# else:
#     print("number is zero") 

# number = int(input("enter a number :"))
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")

# for i in range(10,0, -1):
#     print(i)

# def add(a, b):
#     return a + b

# result = add(5, 4)

# print("result:", result)

# def greet(name):
#     print(f"hello {name} , Welcome to python")

# greet("guru")

# def find_avg(numbers):
#     total = sum(numbers)
#     count = len(numbers)
#     average = total/count
#     return average

# numb = [10, 20, 30, 40, 50]

# avg_numb = find_avg(numb)

# print(avg_numb)

# def grade_checker(value):
#     if value >= 90 and value <= 100 :
#         return "A"
#     elif value >= 75 and value <= 89:
#         return "B"
#     elif value >= 50 and value <= 74:
#         return "C"
#     elif value > 100:
#         return "invalid value"
#     else:
#         return "Fail"
    
# result = grade_checker(101)

# print(result)

#  sum of n numbers

# def sum_n(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#     return total

# res = sum_n(5)

# print(res)

# def factorial(f):
#     total= 1
#     for i in range(1, f+1):
#        total = total * i
#     return total

# res = factorial(5)

# print("factorial: ", res)

# def add(a:int , b:int) -> int:
#     return a + b

# print(add(5, 6))


# list operations

# def pfl(numb):
#     first = None
#     last = None
#     for i in numb:
#         if first is None:
#             first = i
#         last = i
#     return first, last
    


       
# number = [10, 30 , 15, 80]

# number.append(60)
# if 30 in number:
#     number.remove(30)

# print(number)

fruits = ["mango", "apple", "banana"]

fruits[1] = "papaya"

print(fruits.index("banana"))
        
        # tuples  its immutable
colors = ("red", "green", "blue", "yellow")

