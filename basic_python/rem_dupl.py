nums = [1, 3, 3, 2, 5, 5, 7, 6, 8]

def rem_dupl(inp_nums):
    # below commented code in not for interview
    # updated_list = list(set(inp_nums))
    # return updated_list
    uniq_list = []
    
    # this is interview friendly
    for num in inp_nums:
        if num not in uniq_list:
            uniq_list.append(num)
            
    return uniq_list
    
 
print(rem_dupl(nums))