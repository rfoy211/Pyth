class person:
    def __init__(self) -> None:
        print(self.__dir__())

    # override
    def __str__(self):
        return "your naem is: " + self.name
    
class student(person):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)

student1 =student('a', 12)
print(student1.__str__())