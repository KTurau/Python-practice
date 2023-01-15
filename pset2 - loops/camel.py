# In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the
# corresponding name in snake case. Assume that the user’s input will indeed be in camel case.


camelCase = input("camelCase: ")

for i in camelCase:
    if i == i.lower():
        print(i, end="")
    else:
        print("_" + i.lower(), end="")
