#Chapter9 : String Method
#2025.01.02
#Jiyun Nam
#@codecademy

# 1. Formatting Methods 
# .lower() : returns string with all lowercase characters 
# .upper() :
# .title() : returns string with first letter of capitalized 

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
poem_author_fixed = poem_author.upper()
print(poem_title_fixed)
print(poem_author_fixed)



# 2. Splitting Strings - Part 1
# .split() : returns substrings found between the given argument 

line_one = "The sky has given over"
line_one_words = line_one.split()
print(line_one_words)
# returns ['The', 'sky', 'has', 'given', 'over']



# 3. Splitting Strings - Part 2
# list.split("word") : word 제외하고 단어 나눠서 줌 

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
print(author_names)
# ['Audre Lorde', 'Gabriela Mistral', 'Jean Toomer', 'An Qi', 'Walt Whitman', 'Shel Silverstein', 'Carmen Boullosa', 'Kamala Suraiyya', 'Langston Hughes', 'Adrienne Rich', 'Nikki Giovanni']

author_last_names = []
for word in author_names: 
  #each word in author_names (e.g. 'Audre Lorde')
  new_list = word.split(" ")
  # split the word with by space to identify last name and the first name 
  author_last_names.append(new_list[1])
  # each last name should be store in author_last_names list 
print(author_last_names)



# 4. Splitting Strings - Part 3
# \n : Newline
# \t : Horizontal Tab 
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

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)



# 5. Joining Strings - Part 1
# .join() : opposite of split() 

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = ' '.join(reapers_line_one_words)
print(reapers_line_one)



# 6. Joining Strings - Part 2
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']
winter_trees_full = '\n'.join(winter_trees_lines)
print(winter_trees_full)



# 7. .strip()
# word.strip() : removes all the whitespace characters from beginning and end. 
# list에 바로 쓸 순 없음 

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
#remove all the white space in each words 
love_maybe_lines_stripped = []
for words in love_maybe_lines:
  love_maybe_lines_stripped.append(words.strip())
print(love_maybe_lines_stripped)
#join them together 
love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)



# 8. Replace
# .replace() - takes two arguments and replace all instances of the first with the second 
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
#missed value Tomer -> Toomer
toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")



# 9. .find()
# .find() : takes a string as argument and searching the string it was run on for that string 
# tells where it is 

god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find("disown")
print(disown_placement)



# 10. .format() - Part 1 
# .format() : takes variables as an argument, and includes them in the string that it is runon. 
# include {} marks as placeholders where should it be imported

def favorite_song_statement(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)

print(favorite_song_statement("Smooth", "Santana"))
# => "My favorite song is Smooth by Santana."

def poem_title_card(title, poet):
  print(f"The poem {title} is written by {poet}.") #can be like this too 
  return "The poem {} is written by {}.".format(title, poet)

print(poem_title_card("I Hear America Singing", "Walt Whitman"))



# 11. .format() - Part 2
# format(artist=artist, song=song)
# format(song=song, artist=artist) not really matters

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(author, title, original_work, publishing_date)
print(my_beard_description)



