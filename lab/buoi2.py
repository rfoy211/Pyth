class MathList:
    def __init__(self, values) -> None:
        self.values = values
        self.length = len(values)

    def __str__(self) -> str:
        return str(self.values)
    
    def __add__ (self, num):
        for i in range(len(self.values)):
            self.values[i] -= num
            return self
        
list_a = MathList([1,2,3])
print(list_a)
list_a += 2
print(list_a)

#bai3
class Square:
    def __init__(self, edge) -> None:
        self.edge = edge

    def cal_area(self):
        return self.edge**2
    
class cube(Square):
    def __init__(self, edge) -> None:
        super().__init__(edge)

    def cal_volume(self):
        return self.edge**3
    
    def cal_area(self):
        return 6 * self.edge**2
    
# driver code
Square_1 = Square(4)
cube_1 = cube(4)
print(cube_1.cal_area())

#bai4
class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def welcome(self):
        print("welcome", self.username)

    def checkPassword(self, passInput):
        return passInput == self.password
    
from datetime import datetime
class subscribedUser(User):
    def __init__(self, username, password, expiredDate) -> None:
        super().__init__(username, password)
        self.expiredDate = expiredDate

    def isExpired(self):
        return datetime.now() > self.expiredDate
    
# dirve code
user1 = subscribedUser('phong', '2908', datetime(2024, 8, 29))
user1.welcome()
print(user1.checkPassword('789'))
print(user1.isExpired())
    
