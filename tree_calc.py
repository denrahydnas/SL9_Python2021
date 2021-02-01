# Step 1
# Ask the user for their name and the year they were born.

name = input("What is your name?  ")
ages = [25, 50, 75, 100]

from datetime import date
current_year = (date.today().year)

while True:
    birth_year = input("What year were you born?  ")
    try:
        birth_year = int(birth_year)
    except ValueError:
        continue
    else:
        break

current_age = current_year - birth_year

# Step 2
# Calculate and print the year they'll turn 25, 50, 75, and 100.
for age in ages:
    if age > current_age:
        print("Congrats, Sandy! You will be {} in {}.".format(age, (birth_year+age)))

# Step 3
# If they're already past any of these ages, skip them.

print("You will turn {} this calendar year.".format(current_age))