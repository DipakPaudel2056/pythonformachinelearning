
def second_largest(arr):
    max = 0
    second_max = 0
    
    if(len(arr) < 2):
        return None
    for num in arr:
        if num > max:
            second_max = max
            max = num
        if max > num > second_max:
            second_max = num
    return second_max if second_max > 0 else None

print(second_largest([23,543,234,2345,12]))