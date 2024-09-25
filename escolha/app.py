#calculadora com match
x = float(input ("informe um número: "))
y = float(input ("informe outro número: "))
#exibir um menu
print("1 - soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão ")
print("5 - ")

# Solicita ao usuário que escolha uma opção
opcao = input("opção desejada:" )


match opcao:
    case "1":
        print(f"A soma é{x+y}.")
    case "2":
        print(f"A sub é{x-y}.")
    case "3":
        print(f"A div é{x/y}.")     
    case "4":
        print(f"A mult  é{x*y}.")
    case _:
        print("opção invalida.")    
         




