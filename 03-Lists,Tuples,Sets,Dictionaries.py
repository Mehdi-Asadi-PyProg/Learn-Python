# List is a data structure that stores multiple itmes in a specific order mean each element has an index number
# Orderd != sorted and first itme index = 0 and last itme index = -1
print("-"* 60)
myList = [0,6,7,3,4,2,9,1]
print(myList[-1])
i = myList.pop()    # get last itme from list
print(i)
myList.sort()       # Sort list Items
print(myList)
myList.append(13)   # Append an item at the end of current list
print(myList)

# nested List
nList = [1,"joe",[0,4,2,6,7,9]]
print(nList[2][1])  # get index 2 items [0,4,2,6,7,9] then get index 1 of retrived Item that is a list itself!


# Set is unordered collection that stores Unique values and does not allow duplicate value!
print("-"* 60)

numbers = {3,1,3,4,5,2,6,8,9,3}
print(numbers)
numbers.add(23)
print(numbers)

myset = set()
myset.add(9)
myset.add(13)
print(myset)
numbers = numbers.union(myset)         # create Union of two sets
print(numbers)
numbers = numbers.intersection(myset)  # create intersection of two sets
print(numbers)
numbers.difference(myset)              # Find Elementes that are in one set and not in another set
print(numbers)

numbers.pop()
print(numbers)

# Tuple is an ordered, immutable(Could not be changed) collection of itmes  that can store elements of 
# diffrent data types and is created usting ()
# This type is as same as list but is faster and resource efficient than lists
print("-"* 60)

myTuple = tuple([1,2,3,4,5,6])
print(myTuple)
mixedTuple = (1,"Hello World",3.14159,True)
print(mixedTuple)

print(myTuple[-1])
print(myTuple[3:])

lst = [[1,2,3,4,5],[6,7,8,9],[1,"Hello",3.14159,"c"]]
print(lst[2][1])

# Dictionary is a data structure that stores data as key:alue pairs, each key:value 
# is unique and is used to access its corresponding value
print("-"* 60)

score = {
            "Joe": {
                    "Math":60,
                    "Programming" :82,
                    "English" : 70
                     },
            "Sara": {
                    "Math":65,
                    "Programming" :70,
                    "English" : 75
                     },
             "Tom": {
                    "Math":68,
                    "Programming" :73,
                    "English" : 75
                     },
        }

print("Items Of Dictionare \n", score.items())          # Show Items Of Disctionary
print("List Of Values Are \n ",score.values())          # Show Values Of Dictionary
print("List Of Keys Are \n ",score.keys())              # Show Keys Of Dictionary
print("Joe's Elements Are \n ",score.get("Joe"))        # Show Key:Values Of A person
print("Joe's Math Score is \n ", score["Joe"]["Math"])  # Show a value of A Person

score["Alvarez"]= {                                     # Add A Person To Dictionary
                    "Math":58,
                    "Programming" :65,
                    "English" : 80
                     }
print("Items Of Dictionare \n", score.items())

score.pop("Tom")
print("Items Of Dictionare \n", score.items())          # Delete A Person From Dictionary
