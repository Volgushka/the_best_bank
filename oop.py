class Example:
    st1 = 10
    st2 = 20
    
    def __init__(self):
        self.d1 = 5
        self.d2 = 6

    def f1(self):
        d3 = 'hi'
        print(d3)

    def f2(self):
        self.d2 = Example.st1 + Example.st2
        print (self.d2)

    def f3(self):
        print (self.d1**self.d2)

ex = Example()
ex.f1()
ex.f2()
ex.f3()