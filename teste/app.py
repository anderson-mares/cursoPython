def pode_entrar(idade, peso):
    if idade > 10 and peso < 150:
        return True
    return False

def main():
    print("Bem-vindo ao Trem Fantasma!")
    while True:
        try:
            idade = int(input("Digite a sua idade: "))
            peso = float(input("Digite o seu peso em kg: "))

            if pode_entrar(idade, peso):
                print("Você está autorizado a entrar no Trem Fantasma! Divirta-se!")
            else:
                print("Desculpe, você não pode entrar. É necessário ter mais de 10 anos e pesar menos de 150 kg.")
        except ValueError:
            print("Por favor, insira um número válido.")

        continuar = input("Deseja verificar outro usuário? (s/n): ").lower()
        if continuar != 's':
            print("Obrigado por visitar o Trem Fantasma! Até mais!")
            break

if __name__ == "__main__":
    main()
