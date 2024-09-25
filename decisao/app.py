# entrada de dados
nome = input("Informe seu nome: ")
nota = int(input("Informe sua nota de 0 a 10: "))

# estrutura de decisão
if nota >= 0 and nota <= 10:
    if nota >= 7:
        print(f"{nome} está aprovado.")
    elif nota>= 5:
        print(f"{nome} está de recuperação.")
    else:
        print(f"{nome} está reprovado.")
else:
    print("Nota inválida.")


