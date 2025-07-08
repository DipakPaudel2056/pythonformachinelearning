import pandas as pd
from students import students
# we can do the splitting of the columns using the normal python splitting
print(students.columns)
students['gender'] = students.gender_age.str[:1]
students['age']=students.gender_age.str[1:]
print(students.head())
print(students[['full_name','gender','age','score','exam']])