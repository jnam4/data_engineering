#Project:   Scrabble
#Date:      2025.01.02
#Creator:   Jiyun Nam

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Build your Point Dictionary 
# 1. Create a dictionary 
# key, value
letter_to_points = dict(zip(letters, points))
# zip -> zip object  으로만 떠서 dict 으로 감싸줘야함

# 2. Add element has key of " " and value 0 
letter_to_points[" "] = 0
print(letter_to_points) 


# Score a Word 
def score_word(word):
  point_total = 0  #key, value
  for letter in word: 
    if letter in letter_to_points.keys():
      point_total += letter_to_points[letter]
    else:
      point_total += 0 
  return point_total 

brownie_points = score_word("BROWNIE")
print(brownie_points)



# Score a Game
# Create a dicitonary called player to words 
player_to_words = {
  "Player1": ["BLUE", "EARTH", "ERASER", "ZAP"], 
  "Player2": ["TENNIS", "EYES", "BELLY", "COMA"], 
  "Player3": ["EXIT", "MACHINE", "HUSKY", "PERIOD"]}

# Create a empty dictionary 
player_to_points = {}
print(list(player_to_words.items()))

for player, words in player_to_words.items():
  player_points = 0 
  print("") #Indent
  print(f"{player} have list of {words}")
  print(f"The beginning is {player_points}")
  for words in words: 
    player_points += score_word(words)
    print(f"The sum of next word is {player_points}")
  player_to_points[player] = player_points 
  print(f"The total sum of player is {player_points}")

