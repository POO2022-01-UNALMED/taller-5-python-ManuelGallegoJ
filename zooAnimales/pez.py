from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().setNombre(nombre)
        super().setEdad(edad)
        super().setHabitat(habitat)
        super().setGenero(genero)
        super().setZona(None)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)
	
    @classmethod
    def cantidadPeces(cls):
        cantidadPeces = 0
        for i in cls._listado:
            cantidadPeces += 1
        return cantidadPeces
        
    def movimiento():
        return "nadar"
	
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        cls.salmones += 1
        return salmon
	
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        cls.bacalaos += 1
        return bacalao
        
    def getColorEscamas(self):
        return self._colorEscamas
        
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas
        
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas
	
    @classmethod
    def getListado(cls):
        return cls._listado