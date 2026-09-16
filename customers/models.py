class Customer:

    POINT_RATE = 0.01

    def __init__(self, cus_id, name, phone, points = 0):

        self.cus_id = cus_id
        self.name = name
        self.phone = phone
        self.points = points

    def buy(self, amount):
        add_point = amount * self.POINT_RATE
        self.points += add_point
        return add_point
        
    def __str__(self):
        return f"ID : {self.cus_id} | 이름 : {self.name} | 전화번호 : {self.phone} | 누적 포인트 : {self.points} "


class VIPCustomer(Customer):

    POINT_RATE = 0.05

    def __init__(self, cus_id, name, phone, manager_name, points = 0):
        super().__init__(cus_id, name, phone, points)
        self.manager_name = manager_name

    def __str__(self):
        return super().__str__() + f" | 전담 매니저 : {self.manager_name}"