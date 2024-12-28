#Chapter4: Loop
#2024.12.27
#Jiyun Nam
#@codeacademy

#Why Loops?
#Can be more efficient 
# Write 10 print() statements below! 
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")


#1. For Loops-Intro
#will know how many times the loop will need to be
#for <temporary variable> in <collection>:action
#for i in ingredients:
  #print(i)

#Indentation-should be in the body
#Elegant loops-in one line

board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]
sport_games = ["football", "hockey", "baseball", "cricket"]

#prints each game in the list board_games
for game in board_games:
  print(game)
#prints each sports in the list sport_games
for sports in sport_games:
  print(sports)


#2. For Loops-Using Range
#for <temporary variable< in <list of length 6>:print("Learnig Loops!")
promise = "I will finish the python loops module!"
for temp in range(5):
  print(promise)