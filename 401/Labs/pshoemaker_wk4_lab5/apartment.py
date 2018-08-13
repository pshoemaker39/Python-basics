class Apartment:
    def __init__(self, apartmentNumber, beds, baths, rent, status):
        self.apt_num = apartmentNumber
        self.apt_bedrm = beds
        self.apt_rent = rent
        self.apt_status = status

    def setApartmentNumber(self, apartmentNumber):
        self.apt_num = apartmentNumber

    def getApartmentNumber(self):
        return self.apt_num

    def setApartmentBedrooms(self, beds):
        self.apt_bedrm = beds

    def getApartmentBedrooms(self):
        return self.apt_bedrm

    def setApartmentRent(self, rent):
        self.apt_rent = rent
    
    def getApartmentRent(self):
        return self.apt_rent

    def setApartmentStatus(self, status):
        self.apt_status = status
    
    def getApartmentStatus(self):
        return self.apt_status