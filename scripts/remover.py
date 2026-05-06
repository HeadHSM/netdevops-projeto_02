from database import Servidor, Dispositivo, session_dispositivos, session_servidores
from rich.console import Console
from rich.table import Table

console = Console()

def remover_dispositivos():
    dispositivos = session_dispositivos.query(Dispositivo).all()
    
    if not dispositivos:
        console.print("Nenhum dispositivo encontrado")
        return
    
    # Montagem da Tabela
    table = Table(title="REMOVER DISPOSITIVOS")
    table.add_column("ID", justify="right")
    table.add_column("Nome")
    table.add_column("IP")
    table.add_column("Status")

    for disp in dispositivos:
        status_disp = "ON" if disp.ativo else "OFF"
        table.add_row(str(disp.id), disp.nome, disp.ip_addr, status_disp)
    
    console.print(table)
    
    disp_deletar = input("\nDigite o ID ou o nome do dispositivo que deseja excluir (ou 's' para sair): ")
    
    if disp_deletar.lower().strip() == "s":
        return
    
    busca_disp = session_dispositivos.query(Dispositivo).filter(
        (Dispositivo.id == disp_deletar) | (Dispositivo.nome == disp_deletar)
    ).first()

    if busca_disp:
        session_dispositivos.delete(busca_disp)
        session_dispositivos.commit()
        console.print(f"Dispositivo {busca_disp.nome} deletado com sucesso")
    else:
        console.print("Erro: Dispositivo não encontrado")

def remover_servidores():
    servidores = session_servidores.query(Servidor).all()
    
    if not servidores:
        console.print("Nenhum servidor encontrado")
        return
    
    # Montagem da Tabela
    table = Table(title="REMOVER SERVIDORES")
    table.add_column("ID", justify="right")
    table.add_column("Nome")
    table.add_column("IP")
    table.add_column("Status")

    for serv in servidores:
        status_srv = "ON" if serv.ativo else "OFF"
        table.add_row(str(serv.id), serv.nome, serv.ip_addr, status_srv)
    
    console.print(table)
    
    srv_deletar = input("\nDigite o ID ou o nome do servidor que deseja excluir (ou 's' para sair): ")

    if srv_deletar.lower().strip() == "s":
        return
    
    # Corrigido o filtro para buscar na tabela Servidor
    busca_srv = session_servidores.query(Servidor).filter(
        (Servidor.id == srv_deletar) | (Servidor.nome == srv_deletar)
    ).first()

    if busca_srv:
        session_servidores.delete(busca_srv)
        session_servidores.commit()
        console.print(f"O Servidor {busca_srv.nome} foi excluído com sucesso")
    else:
        console.print("Erro: Servidor não encontrado")


def remover():

    while True:
        console.clear()
        console.print("--- REMOVER (DISPOSITIVOS/SERVIDORES) ---")
        console.print("1. Remover Dispositivos")
        console.print("2. Remover Servidores")
        console.print("3. Sair")
        opcao = input("Escolha [1-3 ou Dispositivos/Servidores/Sair]: ")

        match opcao.lower().strip():
            case "1" | "dispositivos":
                console.clear()
                remover_dispositivos()
            case "2" | "servidores":
                console.clear()
                remover_servidores()
            case "3" | "sair":
                console.clear()
                break
            case _:
                print("Comando incorreto. [1-3 ou Dispositivos/Servidores/Sair]")
                input("Pressione qualquer tecla para voltar...")

def main():
    remover()

if __name__ == "__main__":
    main()