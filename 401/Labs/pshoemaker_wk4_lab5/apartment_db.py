class Apartment_db:
    def __init__(self):
        self.apartments = list()

    def addApartment(self, apartment):
        self.apartments.append(apartment)

    def getApartment(self, apartmentNumber):
        ## this could run forever as written
        for apartment in self.apartments:
            if apartment.getApartmentNumber() == apartmentNumber:
                return apartment

    def getAvailApartments(self):
        available = []
        for apartment in self.apartments:
            if apartment.getApartmentStatus() == 'A':
                available.append(apartment)
        return available

    def getRentedApartments(self):
        rented = []
        for apartment in self.apartments:
            if apartment.getApartmentStatus() == 'R':
                rented.append(apartment)
        return rented

    def changeApartmentStatus(self, apartmentNumber, status):
        ## this could run forever as written
        for apartment in self.apartments:
            if apartment.getApartmentNumber() == apartmentNumber:
                apartment.setApartmentStatus(status)

    def getTotalApartments(self):
        return len(self.apartments)

    def getTotalAvailable(self):
        return len(Apartment_db.getAvailApartments())
    
    def getTotalRented():       
        return len(Apartment_db.getRentedApartments())
