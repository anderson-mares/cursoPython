# crie um programa que possa inserir o nome na lista
# inserir nome
# exibir a lista de nomes
# Odernar os nomes
# Alterar um nome na lista
# Excluir um nome na lista
# Sair do programa
# o programa deverá exibir um menu, e o usuário irá escolher a opção desejada do menu
# ao terminar, envie o Github e poste o link do repositorio no Classroom

import time

menu = ["Exibir nomes", "Inserir nome", "Alterar nome", "Excluir nome", "Sair"]

nomes = ["Joao", "Maria", "Jose", "Joana", "Jurema"]

# Mantém o programa rodando até que o usuário escolha a opção 'Sair'
while True:
    # Exibe o menu
    print(f"\n##################")
    print(f"\nEscolha uma opção no menu abaixo:")
    time.sleep(1)

    for i in range(len(menu)):
        print(f"Opção {i}: {menu[i]}")
        time.sleep(1)

    try:
        opcao = int(input("\nInforme o número da opção: "))
        time.sleep(2)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        continue

    # Opções do menu
    if opcao == 0:
        print("\nLista de nomes:")
        for i in range(len(nomes)):
            print(f"Índice {i}: Nome: {nomes[i]}")
            time.sleep(1)

    elif opcao == 1:
        nome_incluido = input("Informe o nome que deseja incluir: ")
        if nome_incluido != '':
            nomes.append(nome_incluido)
            print(f"Nome '{nome_incluido}' foi adicionado com sucesso!")
        else:
            print("Nome não pode ser vazio.")
        time.sleep(1)

    elif opcao == 2:
        nome_antigo = input("Informe o nome que deseja alterar: ")
        if nome_antigo in nomes:
            novo_nome = input("Agora informe o novo nome: ")
            nomes[nomes.index(nome_antigo)] = novo_nome
            print(f"Nome '{nome_antigo}' foi alterado para '{novo_nome}'.")
        else:
            print(f"Nome '{nome_antigo}' não encontrado na lista.")
        time.sleep(1)

    elif opcao == 3:
        nome_excluir = input("Informe o nome que deseja excluir: ")
        if nome_excluir in nomes:
            nomes.remove(nome_excluir)
            print(f"Nome '{nome_excluir}' foi excluído com sucesso!")
        else:
            print(f"Nome '{nome_excluir}' não encontrado na lista.")
        time.sleep(1)

    elif opcao == 4:
        print("Encerrando o programa. Até mais!")
        break

    else:
        print("Opção inválida! Tente novamente.")