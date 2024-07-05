class animal:
    name = 'abc'
    age = 0.5

    def __init__(self, name):
        self.name = name

    def talk():
        print('talk')
cuu = animal(name="xyz")

print(cuu.name)
cuu.talk()