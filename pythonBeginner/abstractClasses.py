import abc

class MyAbstractClass(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def alguna_funcion(self):
        pass

    
    @staticmethod
    @abc.abstractmethod
    def algun_static_method():
        pass

    

    
    @classmethod
    @abc.abstractmethod
    def algun_class_method(cls):
        pass



class MyClass(MyAbstractClass):

    def alguna_funcion(self):
        print('funciona')

    @staticmethod
    def algun_static_method():
        print('funciona static')

    @classmethod
    def algun_class_method(cls):
        print('funciona class method')



a = MyClass()
a.alguna_funcion()
a.algun_class_method()

MyClass.algun_static_method()