from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0
    
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().setNombre(nombre)
        super().setEdad(edad)
        super().setHabitat(habitat)
        super().setGenero(genero)
        super().setZona(None)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)
	
    @classmethod
    def cantidadMamiferos(cls):
        cantidadMamiferos = 0
        for i in cls._listado:
            cantidadMamiferos += 1
        return cantidadMamiferos
	
    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        cls.caballos += 1
        return caballo
	
    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        leon = Mamifero(nombre, edad, "selva", genero, True, 4)
        cls.leones += 1
        return leon
        
    def isPelaje(self):
        return self._pelaje
        
    def setPelaje(self, pelaje):
        self._pelaje = pelaje
        
    def getPatas(self):
        return self._patas
        
    def setPatas(self, patas):
        self._patas = patas
	
    @classmethod
    def getListado(cls):
        return cls._listado