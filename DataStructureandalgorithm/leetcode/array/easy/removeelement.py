# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

# my approach to this question is very simple
# go from the back if found a val pop it if not found then loop ahead
# and at last return the length of the remaining items

def removeelement(nums,val):
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == val:
            nums.pop(i)
    
    return (nums,len(nums))
# second approach for this problem is using two pointer
def remove_val(nums,val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return (nums[:k],k)
        
print(remove_val([1,2,3,2,2,2,3],2))