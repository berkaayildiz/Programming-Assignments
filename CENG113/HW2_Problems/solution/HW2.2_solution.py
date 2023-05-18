# Counts the char number in text.
def countChar(string):
    count = 0
    
    for i in string:
        if i == char:
            count += 1
    
    return count

text = input("Write your text: ") 
char = input("Write your special character: ")

# Checks if the given input is valid or not.

while len(char) != 1:
    char = input("Please enter a valid character: ")

print("We have found", countChar(text), f"special character '{char}' !")
