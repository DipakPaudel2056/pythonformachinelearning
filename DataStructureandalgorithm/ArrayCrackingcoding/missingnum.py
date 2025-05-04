# You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.

# Examples:

# Input: arr[] = [1, 2, 3, 5]
# Output: 4

def missingNum( arr):
        if len(arr) == 1:
            if arr[0] == 1:
                return 2
            else:
                return 1
        arr.sort()
        check = [x for x in range(1, arr[-1] + 1)]
        res = sum(check) - sum(arr)
        if res == 0:
            return arr[-1] + 1
        return res