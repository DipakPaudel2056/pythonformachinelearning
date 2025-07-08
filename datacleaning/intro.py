# here we are learning pandas glob function which is helpful to open multiple files using shell-style wildcard matching
import pandas as pd
import glob

student_files = glob.glob("exam*.csv")
df_list = []
for file in student_files:
  data = pd.read_csv(file)
  df_list.append(data)
students = pd.concat(df_list)
print(students.head)
print(len(students))