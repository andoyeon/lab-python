class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def info(self):
        print('width:', self.width, 'height:', self.height)


    def area(self):
        return self.width * self.height


r1 = Rectangle(1,2)
r1.info()
print(r1.area())

r2 = Rectangle(width=1, height=2)
r2.info()

