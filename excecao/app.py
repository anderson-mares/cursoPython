try:
    # Solicita ao usuário que insira dois elementos
    nome = input("Informe um nome: ")
    idade = int(input("Informe a idade: "))
    
    print(f"Nome:{nome}.")
    print(f"Idade:{idade}.")
except:
    print("Não foi possível mostrar os dados.")


    # Tenta realizar a divisão
    resultado = x / y

except ZeroDivisionError:
    # Captura a exceção de divisão por zero
    print("Erro: Não é possível dividir por zero.")

except ValueError:
    # Captura a exceção de valor inválido (quando a entrada não é um número)
    print("Erro: Por favor, insira um número válido.")

else:
    # Executa se nenhuma exceção for levantada
    print("O resultado da divisão é:", resultado)

finally:
    # Executa independentemente de uma exceção ter sido levantada ou não
    print("Operação finalizada.")
