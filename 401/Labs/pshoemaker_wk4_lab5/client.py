from apartment import Apartment as Apt
from  apartment_db import Apartment_db as AptDB
from tenant import Tenant as Tnt
from tenant_database import Tenant_db as TenantDB

apartmentDataFile = 'apartment_data.txt'

options = {
    '1': 'Rent/Lease Apartment',
    '2': 'Search Available Apartments',
    '3': 'Make Apartment Available',
    '4': 'List Available Apartments',
    '5': 'List Rented Apartments',
    '6': 'Display Tenant Information',
    '7': 'Add New Apartment',
    '8': 'Exit'
}

def displaySearchResults(results):
    print("| Apartment Number | Bedrooms | Bathrooms | Rent |")
    for apt in results:
        print("| ", apt.getApartmentNumber()," | ", apt.getApartmentBedrooms(), " | ", apt.getApartmentBathrooms(), " | ", apt.getApartmentRent()," |")

def rentLeaseApartment(db, tdb):
    print("\n")
    minBeds = float(input("Please enter the minimum beds: "))
    print("\n")
    minBaths = float(input("Please enter the minimum baths: "))
    print("\n")
    maxRent = float(input("Please enter the maximum rent: "))
    print("\n")
    reqStatus = 'A'
    
    results = db.searchDb(minBeds, minBaths, maxRent, reqStatus)

    if len(results) > 0:
        print("******** Available Apartments ********************")
        displaySearchResults(results)
        print("\n******** End Available Apartments ****************\n")
        targetApt = str(input("Enter an apartment number to rent it, or enter -1 to exit"))

        if (targetApt == '-1'):
            return
        else:
            fName = str(input("\n\nPlease enter your first name: "))
            lName = str(input("\n\nPlease enter your last name:"))

            newTnt = Tnt(fName, lName, targetApt)

            db.getApartment(targetApt).setApartmentStatus('R')

    else:
        print("******** No Matching Apartments ********************")


    
    
    
    
    pass

def searchAvailableApartments(db, tdb):
    print("\n")
    minBeds = float(input("Please enter the minimum beds: "))
    print("\n")
    minBaths = float(input("Please enter the minimum baths: "))
    print("\n")
    maxRent = float(input("Please enter the maximum rent: "))
    print("\n")
    reqStatus = 'A'
    
    results = db.searchDb(minBeds, minBaths, maxRent, reqStatus)

    if len(results) > 0:
        print("******** Available Apartments ********************")
        displaySearchResults(results)
        print("\n******** End Available Apartments ****************")
    else:
        print("******** No Available Apartments ********************")
    pass

def makeApartmentAvailable(db, tdb):
    
    aptNum = str(input("\nPlease enter an apartment number:"))

    targetApt = db.getApartment(aptNum)

    if len(targetApt) == 0:
        print("******** No Apartments Match Specified Number ******")
        return

    if (targetApt.getApartmentStatus() == 'A'):
        print("***** Apartment Matching Specified Number Already Available ****")
        return
    else:
        targetApt.setApartmentStatus('A')
        tdb.removeTenant(aptNum)
        print("**** Tenant at ", aptNum, " removed. *****")

    pass

def listAvailableApartments(db, tdb):
    
    results = db.getAvailApartments()

    if len(results) > 0:
        print("******** Available Apartments ********************")
        displaySearchResults(results)
        print("\n******** End Available Apartments ****************")
    else:
        print("******** No Available Apartments ********************")
    pass

def listRentedApartments():
    print('Selected List Rented Apartments')
    pass

def displayTenantInformation():
    print('Selected Display Tenant Information')
    pass

def addNewApartment(db, tdb):
    print("\n")
    number = str(input("Please enter the apartment number: "))
    print("\n")
    beds = float(input("Please enter the number of beds: "))
    print("\n")
    baths = float(input("Please enter the number of baths: "))
    print("\n")
    rent = float(input("Please enter the rent: "))
    print("\n")
    status = 'A'    

    newApt = Apt(number, beds, baths, rent, status)

    db.addApartment(newApt)

    print('**** Apartment Added *****')

    pass

def quitMenu():
    print('Done')
    quit()

def optionSelector(option, db, tdb):
    switcher = {
        '1': rentLeaseApartment,
        '2': searchAvailableApartments,
        '3': makeApartmentAvailable,
        '4': listAvailableApartments,
        '5': listRentedApartments,
        '6': displayTenantInformation,
        '7': addNewApartment,
        '8': quitMenu
    }
    switch = switcher.get(option)
    switch(db, tdb)

def menuController(dataFile):
    db = AptDB()
    tdb = TenantDB()
    db.loadApartments(dataFile)

    while True:

        print('\n\nMenu options:')
        
        for option, title in options.items():
            print(option, ' ', title)
        
        menuOption = str(input('Choice? '))

        optionSelector(menuOption, db, tdb)

        print('\n\n')


menuController(apartmentDataPath)

