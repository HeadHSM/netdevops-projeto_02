from scripts.database import Usuario, session

nome = input("Digite o seu nome: ")
email = input("Digite o email: ")
cargo = input("Digite o cargo: ")
senha = input("Digite a senha: ")

usuario = Usuario(nome=nome, email=email, cargo=cargo, senha=senha)
session.add(usuario)
session.commit()