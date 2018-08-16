class Tenant_db:
    def __init__(self):
        self.tenants = list()

    def addTenant(self, newTenant):
        self.tenants.append(newTenant)

    def getTenant(self, apartmentNumber):
        for tenant in self.tenants:
            if tenant.getApartmentNumber() == apartmentNumber:
                return tenant.getTenantName()
        return ''

    def countTenants(self):
        return len(self.tenants)

    def removeTenant(self, apartmentNumber):
        
        for tenant in self.tenants:
            if tenant.getApartmentNumber() == apartmentNumber:
                return self.tenants.pop(self.tenants.index(tenant))
        return ''

    def getAllTenants(self):
        return self.tenants

