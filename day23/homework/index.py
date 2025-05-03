#Ask the user for a name then create a function that will have one parameter that will be passed as an argument the user's entered name and then greet him

user_name = input("What's your name? ")

def greet(name):
    print(f"Hello, {name}! Nice to meet you.")
greet(user_name)