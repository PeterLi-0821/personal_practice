

# Conditions for a strong password
# -minimum of 8 characters
# -atleast 1 digit
# -uppercase and lowercase

import re


lorem = 'smilem4dfsdfdDe'

def testCharactNumb(myPass):
    thePass = re.compile(r'\w{8,}')
    return thePass.search(myPass) != None

def testDigit(myPass):
    thePass = re.compile(r'\d')
    return thePass.search(myPass) != None           # returns true if there is a digit

def testCase(myPass):
    thePass = re.compile(r'[a-z]{1,}')
    thePass2 = re.compile(r'[A-Z]{1,}')
    return thePass.search(myPass) != None and thePass2.search(myPass) != None

while(lorem != 'q'):
    lorem = input("Enter a password: ")
    # print(testCharactNumb(lorem), testDigit(lorem), testCase(lorem))
    if (lorem == 'q'):
        break
    elif (testCharactNumb(lorem) and testDigit(lorem) and testCase(lorem)):
        print('Valid password!')
    else:
        print('Your password must contain, UPPERCASE letters and digits')
    print('(q to quit)\n')
