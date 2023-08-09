# Using slice() and len() function on a string
Str = "Aine Daniel Mwejune"
len(Str)
starting_index = 4
ending_index = 12
sliced_string = Str[slice(starting_index, ending_index)] 
print(sliced_string)

# Using a for loop on a string
for char in Str:
    print(char)

# Showing a string within another string
name = "Daniel"
language = "python"
years = 4
message = "My name is {} and I have been using {} for the past {} year(s).".format(name, language, years)
print(message)