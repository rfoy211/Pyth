#bai1
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def say_hi(self):
        print(f"Hi, my name is {self.name}.")

    def tell_position(self):
        print(f"I am a {self.position}.")

# Test code
john = Employee("John", "Software Engineer")
john.say_hi()
john.tell_position()
#bai2
import math

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def area(self):
        return self.height * self.width

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius**2

# Main program
shape = input("Shape (rectangle|circle): ")

if shape == "rectangle":
    height = float(input("Height: "))
    width = float(input("Width: "))
    rectangle = Rectangle(height, width)
    print(f"=> Perimeter: {rectangle.perimeter()}")
    print(f"=> Area: {rectangle.area()}")
elif shape == "circle":
    radius = float(input("Radius: "))
    circle = Circle(radius)
    print(f"=> Perimeter: {circle.perimeter()}")
    print(f"=> Area: {circle.area()}")
else:
    print("=> Invalid!")
#bai3
from datetime import datetime

class CustomDate:
    def __init__(self):
        self.now = datetime.now()

    def get_date(self):
        return self.now.strftime("%d/%m/%Y")

    def get_time(self):
        return self.now.strftime("%H:%M:%S")

# Test code
now = CustomDate()
print(now.get_date())
print(now.get_time())
#bai4
from datetime import datetime

class DateHandler:
    @staticmethod
    def format_date(date):
        return date.strftime("%d/%m/%Y")

    @staticmethod
    def get_days_between(date1, date2):
        return (date2 - date1).days

# Test code
start_date = datetime(2021, 1, 1)
end_date = datetime(2022, 1, 1)

print("Start:", DateHandler.format_date(start_date))
print("End:", DateHandler.format_date(end_date))
print("Days between:", DateHandler.get_days_between(start_date, end_date))

