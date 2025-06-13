from datetime import datetime  # importando módulo de data e hora

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


nome = input("Digite aqui o seu nome: ")

sobrenome = input("Digite aqui o seu sobrenome: ")

data_nascimento = obter_data_nascimento()  # chamamento de funções

idade = calcular_idade(data_nascimento)

curso = input("Digite aqui o nome do seu curso: ")

print(f"\nAluno:{nome} {sobrenome}, do curso de {curso}, tem {idade} anos")
