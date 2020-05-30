class Evens:
    def __init__(self, *args):
        if len(args)>1:
            if args[0]%2==0:
                self.val = args[0]
            else:
                self.val = args[0]+1
            self.end = args[1]
        else:
            self.val = 0
            self.end = args[0]

    def __iter__(self):
        return self

    def __next__(self):
        if self.val >= self.end:
            raise StopIteration
        else:
            val = self.val
            self.val += 2
            return val


for i in Evens(5,21):
    print(i)

