# pergunta 1
# nick = input("Qual é o nome do jogador?...")
# nivel = int(input("Qual é o nível?..."))
# print(f"O jogador {nick} está o nível {nivel} e pronto para a partida!")

# pergunta 2
# print("Calculadora de Mesada")
# valor_semana = float(input("Quanto você ganha por semana?..."))
# total = valor_semana * 4
# print(f"Sua mesada no im do mês foi de... {total}")

# pergunta 3
# print("Conversor de Internet")
# gigi = float("Digite o valor em Gigabytes...")
# meg = gigi * 1024
# print(f"O valor convertido em Megabytes seria de... {meg}")

# pergunta 4
# print("Média das Notas")
# mat = float(input("Digite sua nota de Matematica"))
# port = float(input("Digite sua nota de Português"))
# media = (mat + port) / 2
# print(f"Sua média de Matematica e Português... {media}")

# pergunta 5
# seg_atual = int(input("Quantos seguidores você possui?"))
# seg_novos = int(input("Quantos novos você ganhou?"))
# seg_atualizado = seg_atual + seg_novos
# print(f"Você possui {seg_atualizado} um total atualizado de seguidores")

# pergunta 6
# print("Idades em Dias")
# idade = int(input("Digite sua idade"))
# idade_dias = idade * 365
# print(f"A quantidade de dias vividos são {idade_dias}")

# pergunta 7
# print("Consumo do Lanche")
# salgado = float(input("Qual o valor do salgado...?"))
# suco = float(input("Qual o valor do suco...?"))
# total = salgado + suco
# print(f"Sua compra ficou no valor de ... {total:.2f}")
# print("Sua compra foi um total de R$..." ,round(total,2))

# pergunta 8 
# print("Ano de Nascimento")
# ano_atual = int(input("Digite o ano do seu ano atual"))
# idade = int(input("Quantos você irá fazer esse ano?"))
# ano_nasc = ano_atual - idade
# print(f"O ano que você nasceu {ano_nasc}")

# pergunta 9
# print("Filtro de Idade (TikTok)")
# idade = int(input("Qual é sua idade...?"))

# if idade < 13:
#     print("Acesso Restrito!")
# elif 13 < idade < 17: #entre esse intervalo
#     print("Acesso Moderado")
# elif idade >= 18:
#     print("Acesso Liberado")
# else:
#     print("Idade Invalida")

# pergunta 10
# print("Bateria de Celular...Carregamento")
# import time
# bateria = 100

# while bateria > 10:
#     print(f"Bateria em {bateria}%")
#     bateria -= 10
#     time.sleep(1)
# print("Por favor conecte o carregador!")

# pergunta 11
# print("Contagem de Curtidas")
# import time
# limite = int(input("Diite a quantidade de curtidas"))
# for curtidas in range(1,limite + 1):
#     print(f"Curtida Nº {curtidas} recebidas!")
#     time.sleep(0.5)

# pergunta 12
# print("Carrinho de Compra Online")
# contador = 0
# produto = ""
# while produto.lower() != "sair":
#     produto = input("Digite o nome do produto")
#     contador += 1
#     if produto.lower() != "sair":
#         print(f"produto '{produto}' adicionado ao carrinho!")
# print(f"Compra finalizada você  adicionou {contador-1} itens ao seu carrinho!")
# print("obrigado por comprar conosco!")


# print("Carrinho de Compras Online - Versão 2.0")
# contador = 0
# produto = 0
# while produto != "sair":
#     contador =+ 1
#     produto = input("Digite o nome do produto ou sair para finalizar")
# print(f"Você adicionou {contador-1} itens ao carrinho")
# print("Obrigado por comprar conosco!")

# Registro de Veículo: Peça o modelo do veículo e a placa. ○ Exiba: "Veículo [Modelo] de placa [Placa] registrado no sistema. Boa viagem!

# def registrar_veiculo() -> Nome:
#     """Solicita dados do usuario e confirma o registro do veiculo."""
#     modelo = input("Digite o modelo do veiculo: ").strip()
#     placa = input("Digite a placa do veiculo: ").strip()

#    #O uso de f-strings tona a leitura muito mais clara e direita
#     print(f"\nVeiculo {modelo} de placa {placa} registrado no sistema. Boa Viagem!")
# if __name__ == "__main__":
#     registrar o veiculo 
