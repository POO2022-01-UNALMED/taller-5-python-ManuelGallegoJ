from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().setNombre(nombre)
        super().setEdad(edad)
        super().setHabitat(habitat)
        super().setGenero(genero)
        super().setZona(None)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)
	
    @classmethod
    def cantidadAnfibios(cls):
        cantidadAnfibios = 0
        for i in cls._listado:
            cantidadAnfibios += 1
        return cantidadAnfibios
        
    def movimiento():
        return "saltar"
	
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        cls.ranas += 1
        return rana
	
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.salamandras += 1
        return salamandra
        
    def getColorPiel(self):
        return self._colorPiel
        
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def isVenenoso(self):
        return self._venenoso
        
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
	
    @classmethod
    def getListado(cls):
        return cls._listado