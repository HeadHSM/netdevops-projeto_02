import create, read, update, delete
import typer

app = typer.Typer(help="CLI para Gestão de Disposiivos", rich_markup_mode="rich")

@app.command()
def registrar():
    """[green]Cadastra[/green] novos Servidores ou Dispositivos no banco."""
    create.main()

@app.command()
def verificar():
    """
    Lista e consulta os ativos cadastrados (visualização em tabelas).
    """
    read.main()

@app.command()
def remover():
    """
    Remove um ativo do inventário baseado no nome ou ID.
    """
    delete.main()

@app.command()
def atualizar():
    """
    Modifica informações de ativos existentes (IP, Usuário, Status).
    """
    update.main()

if __name__ == "__main__":
    app()
