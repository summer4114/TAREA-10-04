import random
from utils import get_integer_input

def play_game():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("Estoy pensando en un número entre 1 y 100...")

    while True:
        intento = get_integer_input("Adivina el número: ")
        intentos += 1

        if intento < numero_secreto:
            print("Muy bajo. Intenta otra vez.")
        elif intento > numero_secreto:
            print("Muy alto. Intenta otra vez.")
        else:
            print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
            break
