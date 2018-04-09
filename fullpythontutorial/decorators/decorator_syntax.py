def be_polite(fn):
    def wrapper():
        print("Nice to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite
def greet():
    print("My name is Sergey")

greet()
