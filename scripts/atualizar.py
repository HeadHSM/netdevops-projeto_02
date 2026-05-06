from database import Servidor, Dispositivo, session_dispositivos, session_servidores
import time
from rich.console import Console
from rich.table import Table

console = Console()

def atualizar_dispositivos():
    dispositivos = session_dispositivos.query(Dispositivo).all()

    if not dispositivos:
        print("Dispositivos não encontrados")
        return
    
    # Montagem da Tabela
    table = Table(title="ATUALIZAR DISPOSITIVOS")
    table.add_column("ID", justify="right")
    table.add_column("Nome")
    table.add_column("IP")
    table.add_column("Status")

    for disp in dispositivos:
        status_disp = "ON" if disp.ativo else "OFF"
        table.add_row(str(disp.id), disp.nome, disp.ip_addr, status_disp)
    
    console.print(table)

    try:
        id_escolhido = int(input("\nDigite o ID do dispositivo que deseja alterar: "))
        
        # 2. Buscar o objeto específico no banco
        disp = session_dispositivos.query(Dispositivo).filter_by(id=id_escolhido).first()

        if disp:
            print(f"Editando: {disp.nome}")
            novo_nome = input(f"Novo nome [{disp.nome}]: ") or disp.nome
            novo_ip = input(f"Novo IP [{disp.ip_addr}]: ") or disp.ip_addr
            
            # 3. Alterar os valores do objeto
            disp.nome = novo_nome
            disp.ip_addr = novo_ip

            # 4. Salvar no Banco de Dados
            session_dispositivos.commit()
            console.print("[bold green]Dados atualizados com sucesso![/bold green]")
            time.sleep(2)
        else:
            print("ID não encontrado.")
            
    except ValueError:
        print("ID inválido. Digite um número.")
    except Exception as e:
        session_dispositivos.rollback() # Reverte se der erro
        print(f"Erro ao atualizar: {e}")


def atualizar_servidores():
    servidores = session_servidores.query(Servidor).all()

    if not servidores:
        print("Servidores não encontrados")
        return
    
    # Montagem da Tabela
    table = Table(title="ATUALIZAR SERVIDORES")
    table.add_column("ID", justify="right")
    table.add_column("Nome")
    table.add_column("IP")
    table.add_column("Status")

    for srv in servidores:
        status_srv = "ON" if srv.ativo else "OFF"
        table.add_row(str(srv.id), srv.nome, srv.ip_addr, status_srv)
    
    console.print(table)

    try:
        id_escolhido = int(input("\nDigite o ID do Servidor que deseja alterar: "))
        
        # 2. Buscar o objeto específico no banco
        srv = session_servidores.query(Servidor).filter_by(id=id_escolhido).first()

        if srv:
            print(f"Editando: {srv.nome}")
            novo_nome = input(f"Novo nome [{srv.nome}]: ") or srv.nome
            novo_ip = input(f"Novo IP [{srv.ip_addr}]: ") or srv.ip_addr
            
            # 3. Alterar os valores do objeto
            srv.nome = novo_nome
            srv.ip_addr = novo_ip

            # 4. Salvar no Banco de Dados
            session_servidores.commit()
            console.print("[bold green]Dados atualizados com sucesso![/bold green]")
            time.sleep(2)
        else:
            print("ID não encontrado.")
            
    except ValueError:
        print("ID inválido. Digite um número.")
    except Exception as e:
        session_servidores.rollback() # Reverte se der erro
        print(f"Erro ao atualizar: {e}")

def update():
    console = Console()
    while True:
        console.clear()
        console.print("--- ATUALIZAR (DISPOSITIVOS/SERVIDORES) ---")
        console.print("1. Atualizar Dispositivos")
        console.print("2. Atualizar Servidores")
        console.print("3. Sair")
        opcao = input("Escolha [1-3 ou Dispositivos/Servidores/Sair]: ")

        match opcao.lower().strip():
            case "1" | "dispositivos":
                console.clear()
                atualizar_dispositivos()
                continue
            case "2" | "servidores":
                console.clear()
                atualizar_servidores()
                continue
            case "3" | "sair":
                console.clear()
                break
            case _:
                console.print("[bold red]Comando incorreto. Escolha [1-3 ou Dispositivos/Servidores/Sair][/bold red]")
                input("Pressione qualquer tecla para tentar novamente...")

def main():
    update()

if __name__ == "__main__":
    main()