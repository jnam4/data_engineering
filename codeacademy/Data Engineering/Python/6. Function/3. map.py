#Chapter6: map
#2024.12.29
#Jiyun Nam
#@codeacademy

# map(function, iterable, [iterable2, iterable3, ...]) 


def double(x): 
    return x * 2 
numbers = [1, 2, 3, 4, 5] 
doubled_numbers = map(double, numbers) 
print(list(doubled_numbers))  # Output: [2, 4, 6, 8, 10] 