#Chapter3: List Method
#2024.12.27
#Jiyun Nam
#@codeacademy


#1. .insert()
#add element to a specific index in a list 
#list_name.insert(# where to put, "vocab")
#If want to put front, need to put as 0 
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)
# Your code below: 
front_display_list.insert(0, "Pineapple")
print(front_display_list)



#2. .pop()
#index for the element to remove
#remove in the opposite order
data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)
#Your code below:
#remove "Python 3"
remove_elements1 = data_science_topics.pop()
print(data_science_topics)
print(remove_elements1)
#remove "Algorithms"
remove_elements2 = data_science_topics.pop(-2)
print(data_science_topics)
print(remove_elements2)



#3.range()
#create range objects => use this obejct as list, need to convert thru list()
#0 to 8
number_list = range(9) 
print(list(number_list)) #[0,1,2,3,4,5,6,7,8]
#0 to 7
zero_to_seven=range(8)
print(list(zero_to_seven))

#start from 5, ends before 15, difference of 3
range_five_three = range(5, 15, 3)
print(list(range_five_three))

#starts from 0, ends before 40, difference 5
range_diff_five = range(0,40,5)
print(list(range_diff_five))



#4. len(list)
#get number of elements in the list
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 10)

# Your code below:
long_list_len = len(long_list)
print(long_list_len)
big_range_length = len(big_range)
print(big_range_length)

big_range = range(2, 3000, 100)
big_range_length = len(big_range)
print(big_range_length)


