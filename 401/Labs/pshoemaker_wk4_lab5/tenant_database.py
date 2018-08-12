class Tenant_db:
    def __init__(self):
        self.tenants = list()

    def addTenant(self, newTenant):
        self.tenants.append(newTenant)

    def getTenant(self, apartment):
        