'''
Crie um programa que calcule o IMC do usuário. O programa irá informar o valor do IMC
e informar o diagnóstico (consultar tabela do IMC na internet).
'''

# Criando as variáveis para o cálculo do IMC
# Entrada de dados
peso = float(input("Informe seu peso em Kg: ").replace(",","."))
altura = float(input("Informe sua altura em metros: ").replace(",","."))
    
# Cálculo do IMC
imc = peso / (altura ** 2)

# Saída de dados
print(f"\nSeu IMC é: {imc:.2f}")
    
if imc < 18.5:
    print("Diagnóstico: Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Diagnóstico: Peso normal")
elif 25 <= imc < 29.9:
    print("Diagnóstico: Sobrepeso")
elif 30 <= imc < 34.9:
    print("Diagnóstico: Obesidade grau 1")
elif 35 <= imc < 39.9:
    print("Diagnóstico: Obesidade grau 2")
else:
    print("Diagnóstico: Obesidade grau 3")