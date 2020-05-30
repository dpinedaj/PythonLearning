class A:

    def testFunction(self):
        try:
            for i in range(10):
                print(i)
            1/0
        except Exception as e:
            print(str(e))
a = 'A()'


b = eval(a)
b.testFunction()
