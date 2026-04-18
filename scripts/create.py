from database import Usuario, bcrypt, session 

nome = input("Digite o seu nome: ")
email = input("Digite o email: ")
cargo = input("Digite o cargo: ")
senha = input("Digite a senha: ")

senha_bytes = senha.encode("utf-8")
senha_hash = bcrypt.hashpw(senha_bytes, bcrypt.gensalt())
senha_hash_str = senha_hash.decode("utf-8")

usuario = Usuario(nome=nome, email=email, cargo=cargo, senha=senha_hash_str)
session.add(usuario)
session.commit()