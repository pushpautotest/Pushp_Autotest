print ("***** Tuple****")

thistuple = ("one", "Two", "Three", "four")
print(thistuple)

print ("***** Tuple with one item ****")
ntuple = ("apple",)
print (type(ntuple))

print ("***** Data type in tuple ****")
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))

print ("***** A tuple with strings, integers and boolean values ****")

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

print ("***** Check if apple is present in the tuple ****")
thistuple = ("one", "Two", "Three", "four")
if "Three" in thistuple:
    print(" Three is present")
else:
    print("three not found")


print ("***** Change Tuple Values ****")
tuple1 = ("apple", "banana", "cherry")
lis = list(tuple1)
lis[1]= "Kiwi"
tuple1 = tuple(lis)
print (tuple1)

print("**** For loop Through a Tuple***")
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
 print(x)

print("**** while loop Through a Tuple***")
thistuple1= ("one", "Two", "Three", "four")
i=0
while i < len(thistuple1):
 print(thistuple1[i])
 i=i+1

print("**** multiply Tuple***")
thistuple= ("one", "Two", "Three", "four")
tuple3= thistuple*2
print(tuple3)