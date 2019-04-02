
class foo:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def __call__(self):
        print(self.a, self.b)



d = foo(1,2)
d()
