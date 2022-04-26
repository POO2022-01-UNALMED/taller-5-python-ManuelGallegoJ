class Zoologico:
    
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []
        
    def agregarZonas(self, nuevaZona):
        nuevaZona.setZoo(self)
        self._zonas.append(nuevaZona)
        
    def cantidadTotalAnimales(self):
        totalAnimales = 0
        for i in self._zonas:
            totalAnimales += i.cantidadAnimales()
        return totalAnimales
        
    def getNombre(self):
        return self._nombre
        
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def getUbicacion(self):
        return self._ubicacion
        
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
        
    def getZona(self):
        return self._zonas