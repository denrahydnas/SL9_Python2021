# Columns: Name, Day/Month, Celebrates, Age
BIRTHDAYS = (
    ("James", "9/8", True, 9),
    ("Shawna", "12/6", True, 22),
    ("Amaya", "28/2", False, 8),
    ("Kamal", "29/4", True, 19),
    ("Sam", "16/7", False, 22),
    ("Xan", "14/3", False, 34),
)

# Problem 1: Celebrations
# Loop through all of the people in BIRTHDAYS
# If they celebrate their birthday, print out
# "Happy Birthday" and their name
print("Celebrations:")

# Solution 1 here
for parties in BIRTHDAYS:
    if parties[2] == True:
        print("Happy Birthday {}!".format(parties[0]))

print("-"*20)

# Problem 2: Half birthdays
# Loop through all of the people in BIRTHDAYS
# Calculate their half birthday (six months later)
# Print out their name and half birthday
print("Half birthdays:")

# Solution 2 here
for birthday in BIRTHDAYS:
    name = birthday[0]
    date = birthday[1].split('/')
    date[1] = int(date[1]) + 6
    if date[1] > 12:
        date[1] -= 12
    date[1] = str(date[1])
    
    print(name, "/".join(date))

print("-"*20)

# Problem 3: Only school year birthdays
# Loop through the people in BIRTHDAYS
# If their birthday is between September (9)
# And June (6), print their name
print("School birthdays:")

# Solution 3 here
for school in BIRTHDAYS:
    name = school[0]
    date = school[1].split('/')
    date[1] = int(date[1])

    if date[1] not in range(7,9):
        date[1] = str(date[1])
        print(name)

print("-"*20)

# Problem 4: Wishing stars
# Loop through BIRTHDAYS
# If the person celebrates their birthday,
# AND their age is 10 or less,
# Print out their name and as many stars as their age
print("Stars:")

# Solution 4 here
for stars in BIRTHDAYS:
    name = stars[0]
    age = stars[3]
    if stars[2] == True and age <=10:
        print(name, " *"*age)


print("-"*20)