#importar bibliotecas
import time
import os
import winsound

#entrada de dados
n = int(input("Informe um número inteiro positivo: "))

def boom_sound():
    frequency = 2000
    duration = 2500

    winsound.Beep(frequency, duration)

while n > 0:
    os.system("cls")
    print(n)
    time.sleep(1)
    n -= 1

os.system("cls")
print("BOOOMM!!!")
boom_sound()
time.sleep(3)