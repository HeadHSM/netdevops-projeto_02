from database import Usuario, bcrypt, session

email = input("Digite o seu email: ")
senha = input("Digite a sua senha: ")

usuario_login = session.query(Usuario).filter_by(email=email).first()
if usuario_login and bcrypt.checkpw(senha.encode("utf-8"), usuario_login.senha.encode("utf-8")):
    print(f"Bem-vindo {usuario_login.nome}")
else:
    print("Email ou senha incorreto!")


