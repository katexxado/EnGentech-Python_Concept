def check(char):

    if len(char) > 1:
        print("Not more than one character at a time, try again")
        return check(input(" Enter a Single Charater"))

    if not char.isalpha():
        print("None Alphabetical character is allowed, please try again")
        return check(input(" Enter a Single Character"))

    if char == char.lower():
        return f"The input {char} is a lowercase"
    else:
        return f"The input {char} is an Uppercase"

print(check("b"))
print(check("H"))

