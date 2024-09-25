'''
Crie um programa que receba do usuário as seguintes informações:
- Nome
- CPF
- Telefone
- E-mail
- Endereço
- Gênero
- Escolaridade
- Signo
- Tipo Sanguíneo
Ao final, o programa exibe essas informações na tela.
Ao terminar, crie um repositório no GitHub.
'''

# Recebendo as informações do usuário
nome = input("Digite seu nome: ")
cpf = input("Insira seu CPF: ")
telefone = input("Digite seu telefone com o DDD: ")
email = input("Digite seu e-mail: ")  # Corrigido o nome da variável
endereco = input("Digite seu endereço: ")
genero = input("Digite seu gênero: ")  # Corrigido para gênero
escolaridade = input("Informe sua escolaridade: ")
signo = input("Digite seu signo: ")
tipo_sanguineo = input("Informe seu tipo sanguíneo: ")

# Exibindo as informações coletadas
print("\nInformações coletadas:")
print(f"Nome: {nome}")
print(f"CPF: {cpf}")
print(f"Telefone: {telefone}")
print(f"E-mail: {email}")
print(f"Endereço: {endereco}")
print(f"Gênero: {genero}")
print(f"Escolaridade: {escolaridade}")
print(f"Signo: {signo}")
print(f"Tipo Sanguíneo: {tipo_sanguineo}")
