import random

print("\tJuego del ahorcado\n\n")

listapalabras = ['hola', 'adios', 'perro', 'gato', 'carro', 'python', 'a']
tupalabra = ''
intentos = 6
palabra = listapalabras[random.randint(1,7)]

while intentos > 0:
    fallas = 0
    for letra in palabra:
        if letra in tupalabra.lower():
            print(letra, end = "") ##Siguiente palabra se escriba enseguida
        else:
            print("*", end="")
            fallas += 1
    if fallas == 0:
        print("\nGanaste!!!!\n")
        print("          O  ")
        print("         \|/ ")
        print("          |  ")
        print("         / \ ")
        break
    tuletra = input("\nIntroduce una letra: ").lower()
    tupalabra += tuletra.lower()

    if tuletra.lower() not in palabra: ##Verificar si la letra existe en la cadena
        intentos -= 1
        print("Fallaste")
        print("Te quedan ",+intentos, " intentos")
        if intentos == 5:
            print("------------")
            print("|          |")
            print("|          O")
            print("|         ")
            print("|         ")
            print("|         ")
            print("|")
            print("|____")
        if intentos == 4:
            print("------------")
            print("|          |")
            print("|          O")
            print("|          |")
            print("|          |")
            print("|         ")
            print("|")
            print("|____")
        if intentos == 3:
            print("------------")
            print("|          |")
            print("|          O")
            print("|         /|")
            print("|          |")
            print("|         ")
            print("|")
            print("|____")
        if intentos == 2:
            print("------------")
            print("|          |")
            print("|          O")
            print("|         /|\ ")
            print("|          |")
            print("|         ")
            print("|")
            print("|____")
        if intentos == 1:
            print("------------")
            print("|          |")
            print("|          O")
            print("|         /|\ ")
            print("|          |")
            print("|         / ")
            print("|")
            print("|____")
    if intentos == 0:
        print("------------")
        print("|          |")
        print("|          O")
        print("|         /|\ ")
        print("|          |")
        print("|         / \ ")
        print("|")
        print("|____")
        print("perdiste :(")
else:
    print("Gracias por jugar")
