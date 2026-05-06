import scripts.criar as criar, scripts.ler as ler, scripts.atualizar as atualizar, scripts.remover as remover
import typer

app = typer.Typer(help="CLI para Gestão de Disposiivos", rich_markup_mode="rich")

@app.command()
def registrar():
    """
    Cadastra novos Servidores ou Dispositivos no banco.
    """
    criar.main()

@app.command()
def verificar():
    """
    Lista e consulta os ativos cadastrados (visualização em tabelas).
    """
    ler.main()

@app.command()
def excluir():
    """
    Remove um ativo do inventário baseado no nome ou ID.
    """
    remover.main()

@app.command()
def alterar():
    """
    Modifica informações de ativos existentes (IP, Usuário, Status).
    """
    atualizar.main()

if __name__ == "__main__":
    app()
