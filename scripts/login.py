from database import Usuario, session

email = input("Digite o email: ")
senha = input("Digite a senha: ")

usuario_login = session.query(Usuario).filter_by(email=email, senha=senha).first()
if usuario_login:
    print(f"Bem-vindo {usuario_login.nome}!")
else:
    print("Email ou senha incorreto!")

