#_____________________________________________________________   LISTS    ___________________________________________________________________________

list_of_names = ["John", "Mary", "David", "Sarah", "Michael"]

#Print the second name
second_item = list_of_names[1]
print(second_item)
print("\n")

# Change the value of the first item
list_of_names[0] = "Robert"
print(list_of_names)
print("\n")

# Add a sixth item to the list
list_of_names.append("Emily")
print(list_of_names)
print("\n")

# Insert "Bathel" as the 3rd item in the list
list_of_names.insert(2, "Bathel")
print(list_of_names)
print("\n")

# Remove the 4th item from the list
del list_of_names[3]
print(list_of_names)
print("\n")

# Print the last item using negative indexing
last_item = list_of_names[-1]
print(last_item)
print("\n")

new_list = ["Python", "Java", "Kotlin", "PHP", "HTML", "C++", "JavaScript"]

# Print the 3rd, 4th, and 5th items using index range
items = new_list[2:5]
print(items)
print("\n")

country_list = ["USA", "Canada", "Australia", "France", "Japan"]

# Make a copy of the list using the slice operator
country_copy = country_list[:]
print("Original List of Countries:", country_list)
print("Copy of the List of Countries:", country_copy)
print("\n")

# Loop through the list of countries
for country in country_list:
    print(country)

# List of animals

print("\n")
animal_list = ["Giraffe", "Tiger", "Lion", "Antelope", "Zebra"]
print("\n")

# Sort the list in ascending order
ascending_order = sorted(animal_list)
print("\n")

# Sort the list in descending order
descending_order = sorted(animal_list, reverse=True)
print("\n")

# Output the sorted lists
print("Animal list in ascending Order:", ascending_order)
print("Animal list in descending Order:", descending_order)
print("\n")

# Filter the list to get names with the letter 'a'
animal_with_a = [name for name in animal_list if 'a' in name.lower()]
print("\n")

# Output the names with 'a'
print("Animal names with 'a':")
for name in animal_with_a:
    print(name)


print("\n")
first_names = ["Daniel", "Aine"]
last_names = ["Mwejune", "Banga"]

# Join the two lists
full_names = first_names + last_names

# Output the joined list
print("Full Names:", full_names)

print("\n")

###################################################    TUPLES    #########################################################

print("\n")
x = ("samsung", "iphone", "tecno", "redmi")
favorite_brand = x[1]
print("Favorite phone brand:", favorite_brand)
print("\n")

#To print the 2nd last item using negative indexing
second_last_item = x[-2]
print("Second Last phone brand:", second_last_item)
print("\n")

#To update "iphone" to "itel"
x = list(x) #changing the tuple to a list such that it can be changed
x[x.index("iphone")] = "itel"  
x = tuple(x) #returning to a tuple
print("Updated Tuple:", x)
print("\n")

#To add "Huawei" to the tuple
x = x + ("Huawei",)
print("Updated Tuple:", x)
print("\n")

#To loop through the tuple
for phone_brand in x:
    print(phone_brand)

#To remove/delete the first item in the tuple
print("\n")
x = x[1:]
print("Updated Tuple:", x)
print("\n")

#Using the tuple() constructor to create a tuple of cities in Uganda
ug_cities = tuple(["Kampala", "Jinja", "Mbarara", "Entebbe"])
print("Cities in Uganda:", ug_cities)
print("\n")

#To unpack the tuple
Vietnam, America, Japan, Korea = x
print("Unpacked Brands:", Vietnam, America, Japan, Korea)
print("\n")

#To print the 2nd, 3rd, and 4th cities using index range
cities = ug_cities[1:4]
print("Cities:", cities)
print("\n")

#To join two tuples of first and second names
first_names = ("Daniel", "Aine")
last_names = ("Mwejune", "Banga")
full_names = first_names + last_names
print("Full Names:", full_names)
print("\n")

#To create a tuple of colors and multiply it by 3
colors = ("Red", "Yellow", "Green")
tripled_colors = colors * 3
print("Triple Color:", tripled_colors)
print("\n")

#To return the number of times 8 appears in the tuple
sample = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
frequency_of_eight = sample.count(8)
print("Frequency of 8:", frequency_of_eight)
print("\n")


###############################################   SETS   ####################################################

#To create a set of 3 favorite beverages using the set() constructor
favorites = set(["yoghurt", "milk", "juice"])
print("Favorites:", favorites)
print("\n")

#To add 2 more items to the beverages set using the add() method
favorites.add("water")
favorites.add("soda")
print("Updated Beverages:", favorites)
print("\n")

#To check if "microwave" is present in the set
test = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in test:
    print("Microwave is in the set.")
else:
    print("Microwave is not in the set.")
print("\n")

#To remove "kettle" from the set
test = {"oven", "kettle", "microwave", "refrigerator"}
test.remove("kettle")
print("Updated Set:", test)
print("\n")

#To loop through the set
test = {"oven", "kettle", "microwave", "refrigerator"}
print("Elements in the set:")
for item in test:
    print(item)
print("\n")

#To add elements from a list to a set
test = {"Python", "Java", "Kotlin", "PHP"}
test2 = ["C++", "JavaScript"]
test.update(test2)
print("Updated Set:", test)
print("\n")

#To join two sets of ages and first names
first_names = {"John", "Mary", "David"}
ages = {25, 30, 35}
joined_set = first_names.union(ages)
print("Joined Set:", joined_set)
print("\n")


###############################################   STRINGS   ###################################################

#To concatenate an integer and a string
number = 20
word = " twenty three"
concatenated = str(number) + word
print("Together:", concatenated)
print("\n")

#To output the string without spaces at the beginning, in the middle, and at the end
txt = " Hello,   Uganda! "
without_spaces = txt.strip()
print("String without spaces:", without_spaces)
print("\n")

#To convert the value of 'txt' to uppercase
uppercase_txt = txt.upper()
print("Uppercase:", uppercase_txt)
print("\n")

#To replace character 'U' with 'V' in the string
replaced_txt = txt.replace("U", "V")
print("Replaced String:", replaced_txt)
print("\n")

#To return a range of characters in the 2nd, 3rd, and 4th position
y = "I am proudly Ugandan"
characters_range = y[1:4]
print("Characters in range:", characters_range)
print("\n")

#To correct the error in the code
x = 'All "Data Scientists" are cool!'
print(x)
print("\n")



#___________________________________________   To print the value of the shoe size  ____________________________________________________
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
shoe_size = Shoes["size"]
print("Shoe Size:", shoe_size)
print("\n")

#To change the value "Nick" to "Adidas"
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
Shoes["brand"] = "Adidas"
print("Updated Shoes:", Shoes)
print("\n")


#To add a key/value pair "type": "sneakers" to the dictionary
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
Shoes["type"] = "sneakers"
print("Updated Shoes:", Shoes)
print("\n")


#To return a list of all the keys in the dictionary
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
keys_list = list(Shoes.keys())
print("Keys List:", keys_list)
print("\n")

#To return a list of all the values in the dictionary
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
values_list = list(Shoes.values())
print("Values List:", values_list)
print("\n")

#To check if the key "size" exists in the dictionary
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
if "size" in Shoes:
    print("Key 'size' exists in the dictionary.")
else:
    print("Key 'size' does not exist in the dictionary.")
print("\n")

#To loop through the dictionary
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print("Dictionary Items:")
for key, value in Shoes.items():
    print(key, ":", value)
print("\n")

#To remove "color" from the dictionary
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
Shoes.pop("color")
print("Updated Shoes:", Shoes)

#To empty the dictionary
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
Shoes.clear()
print("Empty Shoes:", Shoes)

#To make a copy of a dictionary
original_dict = {"name": "John", "age": 30}
copy_dict = original_dict.copy()
print("Copy Dictionary:", copy_dict)
print("\n")

#To show nested dictionaries
students = {
    "student1": {
        "name": "John",
        "age": 20,
        "grade": "A"
    },
    "student2": {
        "name": "Sarah",
        "age": 18,
        "grade": "B"
    }
}

print("Nested Dictionaries:")
for student, details in students.items():
    print(student, ":", details)
print("\n")
