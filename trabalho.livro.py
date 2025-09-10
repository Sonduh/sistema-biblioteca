import matplotlib.pyplot as plt


class Livro:
    def __init__(self, titulo, autor, genero, quantidade_disponivel):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade_disponivel = quantidade_disponivel


biblioteca = []


def cadastrar_livro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    genero = input("Gênero: ")

    while True:
        try:
            quantidade = int(input("Quantidade disponível: "))
            if quantidade < 0:
                print('Quantidade inválida! Digite um número maior ou igual a zero. ')
            else:
                break
        except ValueError:
            print('Quantidade inválida! Digite um número inteiro. ')

    livro = Livro(titulo, autor, genero, quantidade)
    biblioteca.append(livro)
    print("Livro cadastrado com sucesso!")


def listar_livros():
    if not biblioteca:
        print("Nenhum livro cadastrado.")
    else:
        for i, livro in enumerate(biblioteca, start=1):
            print(
                f"{i}. {livro.titulo} - {livro.autor} ({livro.genero}) | Disponível: {livro.quantidade_disponivel}")


def buscar_livro():
    busca = input("Digite o título do livro: ").lower()
    encontrados = [
        livro for livro in biblioteca if busca in livro.titulo.lower()]
    if encontrados:
        for livro in encontrados:
            print(
                f"{livro.titulo} - {livro.autor} ({livro.genero}) | Disponível: {livro.quantidade_disponivel}")
    else:
        print("Livro não encontrado.")


def gerar_grafico():
    if not biblioteca:
        print("Nenhum livro cadastrado para gerar gráfico.")
        return

    generos = {}
    for livro in biblioteca:
        generos[livro.genero] = generos.get(
            livro.genero, 0) + livro.quantidade_disponivel

    plt.bar(generos.keys(), generos.values(), color='skyblue')
    plt.title("Quantidade de livros por gênero")
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def menu():
    while True:
        print("\n--- Sistema de Biblioteca ---")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Buscar livro por título")
        print("4. Gerar gráfico por gênero")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            buscar_livro()
        elif opcao == "4":
            gerar_grafico()
        elif opcao == "5":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
