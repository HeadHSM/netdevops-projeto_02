from database import Usuario, session


list_usuarios = session.query(Usuario).all()
for u in list_usuarios:
    print(f"Nome: {u.nome} | Email: {u.email}")
