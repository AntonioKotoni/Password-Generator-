import random 
import array

# Function to Generate the Actual Username/Password
def password_generator(choice_size, user_special):

    # Array with all possible digits
    DIGITS =                ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # Array with all possible lower case letters
    LOCASE_CHARACTERS =     ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                            'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                            'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                            'z']
    # Array with all possible upper case letters
    UPCASE_CHARACTERS =     ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                            'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                            'R', 'S', ' T', 'U', 'V', 'W', 'X', 'Y',
                            'Z']
    # Array with all common Symbols
    SYMBOLS =               ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                            '*', '(', ')', '<']

    # An Array that is a combination of all of the arrays above
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS 
    # Similar to Combined list but excludes the SYMBOLS array
    PARTIAL_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS
    # String that will hold the final username/password
    final_random = ""

    # If user wants special characters
    if user_special.lower() == "yes":
        while(choice_size != 0):
            # Making sure that all output has at least one uppercase, one lowercase, one digit, and one special character
            if choice_size == 4:
                final_random = (final_random + random.choice(SYMBOLS) + 
                random.choice(UPCASE_CHARACTERS) + random.choice(LOCASE_CHARACTERS) +
                random.choice(DIGITS))
                choice_size = 0
            else:
                final_random = final_random + random.choice(COMBINED_LIST)
                choice_size = choice_size - 1
    # If user does not want special characters
    else:
        while(choice_size != 0):
            # Making sure that all outputs have at least one uppercase, one lowercase, and one digit
            if choice_size == 3:
                final_random = (final_random + random.choice(UPCASE_CHARACTERS) + 
                random.choice(LOCASE_CHARACTERS) + random.choice(DIGITS))
                choice_size = 0
            else:
                final_random = final_random + random.choice(PARTIAL_LIST)
                choice_size = choice_size - 1
    return(final_random)




def user_inputs():
    clense_bool_one = 0     # Clensing bool variable
    clense_bool_two = 0
    clense_bool_three = 0 


    # While loop to make sure user input username or password
    while(clense_bool_one == 0):
        choice = input("Would you like to generate a username or password?")
        if choice.lower() == "username" or choice.lower() == "password":
            clense_bool_one = 1
        else:
            print("Invalid input. Please make sure your input is either 'username' or 'password'.")

    # While loop to make sure size of the choice is a positive integer 
    while(clense_bool_two == 0):
        # Try except to make sure the program doesn't crash if user inputs letters
        try:
            size = int(input("How long would you like your", choice, "to be? (Minimum of 4)"))
            clense_bool_two = 1
            # If statement to make sure the number is a positive integer 
            if (size < 4 or size % 1 != 0):
                print("Invalid input. Please make sure yoru input is a positive integer greater than 3.")
                clense_bool_two = 0

        except:
            print("Invalid input. Please make sure your input is a valid number.")

    # While loop to make sure user inputs yes or no
    while(clense_bool_three == 0):
        special_char = input("Would you like for your", choice, "to have special characters? (yes or no)")
        if special_char.lower() == "yes" or special_char.lower() == "no":
            clense_bool_three = 1
        else:
            print("Invalid input. Please make sure your input is either 'yes' or 'no'.")
    
    user_output = password_generator(size, special_char)
    print("Your random", choice, "has been generated and it is", user_output)



if __name__ == "__main__":
    # Welcoming Message
    print("Welcome to the Random Password Generator")
    repeat_bool = 1

    while(repeat_bool == 1):
        user_inputs()
        password_generator()
        repeat_bool = int(input("Would you like to generate another random username/password? (yes = 1, no = 0)"))
    
    print("Thank you for using the Random Password Generator. See you later!")




