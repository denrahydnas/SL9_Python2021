def get_user_input():
    first_name = input("What is your first name: ")
    middle_initial = input("What is your middle initial: ")
    last_name = input("What is your last name: ")
    print(f'Hello {first_name} {middle_initial} {last_name}! Welcome to Code Louisville - Monday Night Python Class')
def main():
    get_user_input()
if __name__ == "__main__":
    main()