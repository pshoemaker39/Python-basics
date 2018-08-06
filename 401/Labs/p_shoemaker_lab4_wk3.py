def getAlphaPhoneNumber():
    target = ''
    retry = False
    while (len(target) < 7):
        if retry == True:
            target = str(input("Please try agin. Enter at least 7 characters alphabetic phone number or press Enter to exit: ")).lower().replace(' ','')[0:7]      
        else:
            target = str(input("Please enter an alphabetic phone number or press Enter to exit: ")).lower().replace(' ','')[0:7]
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
        if(letter in value):
            print('found', letter)
            return str(key)
        else:
            print('not found', letter)
            return str(letter)

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
    if target == '':
        quit
    else:
        print(createPhoneNumber(target))

## MENU OPT 1
phoneNumberConverter()