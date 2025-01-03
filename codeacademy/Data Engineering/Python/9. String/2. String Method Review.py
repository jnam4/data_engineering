#Chapter9 : String Method Review
#2025.01.02
#Jiyun Nam
#@codecademy

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"


# spliitng
highlighted_poems_list = highlighted_poems.split(",")

# remove whitespace
highlighted_poems_stripped = []
for words in highlighted_poems_list:
  highlighted_poems_stripped.append(words.strip())


#break up all the information for each poem
highlighted_poems_details = []
for words in highlighted_poems_stripped:
  highlighted_poems_details.append(words.split(":"))

#split 
titles = []
poets = []
dates = []
for words in highlighted_poems_details:
  titles.append(words[0])
  poets.append(words[1])
  dates.append(words[2])

print(titles)

# print(len(highlighted_poems_details)) :11
for i in range(0, len(highlighted_poems_details)):
  print("The poem {titles} was published by {poets} in {dates}".format(titles = titles[i], poets = poets[i], dates = dates[i]))
#format
