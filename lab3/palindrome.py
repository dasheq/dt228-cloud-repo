def is_palindrome(value):
    min = 0
    max = len(value) - 1

    #This program compares the first and last letter of the word 
    #If they're equal, move onto next letter until after passing the middle 
    while True:

        #If all letters checked return true
        if min > max:
            return True;

        a = value[min]
        b = value[max]

        #Return false is characters are not equal.
        if a != b:
            return False;

        #Move to next letter
        min += 1
        max -= 1

words = ["Oxo","OXO","123454321","ROTATOR","12345 54321"]

for word in words:

    if is_palindrome(word):
        print("True: ", word)
    else:
        print("False: ", word)