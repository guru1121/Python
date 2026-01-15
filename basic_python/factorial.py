number = int(input("enter number: "))

def factorial(num):
    res = 1
    for i in range(1 , num+1):
        res = res * i
    return res 
print(factorial(number))

# By recursion 
def rec_factorial(num):
    if num == 0 or num == 1:
        return 1
    
    return num *rec_factorial(num-1)

print(rec_factorial(number))
