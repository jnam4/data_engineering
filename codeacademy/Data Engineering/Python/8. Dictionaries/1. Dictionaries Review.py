#Chapter8 : Dictionaries Review
#2025.01.02
#Jiyun Nam
#@codecademy

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# 1. Dict comprehension 
p = zip(songs,playcounts)
plays = {key:value for key, value in p}

# 2. Add new entry 
plays["Purple Haze"] = 1

# 3. Update dictionary 
plays["Respect"] = 94
print(plays)

# 4. Create dictionary -> Use {}
#  In the case of the invalid dictionary, using lists as keys results in a TypeError 
library = {"The Best Songs": plays, "Sunday Feelings": {}} 
print(library)