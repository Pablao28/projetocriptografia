from cifra import cifrar_texto, decifrar_texto

def exibir_menu():
    print("\n" + "="*35)
    print("   SISTEMA DE CIFRAGEM POR SUBSTITUIÇÃO")
    print("="*35)
    print("1. Cifrar mensagem")
    print("2. Decifrar mensagem")
    print("3. Sair")
    return input("Escolha uma opção (1-3): ").strip()

def main():
    while True:
        opcao = exibir_menu()
        
        if opcao == "1":
            mensagem = input("\nDigite a mensagem a ser cifrada: ")
            try:
                chave = int(input("Digite o valor do deslocamento (chave numérica): "))
                resultado = cifrar_texto(mensagem, chave)
                print(f"\n🔐 Mensagem Cifrada: {resultado}")
            except ValueError:
                print("⚠️ Erro: A chave precisa ser um número inteiro.")
                
        elif opcao == "2":
            mensagem = input("\nDigite a mensagem cifrada: ")
            try:
                chave = int(input("Digite a chave usada na cifragem: "))
                resultado = decifrar_texto(mensagem, chave)
                print(f"\n🔓 Mensagem Decifrada: {resultado}")
            except ValueError:
                print("⚠️ Erro: A chave precisa ser um número inteiro.")
                
        elif opcao == "3":
            print("\nEncerrando o programa... Até logo!")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()