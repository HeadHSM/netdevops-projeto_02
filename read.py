from database import Servidor, Dispositivo, session_dispositivos, session_servidores
import os
import typer
from rich.console import Console

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
    console = Console()

    while True:
        console.clear()
        print("--- VERIFICAR (DISPOSITIVOS/SERVIDORES) ---")
        print("1. Verificar Dispositivos")
        print("2. Verificar Servidores")
        print("3. Sair")
        opcao = input("Escolha [1-3]: ")

        match opcao:
            case "1":
                console.clear()
                verificar_dispositivos()
            case "2":
                console.clear()
                verificar_servidores()
            case "3":
                console.clear()
                break
            case _: # como se fosse o default da Linguagem C/C++ ou então o else
                print("Comando incorreto. Selecione [1-3]")
                input("Pressione qualquer tecla para voltar...")

def main():
    verificacao()

if __name__ == "__main__":
    main()