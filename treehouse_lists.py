shopping_list = []


def show_help():
    print("What should we pick up at the store? ")
    print("""
    Enter 'DONE' to stop adding items
    Enter 'HELP' for this help.
    Enter 'SHOW' to view list
    """)


def add_item(item):
    shopping_list.append(item)
    print("Your list has {} items".format(len(shopping_list)))


def show_list():
    print()
    print("Your List: ")
    for item in shopping_list:
        print(item)

show_help()
while True:
    new_item = input("> ")
    if new_item == 'DONE':
        show_list()
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue


    add_item(new_item)
    





