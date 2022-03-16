car = {
    "brand": "Ford",
    "model": "mustang",
    "year" : 1967
     }
print (car["brand"])
print (type(car))

print ("""***** get the value of model key""")
thisdict = {
    "brand": "Ford",
    "model": "mustang",
    "year" : 1967
     }
x= thisdict.get("year")
print (x)

print ("""***** get the list of all keys****""")
thisdict = {
    "brand": "Ford",
    "model": "mustang",
    "year" : 1967
     }
print(thisdict.keys())
thisdict["color"] = "white"
print(thisdict.keys())

print ("""***** get the list of all values****""")
print (thisdict.values())

print ("""***** Printing upto values****""")

i = 0
while i < 100:
    i = i+1
    print(i)

print ("""***** Counting in descending order****""")
i = 101
while i > 0 :
   i = i-1
   print (i)


thisdi = {
    "brand": "Ford",
    "model": "mustang",
    "year" : 1967
     }
x = thisdi.items()
print(x)

print ("""*****  the square of a number ****""")
a = input("please enter the number to find its square root:")
a = int(a)
print ("The square of number is ", a*a)


