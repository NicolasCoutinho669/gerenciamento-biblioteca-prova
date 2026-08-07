import csv
import os

livros = [] #Lista para armazenar os livros cadastrados no sistema de biblioteca.

with open("livros.csv", "a", newline="", encoding="utf-8") as catalogo:
    livros.append(['Titulo','Autor','Ano de publicação','código/ISBN','Status']) #Adiciona as colunas de cada livro no arquivo "livros.csv".
    escritor = csv.writer(catalogo)
    escritor.writerows(livros)

print("Olá, bom dia!")
print("Algoritmo de sistema de gerenciamento de biblioteca feito por Nicolas Robert de Vasconcellos Coutinho - 2°A.")
def cadastrar():
    with open("livros.csv", "a", newline="", encoding="utf-8") as catalogo:
        escritor = csv.writer(catalogo)
        titulo_livro = input("Digite o título do livro: ")
        autor_livro = input("Digite o autor do livro: ")
        ano_publicacao = input("Digite o ano de publicação do livro: ")
        codigo_isbn = input("Digite o código/ISBN do livro: ")
        status_livro = "Disponível" #Define o status inicial do livro como "Disponível" já que acabou de ser cadastrado.
        escritor.writerow([titulo_livro, autor_livro, ano_publicacao, codigo_isbn, status_livro]) #Insere as informações do livro no arquivo "livros.csv".
        print(f"\nO livro '{titulo_livro}' foi cadastrado com sucesso!")

def registrar_emprestimo():
    print("oi")

def registrar_devolucao():
    print("oi")

def listar_livros():
    print("oi")

def buscar_livro():
    print("oi")

def ordenar_listagem():
    print("oi")

while True:
    print("\n----------------| SISTEMA DE BIBLIOTECA |----------------\n")
    print("Olá, bom dia! Por favor escolha umas das opções a seguir para continuar: \n")
    print("1 - Cadastrar livro")
    print("2 - Pegar livro emprestado")
    print("3 - Devolver livro")
    print("4 - Listar livros catalogados")
    print("5 - Buscar livro")
    print("6 - Ordenar listagem de livros")
    print("7 - Sair")
    print("---------------------------------------------------------")
    try:
        opcao = int(input("\nDigite o número da opção desejada: ")) # Solicita a opção ao usuário para continuar com o programa.
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            registrar_emprestimo()
        elif opcao == 3:
            registrar_devolucao()
        elif opcao == 4:
            listar_livros()
        elif opcao == 5:
            buscar_livro()
        elif opcao == 6:
            ordenar_listagem()
        elif opcao == 7:
            print("Saindo do sistema...")
            break # Encerra o sistema caso o usuário escolha a opção 7.
        else:
            print("Opção inválida. Por favor, tente novamente.")
    except ValueError: # Caso o número digitado não seja inteiro, reinicia a tela do menu.
        print("Número digitado inválido. Por favor, insira um número inteiro. Tente novamente.")