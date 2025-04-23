# working with the text file in python is made simple using the with function
# here is the simple syntax to read the file

with open('file/introfile.txt') as intro_file:
    intro_file_content = intro_file.read()
    print(intro_file)
    
     
    
# here we have seen how to import the file and make it available to read
# now lets see how to read the lines separately

with open('file/introfile.txt') as intro_file:
    for line in intro_file.readlines():
        print(line)
        
        
        
# writing into the file can also been done with the open method, here we pass the argument 'w'
with open('file/introfile.txt','w') as writing_file:
    writing_file.write('hello this is written first')
    
# to append new value at the end of the string we can pass the new parameter 'a' 
with open('file/introfile.txt','a') as appending_file:
    appending_file.write("\n  this is added at the end")