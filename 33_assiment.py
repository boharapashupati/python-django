      #create list
      
1.# append data to list and print
# my_home = ["teable","tv","kichan room"]
# my_home.append("fan")
# my_home.append("water")
# my_home.append("watch")
# print(my_home)      #['teable', 'tv', 'kichan room', 'fan', 'water', 'watch']

2.#access list item using for loop
# furets_list = ["apple","mango","orange","lamon","lichee","banana"]
# for item in furets_list:
#     print(item)


     #createndicationary 
3.# how to access and change value of dictionary
# my_dict = {"name":"pashupati","age":"20","study":"python","frind_name":"sangita"}
# print(my_dict["frind_name"])

4.#access dictionary item using for loop
# my_dict = {
#     "name":"pashupati bohara",
#     "age" :"20",
#     "city" :"kathmandu",
#     "country":"nepal",
# }
# for key in my_dict:
#     value = my_dict[key]
#     print(f'key:{key},value:{value}')
        
        #add dictionary to list
        
#print percentage and student name using loop from 
data = [{'name':"salman",'percentage':45},
        {'name':"mithun",'percentage':56},
        {'name':"katrina",'percentage':34}
        ] 
for student in data :
 print(f" {student["name"]}, percentage:{student["percentage"]}")
