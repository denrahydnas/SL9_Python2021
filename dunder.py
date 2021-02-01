#dunder_main_ - use function in separate file

def print_hello():
    print("Hello from Dunder Mifflin")

print(__name__)

if __name__ == '__main__':
    print_hello()