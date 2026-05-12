# Exercício 1
# 1. Contador de Produção (for)
# Uma estreia processa 10 peças por ciclo. Crie um programa que use um for para contar de 1 a 10 e, para cada número, imprima: "Peças n X processada com sucesso".
# No final, exiba "Ciclo de produção cooncluído".

# for ciclo in range(1,11):
#     print(f"Peça nº {ciclo} processada com sucesso... :)")
# print("Ciclo de produção concluido... :)")

# Exercício 2
# Imagine a produção de frutas em feira. Desejo apresentar as frutas banana, manga, melancia, abacaxi. Com uma quantidade de 10 bananas, 5 mangas, 10 melancias e 13 abacaxi.
# No fim da produção gostaria de ter um total das produções.

for bananas in range(11):
    print(f"bananas Nº {bananas} foi...")
for mangas in range(6):
    print(f"mangas Nº {mangas} foi...")
for melancias in range(11):
    print(f"melancias Nº {melancias} foi...")
for abacaxi in range(13):
    print(f"abacaxi Nº {abacaxi} foi...")

total = bananas + mangas + melancias + abacaxi
print("A produção finaç foi:", total )
