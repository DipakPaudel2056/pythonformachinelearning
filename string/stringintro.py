# all the python string are the list and the operation we can do with the list can be done with the string,
# i have read uderstood and completed all the small coding lesson 

def username_generator(first_name,last_name): #creating username_generator function with first_name and last_name
  if len(first_name) >=3 and len(last_name) >=3:
    user_name = first_name[:3]+last_name[:4] #if the first_name and last_name length is greater than 3 than we add the 3 first letters from both of them otherwise we just add the whole name
  else:
    user_name = first_name + last_name

  return user_name


def password_generator(user_name):
  password = ''
  password = user_name[-1]+user_name[:-1] #created a password with the last letter coming to the front
  return password
