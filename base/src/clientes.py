from io_terminal import imprime_lista

nome_ficheiro_lista_de_clientes = "lista_de_clientes.pk"

# TODO: Copie para aqui o código de cada uma das funções nos
# ficheiros com o nome clientes-*.py e faça um commit de cada vez
# Quando este ficheiro estiver completo com todas as suas funções,
# deve ser o unico ficheiro clientes.py existente, deve apagar
# todos os outros ficheiros clientes-*.py, e inclusive estes comentários

# ...
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

def imprime_lista_de_clientes(lista_de_clientes):
    """TODO: documentação"""

    #TODO: Implementar esta função
    # ...