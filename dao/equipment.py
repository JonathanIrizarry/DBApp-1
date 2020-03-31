#hardcoded DB entries, just for Phase 1, remove later!
rows, columns = (6, 5)
EquipDB = [[0 for x in range(rows)] for y in range(columns)]
EquipDB[0] = [1, 'Generator', 'Wal-Mart', 'Yamaha', 5, 'San Juan']
EquipDB[1] = [2, 'Tools', 'Amazon', 30, 'Dewalt', 'San Juan']
EquipDB[2] = [3, 'Tools', 'Jonathan', 'Bosch', 3, 'Mayaguez']
EquipDB[3] = [4, 'Generator', 'Angel', 'Powerlite', 1, 'Mayaguez']
EquipDB[4] = [5, 'Generator', 'Gilson', 'Powerlite', 1, 'Mayaguez']

class EquipDAO:

    def getAllEquip(self):
        result = "This is a list of equipment"
        return result

    def getEquipByID(self, eid):
        result = "Equipment with specified id"
        return result

    def getEquipByType(self, etype):
        result = []
        for row in EquipDB:
            for col in row:
                if col[2] == etype:
                    result.append(row)
        return result

    def getEquipBySupplier(self, esupplier):
        result = []
        for row in EquipDB:
            for col in row:
                if col[2] == esupplier:
                    result.append(row)
        return result

    def getEquipByBrand(self, ebrand):
        result = []
        for row in EquipDB:
            for col in row:
                if col[2] == ebrand:
                    result.append(row)
        return result

    def getEquipByQuantity(self, equantity):
        result = []
        for row in EquipDB:
            for col in row:
                if col[2] == equantity:
                    result.append(row)
        return result

    def getEquipByLocation(self, elocation):
        result = "Equipment with given location"
        return result

    #fuid entry only for phase 1 for examples
    #Remove fuid for CRUD operations for later phases!
    #Must return the primary key as well
    def insert(self, eid, etype, esupplier, ebrand, equantity, elocation):
        result = "Equipment inserted"
        return result

    def delete(self, eid):
        result = "Equipment deleted"
        return result

    def update(self, eid, etype, esupplier, ebrand, equantity, elocation):
        EquipDB.append(eid, etype, esupplier, ebrand, equantity, elocation)
        return eid