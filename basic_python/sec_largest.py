# Find the second largest element

nums = [1, 3, 2, 5, 7, 6, 8]

def sec_large(inp_nums):
    max = float('-inf')
    sec_max = float('-inf')
    
    for num in inp_nums:
        if num > max:
            sec_max = max
            max = num
        elif num > max and num != max:
            sec_max = num
    return sec_max

print(sec_large(nums))