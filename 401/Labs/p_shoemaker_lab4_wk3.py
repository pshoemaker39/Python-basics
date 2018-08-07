import random

###### BEGIN PROBLEM ONE - PHONE NUMBER CONVERSION #######################

def getAlphaPhoneNumber():
    target = ''
    retry = False
    while (len(target) < 7):
        if retry == True:
            target = str(input("\nPlease try agin. Enter at least 7 characters alphabetic phone number or press Enter to exit: ")).lower().replace(' ','')[0:7]      
        else:
            target = str(input("\nPlease enter an alphabetic phone number or press Enter to exit: ")).lower().replace(' ','')[0:7]
        
        retry = True

        if(target == ''):
            return target

    return target


def getNumber(letter):

    lookup = {
        2:['a','b','c'],
        3:['d','e','f'],
        4:['g','h','i'],
        5:['j','k','l'],
        6:['m','n','o'],
        7:['p','q','r','s'],
        8:['t','u','v'],
        9:['w','x','y','z']
    }

    for key, value in lookup.items():
        if letter in value:
            return(str(key))
    return(str(letter))

def createPhoneNumber(target):
    result = []
    
    for letter in target:
        
        if len(result) == 3:
            result.append('-')
            result.append(getNumber(letter))
        else:
            result.append(getNumber(letter))

    return(''.join(result))

def phoneNumberConverter():
    target = getAlphaPhoneNumber()

    while target != '':
        print('\n', createPhoneNumber(target), '\n')
        target = getAlphaPhoneNumber()
    return ''


###### END PROBLEM ONE - PHONE NUMBER CONVERSION #######################


###### BEGIN PROBLEM TWO - MAGIC NUMBER CALCULATOR #######################

def createTwoDimensionalList():
    twoDList = []
    i = 0
    while i < 3:
        subList = [random.randrange(1,9), random.randrange(1,9), random.randrange(1,9)]
        twoDList.append(subList)
        i += 1
    return twoDList

def displayTwoDimensionalList(targetList):
    print('\n', "Target: ",'\n')
    for l in targetList:
        print(l)
    print('\n')

def getMagicNumber(targetList):
    magicNumber = 0
    for l in targetList:
        magicNumber += sum(l)
    magicNumber = magicNumber / 3
    print('\n', "The magic number is: ", magicNumber, '\n')
    return magicNumber

def checkRows(targetList, magicNumber):
    return (sum(targetList[0]) == magicNumber) and (sum(targetList[1]) == magicNumber) and (sum(targetList[2]) == magicNumber)

def checkCols(targetList, magicNumber):
    c1 = 0
    c2 = 0
    c3 = 0
    for l in targetList:
        c1 += l[0]
        c2 += l[1]
        c3 += l[2]

    return ((c1 == magicNumber) and (c2 == magicNumber) and (c3 == magicNumber))

def checkDiags(targetList, magicNumber):
    d1 = targetList[0][0] + targetList[1][1] + targetList[2][2]
    d2 = targetList[2][0] + targetList[1][1] + targetList[0][2]

    return ((d1 == magicNumber) and (d2 == magicNumber))

def magicSquareEvaluator(forceTrue=False):
    if forceTrue:
        targetList = [[2,7,6],[9,5,1],[4,3,8]]
    else:
        targetList = createTwoDimensionalList()
    displayTwoDimensionalList(targetList)
    magicNumber = getMagicNumber(targetList)
    magicSquare = (checkRows(targetList, magicNumber) and checkCols(targetList, magicNumber) and checkDiags(targetList, magicNumber))
    return magicSquare

def magic():
    magicSquare = magicSquareEvaluator()
    if magicSquare == True:
        print("\n This IS a magic square. \n")
        return ''
    else:
        print("\n This IS NOT a magic square. \n")
        ask = str(input("\n Enter [Y] to see an actual magic square or [N] to return to the main menu. \n")).lower().replace('[','').replace(']','')
        if ask == 'y':
            magicSquare = magicSquareEvaluator(True)
            print("\n This IS a magic square. \n")
            return ''
        else:
            return ''

    




###### END PROBLEM TWO - MAGIC NUMBER CALCULATOR #######################


def menu():

    inputQuery = '\n Enter [1] for phone nunmber conversions. \n Enter [2] for magic number calculator. \n Enter [3] to quit. \n \n'
    target = str(input(inputQuery))
    while target != '3':
        if target == '1':
            target = phoneNumberConverter()
        
        elif target == '2':
            target = magic()

        else:
            target = str(input(inputQuery))
            if target == '3':
                quit

    quit

menu()