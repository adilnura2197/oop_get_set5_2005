class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.__ram = ram

    @property
    def ram(self):
        return self.__ram


    @ram.setter
    def ram(self, new_ram):
        self.__ram = new_ram


l1 = Laptop('HP', 8)

res = l1.ram
print(res)

l1.ram = 16
print(l1.ram)
