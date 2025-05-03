#An algorithm is a step-by-step process that someone takes or makes.

algorithm = "I am going to first drive to the place, come back, and do the same tommorow" #algorithm = repeated process over time.
algorithm2 = "I wake up in the day, work, go to sleep, and do it all over again."
algorithm3 = "I went to work, ate a sandwich, got home, slept, and did the same process for a long time."
algorithm4 = "I went to make a recipe, I used oil and cut up fries, let it refregierate, and did the same process tommorow."
algorithm5 = "I decided to go to kfc, I ate, went back home, played games, slept, ate kfc tommorow, came back, gamed, and slept, etc." #An algorithm does not have to be a never ending process.

#psuedocode

# 1. Input: ask for two numbers 
# 2. process: add the two numbers 
# 3. output: display the numbers.

# num1 = int(input("enter the first number: "))
# num2 = int(input("enter the first number: "))
# result = num1 + num2
# print(f"The result is {result}")


#starting flowchart

# num = float(input("enter a number:"))

# while num > 0 :
#     num = num - 1
#     print(num)
#     print("done")

# Start of program
# Prompt user to enter a number
# x = int(input("Enter a number: "))

# # Check if x is greater than 5
# if x > 5:
#     print("The number is greater than 5.")
# else:
#     print("The number is less than or equal to 5.")

# def login():
#     authorized = False
#     correct_username = "sigma"  # Example username
#     correct_password = "bababoi"  # Example password
    
#     while not authorized:
#         username = input("Enter username: ")
#         password = input("Enter password: ")

#         # Check if the credentials match
#         if username == correct_username and password == correct_password:
#             authorized = True
#         else:
#             print("Invalid username or password. Please try again.")
    
#     print("Done")
# :""

def login_check():
    while True:
        # Step 2: Prompt user to enter a number
        user_input = input("Enter a number: ")
        
        try:
            # Convert input to integer
            number = int(user_input)
            
            # Step 3: Check if the number is greater than 5
            if number > 5:
                print("Access Granted.")
                break  # Exit the loop if condition is met
            else:
                print("The number is not greater than 5. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
login_check()        
# Calling the function to start the process