# create a dictionary and take input from the user and return the meaning of the word from the dictionary

d1 = {"set": "It is a collection of well similar data", "array": "It is a collection of same data type elements",
      "class": "It is a user define data type that store the different type of data",
      "variable": "It is a box that store only one type of data"}

print(d1)

print(d1[input("Enter a search word from the dictionary: ")])


# user input dictionary
d2 = {}

key = input("enter a key for dictionary: ")
value = input("Enter value for key: ")
d2[key] = value
print(d2)