def cria_novo_cliente():
    # Inicialize um dicionário vazio para armazenar as informações do cliente
    novo_cliente = {}

    # Solicite as informações do cliente ao usuário
    novo_cliente["nome"] = input("Nome do cliente: ")
    novo_cliente["nif"] = input("NIF do cliente: ")
    novo_cliente["email"] = input("E-mail do cliente: ")
    novo_cliente["telefone"] = input("Telefone do cliente: ")

    # Returnar o dicionário com as informações do novo cliente
    return novo_cliente
