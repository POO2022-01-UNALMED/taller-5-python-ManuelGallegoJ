from zooAnimales.animal import Animal

class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().setNombre(nombre)
        super().setEdad(edad)
        super().setHabitat(habitat)
        super().setGenero(genero)
        super().setZona(None)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)
	
    @classmethod
    def cantidadAves(cls):
        cantidadAves = 0
        for i in cls._listado:
            cantidadAves += 1
        return cantidadAves
        
    def movimiento():
        return "volar"
	
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        halcon = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        cls.halcones += 1
        return halcon
	
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        cls.aguilas += 1
        return aguila
        
    def getColorPlumas(self):
        return self._colorPlumas
        
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
	
    @classmethod
    def getListado(cls):
        return cls._listado