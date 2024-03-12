#functions
# - consists of function name, parameters.
# - starts "def" keyword.
# - optimizes and make a block of code reusable.
"""
#void function
def averageOfThreeNumbers(num1,num2,num3):
    #codes... 
    average = (num1+ num2 + num3) / 3
    print("Average: ", average)

    averageOfThreeNumbers(89,76,81) """

#return function
title = "ang alamat ni loudie"
title2 = ": Bagsakan Era"

def stringToTitle(title):
    return title.title()

def stringToUpperCase(message):
    return message.upper()

def stringToLowerCase(message):
    return message.lower()

def joinString(message,message2):
    return message.join(message2)

def countLetters(message):
    return len(message)

print(stringToTitle(title))
print(stringToUpperCase(title))
print(stringToLowerCase(title))
# print(joinString(title,title2))
print(countLetters(title))




