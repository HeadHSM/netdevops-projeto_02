from database import Servidor, Dispositivo, session_dispositivos, session_servidores
from rich.console import Console
from rich.table import Table

console = Console()

def verificar_dispositivos():
    # Sem alteração na sua lógica, está correta
    buscar_disp = session_dispositivos.query(Dispositivo).all()
    table = Table(title="--- VERIFICAR DISPOSITIVOS ---")
    table.add_column("Nome", no_wrap=True)
    table.add_column("Usuário")
    table.add_column("IP")
    table.add_column("Ativo", justify="center")
    
    for disp in buscar_disp:
        status = "[green]Ativo[/green]" if disp.ativo else "[red]Inativo[/red]"
        table.add_row(disp.nome, disp.user_root, disp.ip_addr, status)
    
    console.print(table)
    input("\nAperte qualquer tecla para voltar...")

def verificar_servidores():
    buscar_srv = session_servidores.query(Servidor).all()
    table = Table(title="--- VERIFICAR SERVIDORES ---")
    table.add_column("Nome", no_wrap=True)
    table.add_column("Usuário")
    table.add_column("IP")
    table.add_column("Ativo", justify="center")
    
    for srv in buscar_srv:
        status = "[green]Ativo[/green]" if srv.ativo else "[red]Inativo[/red]"
        table.add_row(srv.nome, srv.user_root, srv.ip_addr, status)
    
    console.print(table)
    input("\nAperte qualquer tecla para voltar...")

def verificacao():
    while True:
        console.clear()
        console.print("--- VERIFICAR (DISPOSITIVOS/SERVIDORES) ---")
        console.print("1. Verificar Dispositivos")
        console.print("2. Verificar Servidores")
        console.print("3. Sair")
        opcao = input("Escolha [1-3 ou Dispositivos/Servidores/Sair]: ")

        match opcao.lower().strip():
            case "1" | "dispositivos":
                console.clear()
                verificar_dispositivos()
            case "2" | "servidores":
                console.clear()
                verificar_servidores()
            case "3" | "sair": 
                break
            case _:
                console.print("[bold red]Comando incorreto. Escolha [1-3 ou Dispositivos/Servidores/Sair][/bold red]")
                input("Pressione qualquer tecla para tentar novamente...")

def main():
    verificacao()

if __name__ == "__main__":
    main()