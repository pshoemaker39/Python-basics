import apartment as Apt
from  apartment_db import Apartment_db as AptDB
import tenant as Tenant
from tenant_database import Tenant_db as TenantDB

apartmentDataPath = 'apartment_data.txt'

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

def rentLeaseApartment():
    # print("\n")
    # beds = float(input("Please enter the numnber of beds: "))
    # print("\n")
    # baths = float(input("Please enter the numnber of baths: "))

    pass




def searchAvailableApartments():
    print('Selected Search Available Apartments')
    pass

def makeApartmentAvailable():
    print('Selected Make Apartment Available')
    pass

def listAvailableApartments():
    print('Selected List Available Apartments')
    pass

def listRentedApartments():
    print('Selected List Rented Apartments')
    pass

def displayTenantInformation():
    print('Selected Display Tenant Information')
    pass

def addNewApartment():
    print('Selected Add New Apartment')
    pass

def quitMenu():
    print('Done')
    quit()

def optionSelector(option):
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
    switch()

def menuController(dataFile):
    db = AptDB()

    db.loadApartments(dataFile)

    while True:

        print('\n\nMenu options:')
        
        for option, title in options.items():
            print(option, ' ', title)
        
        menuOption = str(input('Choice? '))

        optionSelector(menuOption)

        print('\n\n')


menuController(apartmentDataPath)

