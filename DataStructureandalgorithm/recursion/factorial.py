# what is factorial?
# if we multiply the numbers inculding the given number untill we reach to 1, itt is factorial of that number
# for example; 4! = 4 * 3* 2* 1

def factorial(n):
    if n >= 1:
        return n * factorial(n-1)
    else:
        return 1
    
print(factorial(4)) #should return 24
print(factorial(12)) #should return 479001600