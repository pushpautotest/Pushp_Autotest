# Accessing a Dictionary
# car = {
#     "Brand" : "Maruti",
#     "Model" : "Suzuki",
#     "Year" : 2021
# }
# x =  car["Brand"]
# print (" Brand of car is: \n", x)

# accessing dictionary using get() method
# emp = {
#     "Name" : "Pushpender",
#     "Last Name" : "Singh",
#     "designation" : "Qa"
# }
# x = emp.get("Last Name")
# print(x)

# accessing all keys of dictionary using key() method

# emp = {
#     "Name" : "Pushpender",
#     "Last Name" : "Singh",
#     "designation" : "Qa"
# }
# x = emp.keys()
# print (x)

# accessing all keys of dictionary using value() method
# emp = {
#     "Name" : "Pushpender",
#     "Last Name" : "Singh",
#     "designation" : "Qa"
# }
# x = emp.values()
# print (x)
#
# emp ["experience"] = 7    # adding new element to dictionary
# print (x)
#
# # items() method will return each item in a dictionary, as tuples in a list.
# x = emp.items()
# print (x)

# To determine if a specified key is present in a dictionary use the "in" keyword

# emp = {
#     "Name" : "Pushpender",
#     "Last Name" : "Singh",
#     "designation" : "Qa"
# }
# # if "lst" in emp:
# #  print ('Yes, Name is a key present in "emp"')
# # else:
# #  print ('Its not there in "emp"')
#
# # Changing the value of any specific key
# x = emp.items()
# print (x)
# emp["Name"] = "Bhupinder"
# print (x)

# The update() method will update the dictionary
# emp = {
#     "Name" : "Pushpender",
#     "Last Name" : "Singh",
#     "designation" : "Qa"
# }
# emp.update({"designation" : "Quality Analyst"})
# print(emp.items())

# The pop() method will remove the item with specified key name

# emp = {
#     "Name" : "Pushpender",
#     "Last Name" : "Singh",
#     "designation" : "Qa"
# }
# emp.pop("Last Name")
# # emp.popitem()
# # print (emp)
# # del emp
# emp.clear()
# print(emp)
# For loop though a dictionary // o
# for x in emp:
#   Print all key names in the dictionary, one by one
#  print(x)
#
# #Print all values in the dictionary, one by one
#  print(emp[x])

# You can use the keys() method to return the keys of a dictionary

# for x in emp.keys():
#  print(x)
#
# for x in emp.values() :
#  print(x)
#
# for x,y in emp.items():
#     print (x,y)

# Make a copy of a dictionary with the copy() method:
emp = {
    "Name" : "Pushpender",
    "Last Name" : "Singh",
    "designation" : "Qa"
}
# emp2 = emp.copy()
# print (emp2)

# Make a copy of a dictionary with the dict() function:
emp2 = dict(emp)
print (emp2)
