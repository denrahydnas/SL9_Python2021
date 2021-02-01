#enumerate 

groceries = ['roast beef', 'cucumbers', 'lettuce', 'peanut butter', 'bread', 'dog food']

index = 1

for item in groceries:
    print(f'{index}. {item}')
    index += 1

for index, item in enumerate(groceries, 1):
    print(f'{index}. {item}')

for i in range(4, 24, 6):
    print(i)

print(groceries[::-3])
print(len(groceries))
print(max(groceries))
print(min(groceries))

#ranges

my_list = []

for val in range(10):
    my_list.append(val)

print(my_list[1::2])
print(my_list[::-2])
print(len(my_list))
print(max(my_list))
print(min(my_list))


#membership testing - in and not in, count, index

text = "We have a growing team of excellent product managers that are fully remote and spread across the world. The role will work closely with the product and engineering teams to drive Hopin product forward."
keyword = (input("What word do you want to search for?  "))

if keyword in text:
    print ("keyword '{}' is here {} times".format(keyword, (text.count(keyword))))
else:
    print("keyword '{}' is not here".format(keyword))

print(text.index(keyword))

#concatenation

group1 = ['Bob', 'Frederika', 'Sam', 'Eugenia']
group2 = ['Sue', 'Robert', 'Mark', 'Marie']
people = group1 + group2
print(people)
print(keyword*5)