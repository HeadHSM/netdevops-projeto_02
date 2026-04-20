from database import Servidor, Dispositivo, session_dispositivos, session_servidores
import os

def verificar_dispositivos():
    buscar_disp = session_dispositivos.query(Dispositivo).all()
    print("--- VERIFICAR DISPOSITIVOS ---")
    for disp in buscar_disp:
        print("-----------------------")
        print(f"Nome: {disp.nome}\nUsuário: {disp.user_root}\nIP: {disp.ip_addr}\nAtivo: {disp.ativo} ")
        print("-----------------------")
    input("Aperte qualquer tecla para sair...")

def verificar_servidores():
    buscar_srv = session_servidores.query(Servidor).all()
    print("--- VERIFICAR SERVIDORES ---")
    for srv in buscar_srv:
        print("-----------------------")
        print(f"Nome: {srv.nome}\nUsuário: {srv.user_root}\nIP: {srv.ip_addr}\nAtivo: {srv.ativo} ")
        print("-----------------------")
    input("Aperte qualquer tecla para sair...")

def verificacao():
    while True:
        os.system("clear")
        print("--- VERIFICAR (DISPOSITIVOS/SERVIDORES) ---")
        print("1. Verificar Dispositivos")
        print("2. Verificar Servidores")
        print("3. Voltar ao Menu")
        opcao = input("Escolha [1-3]: ")

        if opcao == "1":
            os.system("clear")
            verificar_dispositivos()
        elif opcao == "2":
            os.system("clear")
            verificar_servidores()
        elif opcao == "3":
            os.system("clear")
            break
        else:
            print("Comando incorreto. Selecione [1-3]")
            input("Pressione qualquer tecla para voltar...")

def main():
    verificacao()

if __name__ == "__main__":
    main()