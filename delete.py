from database import Servidor, Dispositivo, session_dispositivos, session_servidores
import sys, time
from rich.console import Console

def construcao_timer(segundos):
    for i in range(segundos, 0, -1):
        sys.stdout.write(f"\r--- EM CONSTRUÇÂO --- Retornando em {i}")
        sys.stdout.flush()
        time.sleep(1)
    print()

def remover_dispositivos():
    print("--- REMOVER DISPOSITIVOS ---")
    dispositivos = session_dispositivos.query(Dispositivo).all()
    if not dispositivos:
        print("Nenhum dispositivos encontrado")
        return
    
    for disp in dispositivos:
        status = "ON" if disp.ativo else "OFF"

        print(f"ID: {disp.id} | Nome: {disp.nome} | Ativo: {status}")
    
    disp_deletar = input("\nDigite o ID ou o nome do dispositivo que deseja excluir (ou 's' para sair): ")
    
    if disp_deletar.lower().strip() == "s":
        return
    
    busca = session_dispositivos.query(Dispositivo).filter((Dispositivo.id == disp_deletar) | Dispositivo.nome == disp_deletar).first()

    if busca:
        session_dispositivos.delete(busca)
        session_dispositivos.commit()
        session_dispositivos.close()
        print(f"Dispositivo {busca.nome} deletado com sucesso")
    else:
        print("Erro: Dispositivo não encontrado")

def remover_servidores():
    print("--- REMOVER SERVIDORES ---")
    servidores = session_servidores.query(Servidor).all()


def remover():
    console = Console()

    while True:
        console.clear()
        print("--- REMOVER (DISPOSITIVOS/SERVIDORES) ---")
        print("1. Remover Dispositivos")
        print("2. Remover Servidores")
        print("3. Sair")
        opcao = input("Escolha [1-3 | Dispositivos/Servidores/Sair]: ")

        match opcao.lower().strip():
            case "1" | "dispositivos":
                console.clear()
                remover_dispositivos()
            case "2" | "servidores":
                console.clear()
                construcao_timer(5)
            case "3" | "sair":
                console.clear()
                break
            case _:
                print("Comando incorreto. [1-3 | Dispositivos/Servidores/Sair]")
                input("Pressione qualquer tecla para voltar...")

def main():
    remover()

if __name__ == "__main__":
    main()