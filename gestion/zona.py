class Zona:
    def __init__(self, nombre, zoo = None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []
        
    def agregarAnimales(self, nuevoAnimal):
        nuevoAnimal.setZona(self)
        self._animales.append(nuevoAnimal)
        
    def cantidadAnimales(self):
        cantidadAnimales = 0
        for i in self._animales:
            cantidadAnimales += 1
        return cantidadAnimales
        
    def getNombre(self):
        return self._nombre
        
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def getZoo(self):
        return self._zoo
    
    def setZoo(self, zoo):
        self._zoo = zoo
        
    def getAnimales(self): 
        return self._animales