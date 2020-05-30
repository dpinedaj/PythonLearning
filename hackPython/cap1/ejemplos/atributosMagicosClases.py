class ClaseB:
    def __new__(cls):
        print("Creando una Instancia")

        return super(ClaseB, cls).__new__(cls)
    def __init__(self):
        self.name = __class__.__name__
        self.doc = __class__.__doc__

    def __del__(self):
        pass
    def __repr__(self):  #Permite que al imprimir el objeto, se obtenga el string de este método
        pass
    def __add__(self, other): #Permite agregar un string o algo al objeto de clase al llamarlo
        pass
    def __str__(self):
        pass
    
