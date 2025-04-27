# this is just the data type that we donot use frequently, the use and accessing is pretty similar to that of list 
first_tuple = ('dipak',25,"Programmer")
print(first_tuple)

# to access the tuple same as list we can access using
firstitem = first_tuple[0]
seconditem = first_tuple[1]
thirditem = first_tuple[2]


# one cool thing about tuple is the data here are immutable
# we cannot change the data once they are created
# and to unwrap the tupel we use the syntax same as the array destructuring

# we store data that are meant to be grouped together 
name , age, profession = first_tuple
print(name, age, profession)