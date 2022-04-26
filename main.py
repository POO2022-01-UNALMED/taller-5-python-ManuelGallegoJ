from gestion.zona import Zona
from gestion.zoologico import Zoologico 
from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
from zooAnimales.animal import Animal

zoo = Zoologico("Zoologico Central", "Chicago")

z1 = Zona("zona1")

z2 = Zona("zona2")

zoo.agregarZonas(z1)
zoo.agregarZonas(z2)

z1.agregarAnimales(Mamifero.crearCaballo("test", 11, "M"))
z1.agregarAnimales(Mamifero.crearCaballo("test", 11, "M"))
z1.agregarAnimales(Mamifero.crearLeon("test", 11, "M"))
z1.agregarAnimales(Ave.crearHalcon("test", 11, "M"))
z1.agregarAnimales(Ave.crearHalcon("test", 11, "M"))
z1.agregarAnimales(Ave.crearAguila("test", 11, "M"))
z1.agregarAnimales(Ave.crearAguila("test", 11, "M"))
z1.agregarAnimales(Anfibio.crearRana("test", 11, "M"))

z2.agregarAnimales(Anfibio.crearSalamandra("test", 11, "M"))
z2.agregarAnimales(Reptil.crearIguana("test", 11, "M"))
z2.agregarAnimales(Reptil.crearSerpiente("test", 11, "M"))
z2.agregarAnimales(Pez.crearSalmon("test", 11, "M"))
z2.agregarAnimales(Pez.crearBacalao("test", 11, "M"))

Mamifero.crearCaballo("test", 11, "M")
Ave.crearHalcon("test", 11, "M")
Anfibio.crearRana("test", 11, "M")
Reptil.crearIguana("test", 11, "M")
Pez.crearBacalao("test", 11, "M")

print(zoo.cantidadTotalAnimales() == 13)
print(zoo.getZona()[0].cantidadAnimales() == 8)
print(Mamifero.caballos == 3 and Mamifero.leones == 1)
print(Ave.aguilas == 2 and Ave.halcones ==3)
print(Anfibio.ranas == 2 and Anfibio.salamandras == 1)
print(Reptil.iguanas == 2 and Reptil.serpientes == 1)
print(Pez.salmones == 1 and Pez.bacalaos == 2)

zoo = Zoologico("Central park", "Calle Principal")
print(zoo.getNombre() == "Central park")

zoo1 = Zoologico("Central perk", "Calle Principal")
zona1 = Zona("salvaje", zoo1)
zona2 = Zona("salvaje")
print(zona1.getNombre() == "salvaje" and zona1.getZoo().getNombre() == "Central perk" and zona2.getZoo() == None)

an1 = Animal("Perro", 10, "casa", "m")
print(an1.getNombre() == "Perro" and an1.getEdad() == 10 and an1.getHabitat() == "casa" and an1.getGenero() == "m")

anf1 = Anfibio("rana", 5, "pradera", "F", "verde", False)
print(anf1.getNombre() == "rana" and anf1.getEdad() == 5 and anf1.getHabitat() == "pradera" and anf1.getGenero() == "F" and anf1.getColorPiel() == "verde" and anf1.isVenenoso() == False)

ave1 = Ave("paloma", 5, "ciudad", "F", "gris")
ave1.getNombre() == "paloma" and ave1.getEdad() == 5 and ave1.getHabitat() == "ciudad" and ave1.getGenero() == "F" and ave1.getColorPlumas() == "gris"

mam1 = Mamifero("persona", 50, "ciudad", "F", False, 2)
print(mam1.getNombre() == "persona" and mam1.getEdad() == 50 and mam1.getHabitat() == "ciudad" and mam1.getGenero() == "F" and mam1.isPelaje() == False and mam1.getPatas() == 2)

pez1 = Pez("payaso", 5, "mar", "F", "azul", 3)
print(pez1.getNombre() == "payaso" and pez1.getEdad() == 5 and pez1.getHabitat() == "mar" and pez1.getGenero() == "F" and pez1.getColorEscamas() == "azul" and pez1.getCantidadAletas() == 3)

rep1 = Reptil("lagartija", 1, "casa", "F", "cafe", 1)
print(rep1.getNombre() == "lagartija" and rep1.getEdad() == 1 and rep1.getHabitat() == "casa" and rep1.getGenero() == "F" and rep1.getColorEscamas() == "cafe" and rep1.getLargoCola() == 1)

Anfibio.crearRana("test", 11, "M")
Anfibio.crearSalamandra("test", 11, "M")
Mamifero.crearCaballo("test", 11, "M")
Mamifero.crearCaballo("test", 11, "M")
Mamifero.crearLeon("test", 11, "M")
Reptil.crearIguana("test", 11, "M")
Pez.crearSalmon("test", 11, "M")
Ave.crearHalcon("test", 11, "M")
Ave.crearHalcon("test", 11, "M")
comp = "Mamiferos : 3\nAves : 2\nReptiles : 1\nPeces : 1\nAnfibios : 2"

print(comp.replace('\n', ''))
print(Animal.totalPorTipo().replace('\n', ''))
print(Animal.totalPorTipo().replace('\n', '') == comp.replace('\n', ''))

ave1 =Ave("paloma", 5, "ciudad", "F", "gris")
comp = "Mi nombre es paloma, tengo una edad de 5, habito en ciudad y mi genero es F"
print(ave1.toString() ==  comp)