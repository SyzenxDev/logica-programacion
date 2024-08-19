import random

# Listas de palabras
palabrasFrutasVerduras = ["Manzana", "Uva", "Mango", "Pera", "Limon", "Mandarina", "Sandia", "Melon", "Aguacate", "Platano",
                          "Guineo", "Guayaba", "Guaba", "Kiwi", "Lima", "Coco", "Papaya", "Piña", "Naranja", "Higo", "Hierbita", "Comino"]
palabrasAnimales = ["Perro", "Gato", "Iguana", "Oso", "Leon", "Leopardo", "Jaguar", "Elefante", "Hormiga", "Saltamonte", 
                    "Pajaro", "Loro", "Avestruz", "Gallina", "Gallinazo", "Pato", "Serpiente", "Mono", "Gorila", 
                    "Escarabajo", "Mosquito", "Sancudo", "Oruga", "Mariposa", "Pavo", "Chancho", "Cerdo", "Oveja", "Vaca", "Toro", "Burro", "Lobo"]

# Menú de selección
print("---------------------------------------")
print("        Selecciona la categoria        ")
print("")
print("1. Frutas y Verduras")
print("2. Animales")
print("3. Futbolistas (Proximamente)")
print("4. Marcas de auto (Proximamente)")
print("5. Artistas (Proximamente)")
print("6. Actores (Proximamente)")
print("---------------------------------------")

category = int(input("Ingresa el número de la categoría: "))


if category == 1:
    print("Has seleccionado la categoría de Frutas y Verduras.")
    palabraSeleccionada = random.choice(palabrasFrutasVerduras).upper()
elif category == 2:
    print("Has seleccionado la categoría de Animales.")
    palabraSeleccionada = random.choice(palabrasAnimales).upper()
else:
    print("Proximamente....")
    exit()


palabraOculta = ['_'] * len(palabraSeleccionada)
letrasIntentadas = set()
intentosRestantes = 6


while '_' in palabraOculta and intentosRestantes > 0:
    print("\nPalabra actual: " + ' '.join(palabraOculta))
    print(f"Intentos restantes: {intentosRestantes}")
    print(f"Letras intentadas: {', '.join(letrasIntentadas)}")
    
    letra = input("Introduce una letra: ").upper()
    
    if letra in letrasIntentadas:
        print("Ya has intentado esta letra.")
    elif letra in palabraSeleccionada:
        print("¡Correcto!")
        letrasIntentadas.add(letra)
     
        for i, char in enumerate(palabraSeleccionada):
            if char == letra:
                palabraOculta[i] = letra
    else:
        print("Letra incorrecta.")
        letrasIntentadas.add(letra)
        intentosRestantes -= 1


if '_' not in palabraOculta:
    print(f"\n¡Felicidades! Has adivinado la palabra: {palabraSeleccionada}")
else:
    print(f"\nJuego terminado. La palabra era: {palabraSeleccionada}")
