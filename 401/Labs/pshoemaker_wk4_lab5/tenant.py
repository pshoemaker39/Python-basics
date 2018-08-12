import random

class Tenant:
#Getter methods only
    def __init__(self,firstName, lastName, apartmentNumber):
        self.tenant_fName = firstName
        self.tenant_lName = lastName
        self.tenant_aptNum = apartmentNumber
        self.tenant_id = random.randint(1000,9999)

    

    




    
