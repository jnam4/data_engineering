#Chapter10 : File
#2025.01.03
#Jiyun Nam
#@codecademy

# 1. File
# each file is an individual container of related information. 

# with open('real_cool_document.txt') as cool_doc:
#   cool_contents = cool_doc.read()
# print(cool_contents)

import os

print("Current Working Directory:", os.getcwd())
print("Files in Current Directory:", os.listdir())

print("Does 'welcome.txt' exist?", os.path.exists('welcome.txt'))

file_path = "/Users/jnam4/data_engineering/codeacademy/Data Engineering/Python/10. File /welcome.txt"
with open('how_many_lines.txt') as text_file:
    text_data = text_file.read()
print(text_data)


# 2. Iterating Through Lines
# store each line in a variable 
with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)