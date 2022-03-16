thisset= {"apple","ball","cat","dog"}
print(thisset)
print(type(thisset))
print(len(thisset))


print ("***** Loop through the set, and print the values: ****")
thisset1= {"apple","ball","cat","dog"}
for x in thisset1:
    print(x)

print ("***** Check in item present in Set ****")
new= {"apple","ball","cat","dog"}
if "kiwi" in new:
    print("kiwi is present")
else:
    print ("kiwi not fount")

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

print ("***** adding items to set ****")
new= {"apple","ball","cat","dog"}
new.add("elephant")
print(new)

print ("*****  add items from another set into the current set ****")
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

print ("*****  Using set constuctor ****")
thissetn = set(("apple", "banana", "cherry"))
print (type(thissetn))

print ("***** Add elements of a list to at set ****")

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

print ("***** Add elements of a list to at set ****")
thisset5 = {"apple", "banana", "cherry"}
thisset5.remove("apple")
print(thisset5)

thisset5.discard("cherry")
print(thisset5)

print ("***** Remove the last item by using the pop() method ****")
ab = {"apple", "banana", "cherry"}
c = ab.pop()
print (c)
ab = {"apple", "banana", "cherry"}
ab.clear()
print(ab)

print ("***** set items by using a for loop ****")
abc = {"apple", "banana", "cherry"}
for x in abc:
 print(x)

print ("***** You can use the union() method  ****")
abc = {"apple", "banana", "cherry"}
xyz = {"tomato","potato",",mango"}
rs = abc.union(xyz)
print(rs)

print ("***** The update() method  ****")
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


print ("***** Keep ONLY the Duplicates  ****")
set3 = {"a", "b" , "c"}
set4 = {"a", "d" , "e"}
set3.intersection_update(set4)
print(set3)

print ("***** Keep those who are unique  ****")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)