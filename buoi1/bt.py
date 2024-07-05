class counter:
    def __init__(self):
        self.count = 0

    def tick(self):
        self.count += 1

    def reset(self):
        self.count = 0

counter = counter()
print(counter.count)
counter.tick()
print(counter.count)
counter.reset()
print(counter.count)