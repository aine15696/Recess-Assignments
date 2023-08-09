#__________________________Error handling__________________________________________-

try:
    # Division by zero error
    result = 10 / 0
except ZeroDivisionError:
    # Handling ZeroDivisionError
    print("Error: Division by zero is not allowed")

try:
    # Type error
    result = "10" + 5
except TypeError:
    # Handling TypeError
    print("Error: Unsupported operand types for +")

try:
    # IndexError
    my_list = [1, 2, 3]
    print(my_list[4])
except IndexError:
    # Handling IndexError
    print("Error: Index out of range")

try:
    # File not found error
    with open("nonexistent.txt") as file:
        content = file.read()
except FileNotFoundError:
    # Handling FileNotFoundError
    print("Error: File not found")

try:
    # Value error
    number = int("abc")
except ValueError:
    # Handling ValueError
    print("Error: Invalid literal for int()")

try:
    # Key error
    my_dict = {"name": "John", "age": 25}
    print(my_dict["address"])
except KeyError:
    # Handling KeyError
    print("Error: Key not found in dictionary")
    
try:
    # Custom exception
    raise Exception("Custom error")
except Exception as e:
    # Handling custom exception
    print("Error:", str(e))


#__________________________File handling__________________________________________

# Method 1: Opening and reading a file using the 'open' function and 'read' method
file_path = "sample.txt"
try:
    # Open the file in read mode
    file = open(file_path, "r")

    # Read the contents of the file
    content = file.read()

    # Print the file content
    print("Method 1 - File Content:")
    print(content)

    # Close the file
    file.close()

except FileNotFoundError:
    print("Error: File not found")

# Method 2: Opening and reading a file using a 'with' statement
try:
    with open(file_path, "r") as file:
        # Read the contents of the file
        content = file.read()

        # Print the file content
        print("Method 2 - File Content:")
        print(content)

except FileNotFoundError:
    print("Error: File not found")

# Method 3: Writing to a file
try:
    with open(file_path, "w") as file:
        # Write content to the file
        file.write("Hello, World!\n")
        file.write("This is a sample file.")

    print("Method 3 - File written successfully.")

except FileNotFoundError:
    print("Error: File not found")

# Method 4: Appending to a file
try:
    with open(file_path, "a") as file:
        # Append content to the file
        file.write("\nAdditional content.")

    print("Method 4 - File appended successfully.")

except FileNotFoundError:
    print("Error: File not found")

# Method 5: Reading a file line by line
try:
    with open(file_path, "r") as file:
        # Read the file line by line
        print("Method 5 - File Content (Line by Line):")
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("Error: File not found")
