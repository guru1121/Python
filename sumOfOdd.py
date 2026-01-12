x = range(1, 51)

def oddSum(nums):
     total = 0
     for num in x:
         if num %2 != 0:
             total += num
            #  print(num)
        
     return total
         
print(oddSum(x))
