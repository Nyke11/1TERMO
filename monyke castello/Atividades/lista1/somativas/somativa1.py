# 1. Perfil de Gamer: Peça o nick (nome) do jogador e o nível atual. Exiba: "O
# jogador [nick] está no nível [nível] e pronto para a partida!"

# print("Sejam Bem-Vindos ao jogo")
# pergunta1 = input("Digite seu nome")
# pergunta2 = int(input("Digite o seu nivel"))
# print(f"o jogador" , pergunta1 , "está no nivel" , pergunta2 , "e pronto para a partida!")


# 2. Calculadora de Mesada: Peça o valor que o aluno ganha por semana e
# multiplique por 4 para mostrar quanto ele terá no final do mês.

# valor = float(input("quanto você ganha de mesada toda semana?"))
# print("no fim do mês você terá", valor * 4)


# 3. Conversor de Internet: Peça um valor em Gigabytes (GB) e converta para
# Megabytes (MB) (multiplique por 1024).

# print("peça um valor em gigabytes")
# gb = float(input("digite o valor gigabytes"))
# mb = gb * 1024
# print(f"{gb} GB equivalente a {mb} MB")


# 4. Média de Notas: Peça as notas de Matemática e Português. Calcule e mostre a
# média final.

# mat = float(input("digite a sua nota em matematica"))
# port = float(input("digite a sua nota em português"))
# media = (mat + port) /2
# print(f"A sua media final será {media}")


# 5. Seguidores: Peça a quantidade de seguidores atuais e quantos novos seguidores
# o aluno ganhou hoje. Exiba o total atualizado.

# seguidores_atuais = int(input("digite a quantidade de seguidor4es atuais"))
# novos_seguidores = int(input("quanos seguiodores você ganhou hoje"))
# soma = seguidores_atuais + novos_seguidores
# print(f"eu tenho {seguidores_atuais+novos_seguidores}")


# 6. Idade em Dias: Peça a idade do aluno e calcule aproximadamente quantos dias
# ele já viveu (idade * 365).

# idade = int(input("digite a sua idade do aluno: "))
# dias_vividos = idade * 365
# print(f"o aluno vive {dias_vividos} dias")


# 7. Consumo de Lanche: Peça o preço do salgado e o preço do suco. Exiba o valor
# total da conta.

# preço_salgado = float(input("digite o preço do salgado: "))
# preço_suco = float(input("digite o preço do suco: "))
# total = preço_salgado + preço_suco
# print(f"o valor total da compra é {total}")


# 8. Ano de Nascimento: Peça o ano atual e a idade do aluno. Calcule e exiba o ano
# em que ele nasceu.

# ano_atual = int(input("digite o ano autal: "))
# idade = int(input("digite a idade do aluno:"))
# ano_nascimento = ano_atual - idade
# print(f"o aluno nasceu no ano de {ano_nascimento}")


# 9. Filtro de Idade (TikTok): Peça a idade do usuário. Se for menor que 13, exiba
# "Acesso restrito". Se tiver entre 13 e 17, "Acesso moderado". Se for 18 ou
# mais, "Acesso liberado".

# idade = int(input("digite a idade do usuario"))
#  if idade < 13:
#      print("acesso restrito")
#  elif 13<= idade <= 17:
#     print("aceesso moderado")
#  else:
#      print("acesso liberado")


#  10.Bateria do Celular: Crie um while que começa com a bateria em 100. A cada
#  repetição, subtraia 10 e mostre: "Bateria em [valor]%". O loop para quando
#  chegar em 10 e exibe: "Por favor, conecte o carregador!".

#  bateria = 100
#  while bateria > 10:
#      print(f"bateria em {bateria}% ")
#      bateria -= 10
#  print("por favor, conecte ao carregador!")


# 11. Contagem de Curtidas: Use um for para simular a contagem de curtidas em uma
# foto. Peça ao usuário o limite de curtidas (ex: 5). O programa deve contar de 1 até
#  esse número, printando: "Curtida no [i] recebida!".

# limite = int(input("digite o limite de curtidas: "))
# for i in range(1, limite + 1):
#      print(f"curtida o [{i}] recebida! ")


# 12.Carrinho de Compras Online: Use um while para pedir nomes de produtos que o
# aluno quer comprar. O loop só para quando ele digitar "sair". No final, mostre
# quantas vezes ele adiciona itens ao carrinho (use um contador).

contador = 0
while True:
    produto = input("digite o nome do produto (ou 'sair' para encerrar): ")
    if produto.lower() == "sair":
        break
    contador += 1
print(f"foram acionados {contador} itens no carrinho")