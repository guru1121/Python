nums = [ 1, 2, 4, 5]

def missing_num(input_nums):
    n = len(nums)+1 
    print(n)
    expected_sum = n*(n+1) // 2
    print(expected_sum)
    actual_sum = sum(nums)
    print(actual_sum)
    
    missing = expected_sum - actual_sum
    return missing

print(missing_num(nums))