import getpass

usuario = input("Digite o usuário: ").upper()
senha = getpass.getpass("Digite a senha: ")

if usuario == "GISORE" and senha == "FiapON":
    print("Usuário logado")
else:
    print("Login Negado")