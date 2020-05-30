class A:
	
	a = None
	c = 3
	b = 2


	@classmethod
	def next(cls):
		cls.a = 123124
		return cls

	def otra_cosa(self):
		print(self.a)



a = A.next()
print(a.a)
ab = A()

ab.otra_cosa()




