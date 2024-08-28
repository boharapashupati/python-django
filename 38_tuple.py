# first_tuple =("apple","ball")
# print(type(first_tuple))
# print(first_tuple[0])
# my_tuple = (1, 2, 3, "hello", 4.5)
# print(my_tuple)



#write a difference between tuple,list,set.




# write a program to add item in tuple.

# my_tuple = (1, 2, 3,4,5)
# new_item.append(6)
# new_tuple = my_tuple + (new_item,)
# print(my_tuple)
# print(new_tuple)



new_tuple = ("pashupati", "sangita", "ambika")
my_item = []  
my_item.append("b")
new_tuple = new_tuple + (my_item,)  # Convert my_item to a tuple and concatenate
print(new_tuple)
print(my_item)