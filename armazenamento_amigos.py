import sqlite3
from datetime import datetime  # importando módulo de data e hora

conn = sqlite3.connect("contatos.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    data_nascimento DATE NOT NULL,
    idade INTEGER NOT NULL,
    curso TEXT NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
conn.commit()


FORMATO_DATA = "%d/%m/%Y"  # definindo constante


# criando função para armazenar em uma variável a data de nascimento, importante ".strptime" divide a string.
def obter_data_nascimento():
    while True:  # colocando uma condicional para prever erros
        try:
            data_str = input(
                "Digite aqui sua data de nascimento (DD/MM/AAAA): ").strip()
            data_nasc = datetime.strptime(data_str, FORMATO_DATA)

            if data_nasc > datetime.now():  # condicional
                print("Data de nacimento não pode ser no futuro!")
                continue
            return data_nasc  # atento a identação! precisa seguir o caminho certo. Return volta o valor correto quando aplicado no caminho de if

        except ValueError:  # definiu caso de erro
            print("Formato inválido! Use DD/MM/AAAA (Ex. 18/02/1990)")


def calcular_idade(data_nasc):
    hoje = datetime.now()
    idade = hoje.year - data_nasc.year
    if (hoje.month, hoje.day) < (data_nasc.month, data_nasc.day):
        idade -= 1  # condicional para quem já fez aniversário
    return idade


def obter_sobrenome():
    while True:
        try:
            sobrenome = input("Digite o sobrenome (apenas letras): ")
            if all(c.isalpha() or c in ' -' for c in sobrenome):
                return sobrenome
        except ValueError:
            print("ERRO: Use apenas letras, espaços ou hífens!")


def cadastrar_contato():
    print("\n---NOVO CADASTRO---")
    nome = input("Digite seu nome: ")
    sobrenome = obter_sobrenome()
    data_nasc = obter_data_nascimento()
    idade = calcular_idade(data_nasc)
    curso = input("Digite seu Curso: ")
    try:
        cursor.execute('''INSERT INTO contatos (nome, sobrenome, data_nascimento, idade, curso)
                   VALUES (?, ?, ?, ?, ?)''',  (nome, sobrenome, data_nasc.date(), idade, curso))
        conn.commit()
        print("Contato cadastrado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao cadastrar: {e}")


def listar_contatos():
    print("\n---CONTATOS CADASTRADOS---")
    cursor.execute('SELECT * FROM contatos ORDER BY nome')
    contatos = cursor.fetchall()

    if not contatos:
        print("Nenhum contato encontrado :/")
        return
    for contato in contatos:
        print(f"ID: {contato[0]}")
        print(f"Nome: {contato[1]} {contato[2]}")
        print(f"Data Nascimento: {contato[3]} Idade: {contato[4]} anos")
        print(f"Curso {contato[5]}")
        print(f"Cadastrado em: {contato[6]}")
        print('-' * 30)


while True:
    print("\n\nSISTEMA DE CADASTRO DE CONTAOS")
    print("1 - Cadastrar novo contato")
    print("2 - Listar contatos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_contato()
    elif opcao == '2':
        listar_contatos()
    elif opcao == '3':
        print("Saindo do sistema. . .")
        break
    else:
        print("Opção inválida!")

conn.close()
