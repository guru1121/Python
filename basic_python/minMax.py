nums =[ 1, 5, 7, 4, 3, 8]

def findMinMax(numb):
    min, max = numb[0], numb[0]
    
    for i in numb:
        if i > max:
            max = i 
            
        elif i < min:
            min = i
            
    return(max, min) 

print(findMinMax(nums))