# Clean Code - Aula 6
# Para que usar?
# Como usar?
# print("Clean Code - Aula 6")
# aula = 6
# print(f"Estamos na aula {aula} de Clean Code")

# Manipulação de arquivos e Texto
# texto = "  Python é Muito legal!  "
# print(texto.strip().upper()) # "PYTHON"
# print(texto.strip().lower()) # "python"
# print(texto.strip().capitalize()) # "Python"
# print(texto.strip().title()) # "Python"
# print(texto.strip().replace(" ", "_")) # "Python"
# print(texto.strip().split()) # ["Python"]

# Escrevendo
# with open("notas.txt", "w") as arquivo:
#     arquivo.write("Estudar Pytohn hoje")
#     arquivo.write("\nLer sobre Clean Code")

# Lendo
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# Exercicio 1:
# Crie um programa que peça ao usuario para inserir uma frase e, e seguida, exiba a frase com as seguintes transformações:
# - Remova os espaços extras no inicio e no final da frase

# frase = input("Digie a sua frase")
# print(frase.strip().replace(" ", "_")) # "Python"

# jeito do professor
# frase = input("Digite uma frase: ")
# print(frase.strip())
# # - Converta a frase para letras maiúsculas.
# print(frase.strip().upper())

# Exemplo 1:
# Crie um programa que leia o conteúdo de um arquivo de texto e conte quantas vezess a palavra "Python" aparece no arquivo. Exiba o resultado para o usuario
# print("Contagem de palavras em arquivo")
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     contagem = conteudo.count("Python")
#     print(f"A contagem de palavras {contagem} é de...")

# Execução de comandos do sistema
import os # importa o módulo os para interagir com o sistema operracional
# Onde estou?
# print(os.getcwd())
# Listar arquivos na pasta
# print(os.listdir())
# print(os.listdir("..")) # lista arquivos da pasta pai
# print(os.listdir("..\\..")) # lista arquivos da pasta avô
# print(os.listdir("C:\\")) # lista arquios da raiz do C
# print(os.listdir("C:\\Users")) # lista arquivos da pasta Users
# print(os.listdir("C:\\Users\\Public")) # lista arquivos da pasta Pubilc

# Outros comandos úteis
# Criar pasta
# os.mkdir("nova_pasta")
# Renomear pasta
# os.rename("nova_pasta", "pasta_renomeada")
# Excluir pasta
# os.rmdir("pasta_renomeada")

# Exercicio 2
# Crie um script que mostre o caminho da pasta aual
# print(os.getcwd())

# exercico 3
# liste o arquivo da pasta atual
# print(os.listdir())

# Exercicio 4
# Crie uma pasta chamada "projetos" e depois renomeie para "meus_projetos". Por fim, exclua a pasta
# os.mkdir("projetos")
# os.rename("projetos", "meus_pojetos")
# os.rmdir("meus_projetoss")

# Exercicio 5:
# Crie um arquivo chamado "log.txt" e escreva a mensagem "Log de tividades". Depoi8s, leia o conteudo do arquivo e exiba a tela.
# with open("log.txt", "w") as arquivo:
#     arquivo.write("log de atividade")
# with open("log.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# Exemplo de dicionario:
# Crie um dicionario com informações sobre uma pessoa e acesse um valor usando ua chave

# pessoa = {
#     "nome": "Alice",
#     "idade": 30,
#     "cidade": "São Paulo",
#     "profissão": "Engenharia"
# }
# pessoa2 = {
#     "nome": "Bruno",
#     "idade": 25,
#     "cidade": "SP",
#     "profissão": "Designer"
# }
# print(pessoa["profissão"])
# print(pessoa2["nome"], pessoa["idade"])

# comida = {
#     "nome": "strogonoff",
#     "ingredientes": "frango" "batata-palha" "creme de leite",
#     "sabor": "frango",
# }

# Exemplo 2: desligar o PC (comando para Windows)
with open("desliar.bat", "w") as desligar:
    desligar.write("shutdown -s -t 3600 -c \"Desliamento programando para daqui a 1 hora. Salve se4u trabalho!\"")

#    # -s comando para desligar
#    # -t tempo definir
#    # -a cancelar desligamento