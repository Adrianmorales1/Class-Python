# do not need a var or let or const in python
from operator import truediv


string = "Hello World"
#Printing materials 
print(string)

def adogs_method():
    print("whats up its adog")

adogs_method()

#if statements
new_number = 23
if(new_number == 23): 
    print("New Number is 23")
else:
    print("number did not match")


#integers
price = 20
another_price = 10
total_price = price + another_price #adding 
print(total_price) #30
message = "My age is "
adrians_age = 20
print(message + str(adrians_age))

#Strings
first_name = "Adrian "
last_name = "Morales"
full_name = first_name + last_name
print(full_name)

#booleans 
iswaterwet = True # CAPITAL T
oneequalstwo = False # CAPTIAL F
if(iswaterwet) : 
    print("Yessssss")
else: 
    print("noooo")


#list - container that stores values in javascript it would be []
colors = []
colors.append("blue")
colors.append("red")
colors.append("green")
print(colors) #['blue', 'red', 'green']
print(len(colors)) #len = .length which would be 3
print(colors[0]) #"blue"

#dictionaries - Key/Value
my_dict = {
    "name": "Adrian Morales",
    "age": 20,
    "stack": "Python"
}
my_dict["location"] = "Minneapolis" #Adding in dictionaries
print(my_dict)
print(my_dict["name"])

#Tuples same as list but they are immutable. Made by using "()"!!

dog = ("Canis", "dog", "Carnivore", 12)

#Conditionals 
age = 18
if iswaterwet:
    print("yessir")
    if(age >18) :
        print("you're older than that")
elif iswaterwet == True:
    print("its not getting here")

#loops FOR LOOP YAYYY
for color in colors:
    print(color)

for index in range(3):
    print(colors[index])
    
for i in range(2,7):
    print(i)