import random

class Tenant:
#Getter methods only
    def __init__(self,firstName, lastName, apartmentNumber):
        self.tenant_fName = firstName
        self.tenant_lName = lastName
        self.tenant_aptNum = apartmentNumber
        self.tenant_id = random.randint(1000,9999)

    def getApartmentNumber(self):
        return self.tenant_aptNum

    def getTenantName(self):
        return self.tenant_fName + ' ' + self.tenant_lName

    




    
