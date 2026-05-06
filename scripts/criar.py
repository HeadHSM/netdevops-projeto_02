from database import Servidor, Dispositivo, session_dispositivos, session_servidores
from rich.console import Console

def registro_dispositivos():
    print("--- REGISTRAR DISPOSITIVOS ---")
    nome_disp = input("Nome do Dispositivo: ")
    grupo_disp = input("Grupo (Cisco/Juniper/Huawei): ")
    user_disp = input("Usuário: ")
    ip_addr_disp = input("Endereço IP: ")
    ssh_key_disp = input("Chave SSH: ")

    dispositivo_db = Dispositivo(
        nome=nome_disp,
        user_root=user_disp,
        ip_addr=ip_addr_disp,
        ssh_key=ssh_key_disp,
        grupo=grupo_disp
    )

    session_dispositivos.add(dispositivo_db)
    session_dispositivos.commit()

def registrar_servidores():
    print("--- REGISTRAR SERVIDORES ---")
    nome_srv = input("Nome do Servidor: ")
    grupo_srv = input("Grupo (Debian/Ubuntu/Alpine): ")
    user_srv = input("Usuário: ")
    ip_addr_srv = input("Endereço IP: ")
    ssh_key_srv = input("Chave SSH: ")

    servidores_db = Servidor(
        nome=nome_srv,
        user_root=user_srv,
        ip_addr=ip_addr_srv,
        ssh_key=ssh_key_srv,
        grupo=grupo_srv
    )

    session_servidores.add(servidores_db)
    session_servidores.commit()

def regitros():
    console = Console()

    while True:
        console.clear()
        print("--- REGISTRAR (DISPOSITIVOS/SERVIDORES) ---")
        print("1. Registrar Dispositivos")
        print("2. Registrar Servidores")
        print("3. Sair")
        opcao = input("Escolha [1-3 ou Dispositivos/Servidores/Sair]: ")

        match opcao.lower().strip():
            case "1" | "dispositivos":
                console.clear()
                registro_dispositivos()
            case "2" | "servidores": 
                console.clear()
                registrar_servidores()
            case "3" | "sair":
                console.clear()
                break
            case _:
                print("Comando incorreto. [1-3 ou Dispositivos/Servidores/Sair]")
                input("Pressione qualquer tecla para voltar...")

def main():
    regitros()

if __name__ == "__main__":
    main()