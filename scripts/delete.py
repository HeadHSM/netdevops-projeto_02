from scripts.database import Usuario, session

nome = input("Digite o nome para deletar: ")
deletar_usuario = session.query(Usuario).filter_by(nome=nome).first()

if deletar_usuario:
    session.delete(deletar_usuario)
    session.commit()
    print(f"O Usuário {nome} foi deletado com sucesso!")
else:
    print("Usuário não encontrado")
    