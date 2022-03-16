#Changing the Datatype of variable

#x=float(5)
#print(x)
#y=int(6.5)
#z= x+y
#print (y)
#print(type(z))

#String in python
y= int(5.9)
print (y)

a = 331
b = 200
c = 500
if b > a & b > c:
 print("b is greater")
elif c > a & c > b:
 print("c is greater")
else:
 print("a is greater than b")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

a = "Hello, World!"
print(a[0])

for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))

x= 'I love my India'
if "love" in x:
 print ("love is present in x ")

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print (""""The Program to check the greatest number by if statement
                
                
                """)

a = 8
b = 7
c = 9
if a > b & a > c:
 print("a is greater in three")
elif b > a & b > c:
 print("b is greater in three")
else:
 print("c is greater in three")



 x = "Hello"
 y = 15
 print(bool("Hello"))
 print(bool(15))


 bool("abc")
 bool(123)
 bool(["apple", "cherry", "banana"])

 print("**********")

 def myFunction():
  return False

 if myFunction():
  print("YES!")
 else:
  print("NO!")

 print("*****Removing blank space from text*****")

 txt = " This text is with space in begining and end "
 x = txt.strip()
 print (x)

 print("*changing text to upper case****")
 txt = " This text is with space in begining and end "
 x = txt.upper()
 print (x)

 print("*add a placeholder for the age parameter****")

 age = 36
 txt = "My name is jon and i am {}"
 x = print(txt.format(age))

 print("*Replacing text in list****")
 fruits = ["apple", "banana", "cherry"]
 fruits[0]= "Kiwi"
 print(fruits)

 print("*Creating and printing a list****")
 list= ["Mango","Apple","grapes","banana","tomato","Apple"]
 print (list)
 print(len(list))
 print(type(list))

 print("*Range of indexes****")

 thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
 print(thislist[2:5])
 thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
 print(thislist[:4])
 thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
 print(thislist[2:])

 thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
 print(thislist[-4:-1])

 thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
 thislist[1:3] = ["blackcurrant", "watermelon"]
 print(thislist)

 print("******To append elements from another list")
 fistlist = ["Apple","Mango","Banana"]
 secondlist = ["grapes","Mango","Milk"]
 fistlist.extend(secondlist)
 print(fistlist)

 print("****** To append tuple with list****")
 fistlis = ["Apple", "Mango", "Banana"]
 secondlis = ("grapes", "Mango", "Milk")
 fistlis.extend(secondlis)
 print (fistlis)
 fistlis.remove("Apple")
 print(fistlis)

 print("****** For looo in list ***")
 flist = ["Apple", "Mango", "Banana"]
 for x in flist:
  print(x)

 print("****** For loop in list ***")
 fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
 nfruits = []
 for x in fruits:
  if "a" in x:
   nfruits.append(x)
 print(nfruits)

 print("******Uppercase conversion*********")
 fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
 newlist =[x.upper() for x in fruits]
 print(newlist)

 print("******filtering from list********")
 fruit = ["apple", "banana", "cherry", "kiwi", "mango"]
 list = [x for x in fruit if x != "apple"]
 print (list)


 print("******sorting in list********")
 sfruit = ["kiwi", "mango", "banana", "apple", "cherry"]
 sfruit.sort()
 print(sfruit)

 thislist = [100, 50, 65, 82, 23]
 thislist.sort()
 print(thislist)

 fruit = ["apple", "cherry", "banana", "kiwi", "mango"]
 fruit.sort(reverse= True)
 print(fruit)

 print("******copying a list***")

 #s1 =  ["apple", "cherry", "banana", "kiwi", "mango"]
 #ls2 = ls1.copy()
 #s2 = list(ls1)
 #print (ls2)

 print("****** For loop in list 2***")
 fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
 nfruits = [x for x in fruits if "a" in x]
 print (nfruits)



 thisset = {"apple", "banana", "cherry"}
 #= print("banana" in thisset)
 for x in thisset:
  if "kiwi" in x:
   print("kiwi is there")
  else:
   print("not there")
