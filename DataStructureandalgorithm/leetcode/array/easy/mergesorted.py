# # you are given two sorted arrays nums1 and nums2 and the value m and n and the length of nums1 is m+n 
# #your task is to create and array nums1 with m elements from the n elements from nums2
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.


# my naive approach is to add all the elements from nums2 at the back of the nums1 and sort them
def mergesorted(nums1,nums2,m,n):
    # loop through nums2 and populate end of nums1 with those value
    for i in range(n):
        nums1[m+i] = nums2[i]
    nums1.sort()
    
    
# second approach is to use two pointer 
def mergesorttwopointer(nums1,nums2,m,n):
    i = m -1
    j = n - 1
    k = m + n -1
    
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
        