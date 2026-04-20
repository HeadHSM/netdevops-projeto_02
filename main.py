import registro, verificacao, atualizar, remover
import os

def main():
    while True:
        os.system("clear")
        print("--- MENU PRINCIPAL ---")
        print("1. Registrar (Dispositivos/Servidores)")
        print("2. Verificar (Dispositivos/Servidores)")
        print("3. Editar (Dispositivos/Servidores)")
        print("4. Remover (Dispositivos/Servidores)")
        print("5. Sair")
        opcao = input("Escolha [1-5]: ")

        if opcao == "1":
            os.system("clear")
            registro.main()
        elif opcao == "2":
            os.system("clear")
            verificacao.main()
        elif opcao == "3":
            os.system("clear")
            print("--- EM CONSTRUÇÂO ---")
            atualizar.main()
        elif opcao == "4":
            os.system("clear")
            print("--- EM CONSTRUÇÂO ---")
            remover.main()
        elif opcao == "5":
            print("--- SAINDO... ---")
            break
        else:
            print("Comando incorreto. Selecione [1-5]")
            input("Pressione qualquer tecla para voltar...")

if __name__ == "__main__":
    main()
