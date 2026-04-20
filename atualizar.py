from database import Servidor, Dispositivo, session_dispositivos, session_servidores
import os, sys, time


def construcao_timer(segundos):
    for i in range(segundos, 0, -1):
        sys.stdout.write(f"\r--- EM CONSTRUÇÂO --- Retornando em {i}")
        sys.stdout.flush()
        time.sleep(1)
    print()

def atualizar_dispositivos():
    print("--- ATUALIZAR DISPOSITIVOS ---")
    dispositivos = session_dispositivos.query(Dispositivo).all()

def atualizar_servidores():
    print("--- ATUALIZAR SERVIDORES ---")
    servidores = session_dispositivos.query(Servidor).all()

def atualizar():
    while True:
        os.system("clear")
        print("--- ATUALIZAR (DISPOSITIVOS/SERVIDORES) ---")
        print("1. Atualizar Dispositivos")
        print("2. Atualizar Servidores")
        print("3. Voltar ao Menu")
        opcao = input("Escolha [1-3]: ")

        if opcao == "1":
            os.system("clear")
            construcao_timer(5)
            return
        elif opcao == "2":
            os.system("clear")
            construcao_timer(5)
            return
        elif opcao == "3":
            os.system("clear")
            break
        else:
            print("Comando incorreto. Selecione [1-3]")
            input("Pressione qualquer tecla para voltar...")

def main():
    atualizar()

if __name__ == "__main__":
    main()