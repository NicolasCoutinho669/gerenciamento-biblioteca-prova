import csv
import os


if not os.path.exists("livros.csv"): #Verifica se o arquivo "livros.csv" existe.
    with open("livros.csv", "w", newline="", encoding="utf-8") as catalogo: #Cria o arquivo "livros.csv" caso ele não exista.
        escritor = csv.writer(catalogo)
        escritor.writerow(['Titulo','Autor','Ano de publicação','código/ISBN','Status']) #Adiciona as colunas de cada livro no arquivo "livros.csv".

print("\n\nOlá, bom dia!")
print("Algoritmo de sistema de gerenciamento de biblioteca feito por Nicolas Robert de Vasconcellos Coutinho - 2°A.")

def cadastrar():
    with open("livros.csv", "a", newline="", encoding="utf-8") as catalogo:
        escritor = csv.writer(catalogo)
        print("\n----------------| CADASTRO DE LIVROS |----------------\n")
        titulo_livro = input("Digite o título do livro: ")
        autor_livro = input("Digite o autor do livro: ")
        ano_publicacao = input("Digite o ano de publicação do livro: ")
        codigo_isbn = input("Digite o código/ISBN do livro: ")
        status_livro = "Disponível" #Define o status inicial do livro como "Disponível" já que acabou de ser cadastrado.
        escritor.writerow([titulo_livro, autor_livro, ano_publicacao, codigo_isbn, status_livro]) #Insere as informações do livro no arquivo "livros.csv".
        print(f"\nO livro '{titulo_livro}' foi cadastrado com sucesso!")
        print("------------------------------------------------------")

def registrar_emprestimo():
    codigo_isbn = input("Digite o código/ISBN do livro que deseja pegar emprestado: ") #Solicita o código/ISBN para verificar se o livro está emprestado ou não.
    livros = [] #Lista para armazenar os livros cadastrados no sistema de biblioteca.
    livro_encontrado = False #Define o status do livro como não encontrado inicialmente para verificar se o livro existe no catálogo.
    print("\n----------------| REGISTRO DE EMPRÉSTIMO |----------------\n")
    with open("livros.csv", "r", newline="", encoding="utf-8") as catalogo:
        leitor = csv.DictReader(catalogo)
        for linha in leitor: #Percorre todas as linhas do arquivo "livros.csv" automaticamente
            if linha['código/ISBN'] == codigo_isbn: #Verifica se o código/ISBN é de algum livro cadastrado.
                livro_encontrado = True
                if linha['Status'] == "Disponível":
                    linha['Status'] = "Emprestado"
                    print(f"O livro '{linha['Titulo']}' foi emprestado com sucesso.")
                else:
                    print(f"O livro '{linha['Titulo']}' não está disponível para empréstimo no momento.")
            livros.append(linha) #Adiciona as informações do livro na lista "livros" para reescrever o arquivo "livros.csv" posteriormente.
    if not livro_encontrado: #Caso o livro não tenha sido encontrado, dá uma mensagem de erro pro usuário.
        print("Livro não encontrado no catálogo. Verifique se o código/ISBN está correto.")
    with open("livros.csv", "w", newline="", encoding="utf-8") as catalogo: #Reescreve o arquivo "livros.csv" com o empréstimo registrado.
        campos = ['Titulo', 'Autor', 'Ano de publicação', 'código/ISBN', 'Status'] #Informa o que deve conter no cabeçalho do arquivo "livros.csv"
        escritor = csv.DictWriter(catalogo, fieldnames=campos) #Define "fieldnames" como parâmetros para o cabeçalho do arquivo "livros.csv"
        escritor.writeheader()
        escritor.writerows(livros) #Reescreve as informações atualizadas dos livros.
    print("-------------------------------------------------------")

def registrar_devolucao():
    print("oi")

def listar_livros():
    with open("livros.csv", "r", newline="", encoding="utf-8") as catalogo: #Abre o arquivo "livros.csv" no modo de leitura.
        leitor = csv.DictReader(catalogo) #Lê o arquivo "livros.csv" em forma de dicionário, onde cada linha é representada por uma coluna.
        print("\n----------------| LISTA DE LIVROS |----------------\n")
        for linha in leitor: #Percorre todas as linhas do arquivo "livros.csv" automaticamente e imprime as informações de cada livro.
            print(f"Título: {linha['Titulo']}")
            print(f"Autor: {linha['Autor']}")
            print(f"Ano de publicação: {linha['Ano de publicação']}")
            print(f"Código/ISBN: {linha['código/ISBN']}")
            print(f"Status: {linha['Status']}\n")
        print("----------------------------------------------------")

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
            print("Encerrando o sistema...")
            break # Encerra o sistema caso o usuário escolha a opção 7.
        else:
            print("Opção inválida. Por favor, tente novamente.")
    except ValueError: # Caso o número digitado não seja inteiro, reinicia a tela do menu.
        print("Número digitado inválido. Por favor, insira um número inteiro. Tente novamente.")