from database import Servidor, Dispositivo, session_dispositivos, session_servidores
import os, sys, time


def construcao_timer(segundos):
    for i in range(segundos, 0, -1):
        sys.stdout.write(f"\r--- EM CONSTRUÇÂO --- Retornando em {i}")
        sys.stdout.flush()
        time.sleep(1)
    print()

def remover_dispositivos():
    print("--- REMOVER DISPOSITIVOS ---")
    dispositivos = session_dispositivos.query(Dispositivo).all()



def remover_servidores():
    print("--- REMOVER SERVIDORES ---")
    servidores = session_servidores.query(Servidor).all()

   

def remover():
    while True:
        os.system("clear")
        print("--- REMOVER (DISPOSITIVOS/SERVIDORES) ---")
        print("1. Remover Dispositivos")
        print("2. Remover Servidores")
        print("3. Voltar ao Menu")
        opcao = input("Escolha [1-3]: ")

        if opcao == "1":
            os.system("clear")
            construcao_timer(5)
        elif opcao == "2":
            os.system("clear")
            construcao_timer(5)
        elif opcao == "3":
            os.system("clear")
            break
        else:
            print("Comando incorreto. Selecione [1-3]")
            input("Pressione qualquer tecla para voltar...")

def main():
    remover()

if __name__ == "__main__":
    main()