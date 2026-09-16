
from models import Customer, VIPCustomer


class CRM:

    def __init__(self):
        self.customers = []


    def register_customer(self, cus_id, name, phone):
        cus = Customer(cus_id, name, phone)
        self.customers.append(cus)
        return cus

    def register_VIP(self, cus_id, name, phone, manager_name):
        cus = VIPCustomer(cus_id, name, phone, manager_name)
        self.customers.append(cus)
        return cus

    def find_cusotmer(self, cus_id):
        for cus in self.customers:
            if cus.cus_id == cus_id:
                return cus

    def find_all_customer(self):
        return self.customers

    def find_VIP(self):
        return [cus for cus in self.customers if isinstance(cus, VIPCustomer)]

    def update_phone(self, cus_id, new_phone):
        cus = self.find_cusotmer(cus_id)

        cus.phone = new_phone
        return cus

    def remove(self, cus_id):
        cus = self.find_cusotmer(cus_id)
        self.customers.remove(cus)

    def buy(self, cus_id, amount):
        cus = self.find_cusotmer(cus_id)
        return cus.add(amount)
