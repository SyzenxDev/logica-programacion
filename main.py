## 

palabrasFrutasVerduras = ["Manzana","Uva","Mango","Pera","Limon","Mandarina", "Sandia","Melon","Aguacate", "Platano","Guineo","Guayaba","Guaba","Kiwi","Lima","Coco","Papaya","Piña","Naranja","Higo","Hierbita","Comino"]
palabrasAnimales = ["Perro", "Gato", "Iguana", "Oso", "Leon", "Leopardo", "Jaguar", "Elefante", "Hormiga", "Saltamonte", "Pajaro","Loro","Avestruz","Gallina","Gallinazo","Pato","Serpiente","Mono","Gorila","Escarabajo","Mosquito","Sancudo","Oruga","Mariposa","Pavo", "Chancho", "Cerdo","Oveja","Vaca","Toro","Burro","Lobo"]



print("---------------------------------------")
print("        Selecciona la categoria        ")
print("")
print("1.Frutas y Verduras")
print("2.Animales")
print("3.Futbolistas (Proximamente)")
print("4.Marcas de auto (Proximamente)")
print("5.Artistas (Proximamente)")
print("6.Actores (Proximamente)")
print("---------------------------------------")

category = int(input())

if category == 1: 
    print("Haz seleccionado la categoria de Frutas y Verduras.")   
elif category == 2:
    print("Haz seleccionado la categoria de Animales.")   
else:
    print("Proximamente....")


