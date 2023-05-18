# Gets the username from user and checks if it is valid or not.
def getUsername():
    
    while True:
        
        username = input("Please enter a username: ")
        
        if len(username) not in range(6, 13):
            print("Please enter username in the allowed length!")

        elif username[0] != 'e':
            print("Please use 'e' at the begining of the username.")

        elif username.isalnum() == False:
            print("Please enter a username that contains only alphanumeric characters.")

        else:
            print("Your username", username, "is VALID.")
            break

    return username

# Gets the password from user and checks if it is valid or not.
def getPassword():

    while True:
        
        password = input("Please enter password: ")

        if len(password) < 8:
            print("Please enter a password in the allowed length!")
        
        else:
            print("Your password is VALID.")
            break

    return password

# These could be done with flag variables too instead of break statement.

getUsername()
getPassword()
