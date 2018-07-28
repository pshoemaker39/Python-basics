def getDivisors():
    target = int(input('Please enter a positive integer: '))
    resultSet = []

    #For each integer through the target
    for i in range(1, target, 1):
        #If the target is dividble by the current integer, append that integer to the result
        if( (target % i) == 0 ):
            resultSet.append(i)

    print(resultSet)


#Add definition for vowelCount function
def vowelCount():
    target = str(input('Please enter a string: ')).lower()

    vowels = ['a', 'e', 'i', 'o', 'u']
    resultSet = [0, 0, 0, 0, 0]
    
    #For each letter in the target string
    for i in target:
        #If letter appears in the vowels list
        if(i in vowels):
            #Increment the appropriate counter within the result
            resultSet[vowels.index(i)] += 1

    print('a, e, i, o, and u appear, respectively, {}, {}, {}, {}, {} times.'.format(
        resultSet[0], 
        resultSet[1],
        resultSet[2],
        resultSet[3],
        resultSet[4]
        ))
        
#Add definition for rps function

def rps(p1, p2):

    choices = ['R', 'P', 'S']
    choiceValues = [2, 3, 5]

    #Assign the corresponding prime numbers to the user input
    p1 = choiceValues[choices.index(p1)]
    p2 = choiceValues[choices.index(p2)]

    if ( ( p1 * p2 ) == 6 ):
        # R&P | P&R - Higher number (Paper) wins
        print (-1 if ( p1 > p2) else 1)

    elif ( ( p1 * p2 ) == 10 ):
        # R&S | S&R - Lower number (Rock) wins
        print (-1 if ( p1 < p2) else 1)

    elif ( ( p1 * p2 ) == 15 ):
        # P&S | S&P - Higher number (Scissors) wins
        print (-1 if ( p1 > p2) else 1)
    
    else:
        #Draw
        print(0)


#Add definition for sublist function

def getLists(l1, l2):
    currentIndex = -1
    
    #For each element in list 1
    for l in l1:

        #If element exists in list 2
        if(l in l2):

            #Shift index placeholders
            previousIndex = currentIndex
            currentIndex = l2.index(l)

            if(previousIndex > currentIndex):
                #If previsous element index is greater than current element index
                #List element out of order
                return False
        
        else:
            #List element not found in larger list
            return False
    
    #Elements found in order
    return True

def strToLst(s):
    #Convert string list to actual list
    return s.replace('[','').replace(']','').replace(' ', '').split(',')



def labMenu():
    print('Enter 1 for Problem 3.29')
    print('Enter 2 for Problem 4.25')
    print('Enter 3 for Problem 5.26')
    print('Enter 4 for Problem 5.48')
    print('Enter 5 to exit the program')

done = False

while not done:
    labMenu()
    choice = int(input('Please make an entry: '))

    if choice == 1:

        getDivisors()

        #Prompt the user for a positive integer
        #Add code for Problem 3.29

    elif choice == 2:

        vowelCount()


        #Add code for Problem 4.25
          #Prompt the user for a string
          #Call vowelCount function and pass the string as an argument
        pass
    elif choice == 3:

        p1 = str(input('Player 1 - (R)ock, (P)aper, (S)cissors? ')).upper()
        p2 = str(input('Player 2 - (R)ock, (P)aper, (S)cissors? ')).upper()

        rps(p1, p2)


        #Add code for Problem 5.26
          #Prompt prompt for players 1 and 2 choices. 'R', 'P', or 'S' should be entered for each player
          #Call the rps function and pass the players choices.  The function should return 1, -1, or 0
          #Print the return value of the function
        pass
    elif choice == 4:

        l1 = input('List 1: ')
        l2 = input('List 2: ')

        l1 = strToLst(l1)
        l2 = strToLst(l2)


        # [15, 1, 100]
        # [20, 15, 30, 50, 1, 100]
        # [15, 50, 20]

        print(getLists(l1, l2))

        ### User provides lists
        ### Find the index of each number and compare indicies


        #Add code for Problem 5.48
        # Prompt the user for two lists
        # Call sublist function and pass the two lists as arguments
        pass
    elif choice == 5:
        done = True