# goal is create a calculator how would I do this? take user input then grab their input and solve it so lets try that... Didn't work
#What this actually does is the user selects an operation then the user inputs 2 numbers and it uses the operation they picked to solve it
while True:
    math_func = input("1: addition 2: subtraction 3: multiplication 4: division ").strip().lower() #The user picks which operation they wish to do
    if math_func == "1" or math_func == "addition": #This grabs the user selection
        num1 = float(input("Enter a number: ")) # this uses typecast so it turns a users input into a number
        num2 = float(input("Enter a number again: ")) # this uses typecast so it turns a users input into a number
        print(num1 + num2) # solves users problem
    elif math_func == "2" or math_func == "subtraction": #This grabs the user selection
        num1 = float(input("Enter a number: ")) # this uses typecast so it turns a users input into a number
        num2 = float(input("Enter a number again: ")) # this uses typecast so it turns a users input into a number
        print(num1 - num2) # solves users problem 
    elif math_func == "3" or math_func == "multiplication": #This grabs the user selection
        num1 = float(input("Enter a number: ")) # this uses typecast so it turns a users input into a number
        num2 = float(input("Enter a number again: ")) # this uses typecast so it turns a users input into a number
        print(num1 * num2) # solves users problem
    elif math_func == "4" or math_func == "division": #This grabs the user selection
        num1 = float(input("Enter a number: ")) # this uses typecast so it turns a users input into a number
        num2 = float(input("Enter a number again: ")) # this uses typecast so it turns a users input into a number
        if num2 == 0: # i tried to do "0" like a dumbass but then I realized that it turns it from a str to an int so 0 is valid
            print("You cannot divide by 0")
        else:
            print(num1 / num2) # solves users problem
    else:
        print("Please select one of the numbers 1 - 4")
    Break_loop = input("Do you wish to break this loop? (yes/no) ").strip().lower()
    if Break_loop == "yes":
        break
    else:   
        print("Okay, proceed to next calculation")

    