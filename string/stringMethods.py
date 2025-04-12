# #Formatting method
# there are 3 methods to change the format of the string in python:
# lower() --> to lowercase the string
# upper() --> to uppercase the string
# title() --> return the string in the title case


# # main thing to rememeber is the strings are immutable

# split() --> this method return the list of the strings based of the argument, if we donot provide any argument it will split the string based on the spaces
line_one = "The sky has given over"
line_one_words = line_one.split() #["The","sky","has","given","over"]


# the challenge is to split the string into the name of the authors and print only the last name
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
author_last_names = []
for author_name in author_names:
  author_last_names.append(author_name.split()[1])

print(author_last_names)



# we can also split the string based on the escape characters of python like \n for new line and \t for new tab

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split("\n")
print(spring_storm_lines)


# join method
# it is little weird although it is string method we pass the list as an argument and the string we want to join with as a string where we are applying that join method

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = "\n".join(winter_trees_lines) #we are joining the string with the new_line
print(winter_trees_full)


# strip() --> it removes the white spaces from front and the back of the strings
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    '] #got the messy string
love_maybe_lines_stripped = [] #initiated empty list to store the cute strings
for char in love_maybe_lines:
  strippedchar= char.strip()
  love_maybe_lines_stripped.append(strippedchar)

love_maybe_full = "\n".join(love_maybe_lines_stripped) #joined them together with the new line
print(love_maybe_full)


#replace
#this string method is used to replace the part of the string with another string
#the syntax looks like this
# string_name.replace(substring_being_replaced, new_substring)

toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace("Tomer","Toomer")
print(toomer_bio_fixed)



#find 
# this method returns the first index value of given string
god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find('disown')


#format
#this method is used when we want to uset the variables in the string format we use the variables in the place of {} and we can use as much as we like
def poem_title_card(title,poet):
  formatted_statement =  "The poem \"{}\" is written by {}.".format(title,poet)
  return formatted_statement

print(poem_title_card("I Hear America Singing","Walt Whitman"))

# this is the second implementation where we can pass the arguments in this way too
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

my_beard_description = poem_description(author = "Shel Silverstein",
title = "My Beard",
original_work = "Where the Sidewalk Ends",
publishing_date = "1974"
)
print(my_beard_description)