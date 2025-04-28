# fibonacci number are the number sequece which starts with 1 , 1 and the second number is the sum of previous 2 number
# that means this sequence 1 , 1, 2,3,5,8,13 ...

# that means the next number is the sum of n -1 and n -2 item in the list
# lets write the solution recursively, the escape here is if the n is 1 or n is 2 it must be 1

def fib(n) :
    if (n == 1) or (n == 2) :
        return 1
    else:
     return fib(n - 1)  + fib (n -2)
 
print(fib(200))