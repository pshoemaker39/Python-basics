from apartment import Apartment as Apt

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
            if apartment.getApartmentStatus().strip() == 'A':
                available.append(apartment)
        return available

    def getRentedApartments(self):
        rented = []
        for apartment in self.apartments:
            if apartment.getApartmentStatus().strip() == 'R':
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
    
    def getTotalRented(self):       
        return len(Apartment_db.getRentedApartments())

    def loadApartments(self, file):
        data = open(file, "r")
        for line in data.readlines():
            #print("\nRead Line:\n",line,"\n")
            line = line.split(' ')
            newApt = Apt(line[0], float(line[1]), float(line[2]), float(line[3]), line[4])
            self.apartments.append(newApt)

    def getAllApartments(self):
        return self.apartments

    def searchDb(self, minBeds, minBaths, maxRent, reqStatus):
        results = []
        for apt in self.apartments:
            if (
                (apt.getApartmentBathrooms() >= minBaths) &
                (apt.getApartmentBedrooms() >= minBeds) &
                (apt.getApartmentRent() <= maxRent) &
                (apt.getApartmentStatus().strip() == reqStatus)
            ):
                results.append(apt)
        return results


