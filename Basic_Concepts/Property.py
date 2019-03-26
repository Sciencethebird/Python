
class Birb:

    def __init__(self, name, seeb):

        self.name = name;
        self.seeb = seeb;
    
    @property # turns this function into property
    def data(self, addtxt = ''):
        return "{} {} {}".format(self.name, self.seeb, addtxt)

    @data.setter
    def data(self, input):
        self.name, self.seeb = input.split(" ")

    @data.deleter
    def data(self):
        print("deleted!")
        self.name = None
        self.seeb = None


b1 = Birb("science", "almond")

print(b1.data)
b1.data = "sci weed"
print(b1.data)

del b1.data
print(b1.data)