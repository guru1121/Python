# Find frequency of elements

nums = [2, 2, 3, 5, 1, 5, 5, 6, 6 ]

def freq(inp_num):
    freq_num = {}
    for num in inp_num:
        
        if num in freq_num:
            freq_num[num] += 1
        else:
            freq_num[num] = 1
            
    return(freq_num)

print(freq(nums))
            
            