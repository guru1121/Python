marks = [10, 20, 30, 25, 40]

# newList = []
    
# for num  in marks:
#     num = num +2
#     newList.append(num)
    
# print(newList)

newMarks = [num+2 for num in marks]
print(newMarks)


cubes = [num**3 for num in range(10) if num%2 == 0  ]
print(cubes)
