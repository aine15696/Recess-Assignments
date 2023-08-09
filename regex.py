# Regular expressions in python 
'''
\d: Matches any digit character.
\D: Matches any non-digit character.
\w: Matches any alphanumeric character or underscore.
\W: Matches any non-alphanumeric character or underscore.
\s: Matches any whitespace character.
\S: Matches any non-whitespace character.
[abc]: Matches any single character from the given set.
[^abc]: Matches any single character not in the given set.
[a-z]: Matches any lowercase letter from a to z.
[A-Z]: Matches any uppercase letter from A to Z.
[0-9]: Matches any digit from 0 to 9.
Quantifiers:

*: Matches zero or more occurrences of the preceding character or group.
+: Matches one or more occurrences of the preceding character or group.
?: Matches zero or one occurrence of the preceding character or group.
{n}: Matches exactly n occurrences of the preceding character or group.
{n,}: Matches n or more occurrences of the preceding character or group.
{n,m}: 
\b: Matches a word boundary.
\B: Matches a non-word boundary.
'''

# Matching and and Searching 
#regex re.match(), re search(), re.findall()

## Example1 Demonstrating regex | match first word, match group word, match all numbers

import re
text = "Hello World, My name is Johnson11"

# Match first word
match = re.match(r"\b\w+\b", text)
if match:
        print("Match:", match.group())

# Match all numbers
match = re.match(r"\d+", text)
if match:
        print("Match:", match.group())

# Match group word
match = re.search(r"\b\w+\b", text)
if match:
        print("Match:", match.group())
        

## Example2 validate email format or email address
import re 

def validate_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
                return True
        else:
                return False

# Example usage 
email1 = "kalijoe113@gmailcom"
email2 = "kalijoe@gmail.com"

print(validate_email(email1))
print(validate_email(email2))

# Generators and Iterators
# 'yield' generator
# Iterator '__iter__'"__next__" iterator

def factorial(n):
        if n == 0:
                return 1
        else:
                return n * factorial(n - 1)            
# print(factorial(5))
for i in range(1, 10):
    print(factorial(i))

#Example3
# Generate function that yields the square of nubers from 1 to 10
def squares():
        for i in range(1, 10):
                yield i**2

squares_iterator=squares()

for i in range(5):
        print(next(squares_iterator))

# Decorators    