num1 = int(input("enter num 1 :"))
num2 = int(input("enter num 2 :"))


while num2 !=0:
    num1, num2 = num2 , num1%num2

print(num1)

