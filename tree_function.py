
def add_three(num1, num2, num3):
    val = num1 + num2 +num3
    return val
   
val1 = int(input("pick a number:  "))
val2 = int(input("pick another number:  "))
val3 = int(input("pick another number:  "))

print(add_three(val1, val2, val3))



def hello_class(*args):
    for person in args:
        print("Hello, " + person)

hello_class(input("What is your name? "))

person1, person2, person3, person4 = input("name 4 people in your class separated by commas:  "  ).split(", ")

hello_class(person2)
hello_class(person4)
hello_class(person3)
hello_class(person1)


