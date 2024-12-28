#Project:   Gradebook
#Date:      2024.12.27
#Creator:   Jiyun Nam

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

#Your code below: 
subjects=["physics", "calculus", "poetry", "history"]
grades=[98, 97, 85, 88]
#2D in manually
gradebook=[["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)

#Add more subject
gradebook.append(["Computer Science", 100])
gradebook.append(["visual arts", 93])
print(gradebook)
#Modifying extra 5 more points on visual arts
gradebook[5][1]+=5
print(gradebook)
#Pass/Fail option for poetry
gradebook[2].remove(85)
gradebook[2].append("Pass")
print(gradebook)

#One Big Gradebook
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)


