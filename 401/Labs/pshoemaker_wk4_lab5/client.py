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
    '5': 'List Rented/Leased Apartments',
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
        targetApt = str(input("Enter an apartment number to rent it ( or enter -1 to exit ):   "))

        if (targetApt == '-1'):
            return
        else:
            fName = str(input("\nPlease enter your first name: "))
            lName = str(input("\nPlease enter your last name: "))

            newTnt = Tnt(fName, lName, targetApt)
            tdb.addTenant(newTnt)

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
    
    aptNum = str(input("\nPlease enter an apartment number: "))

    targetApt = db.getApartment(aptNum)

    if targetApt == None:
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

def listRentedApartments(db, tdb):
    targetApts = db.getRentedApartments()
    targetTnts = tdb.getAllTenants()
    results = []

    

    for apt in targetApts:
        aptNum = apt.getApartmentNumber()
        
        result =[
            aptNum, 
            apt.getApartmentBedrooms(),
            apt.getApartmentBathrooms(),
            apt.getApartmentRent()
            ]

        

        for tnt in targetTnts:
            print(tnt.getApartmentNumber(), aptNum)
            if tnt.getApartmentNumber() == aptNum:
                result.append(tnt.getTenantId())
                result.append(tnt.getTenantName())
        
        results.append(result)

    
    print("\n\n******** Occupied Apartments With Documented Tenants ******************")
    print("| Apartment Number | Bedrooms | Bathrooms | Rent | Tenant Id | Tenant Name |")        
    for r in results:
        if len(r) > 4:
            print("| ", r[0]," | ", r[1], " | ", r[2], " | ", r[3]," | ", r[4]," | ", r[5]," |")
    print("******** End Occupied Apartments With Documented Tenants *****************")

    print("******** Occupied Apartments Without Documented Tenants ******************")
    print("| Apartment Number | Bedrooms | Bathrooms | Rent |")        
    for r in results:
        if len(r) < 5:
            print("| ", r[0]," | ", r[1], " | ", r[2], " | ", r[3]," |")
    print("******** End Occupied Apartments Without Documented Tenants *****************")        
            


    pass

def displayTenantInformation(db, tdb):
    aptNum = str(input("\nPlease enter an apartment number: "))

    targetApt = db.getApartment(aptNum)
    
    if targetApt.getApartmentStatus() == 'R':
        targetTnt = tdb.getTenant(targetApt.getApartmentNumber())
        if targetTnt == '': 
            print("\nThe current tenant at ", targetApt.getApartmentNumber(), " is not documented.")
        else:
            print("\nThe current tenant at ", targetApt.getApartmentNumber(), " is ", targetTnt.getTenantName())
        
    elif targetApt.getApartmentStatus() == 'A':
        print("\nThis apartment is currently available for rent.")

    else:
        print("\nNo apartment found with this number.")

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

def quitMenu(db, tdb):
    
    print('\n************* Apartment Metrics ***************')
    print('\nTotal Number of Apartments: ', db.getTotalApartments())
    print('\nTotal Number of Apartments Leased: ', db.getTotalRented())
    print('\nTotal Number of Apartments Available: ', db.getTotalAvailable())
    print('\nTotal Number of Tenants: ', tdb.countTenants())
    print('\n************* End Apartment Metrics ***********')
    
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

    print('\n\n\n\n\n\n')

    while True:

        print('\n\nMenu options:')
        
        for option, title in options.items():
            print(option, ' ', title)
        
        menuOption = str(input('Choice? '))

        optionSelector(menuOption, db, tdb)

        print('\n\n')


menuController(apartmentDataFile)

