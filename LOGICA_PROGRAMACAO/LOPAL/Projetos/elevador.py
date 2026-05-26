# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade
#  de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando).
# O programa deve continuar rodando até que o usuário decida encerrar.

# Movimento do elevador
# botão, para saber onde o elevador deve parar 
# reconhecer quando der problema
# sensor para a porta

# print("Sejam Bem-Vindos ao Condomínio Park MUNYKINHA Residence")
# andar_atual = 0
# limite_pessoas = 5
# qtd_pessoas = 0
# while True:
#     qtd = int(input(f"Quantas pessoas vão entrar no elevador? (Limite {limite_pessoas}) (Digite 0 para pular:"))
#     if qtd < 0:
#         print("Valor invalido")
#         continue
#     if qtd_pessoas + qtd > limite_pessoas:
#         print("Valoe invalido")
#         continue
#     if qtd > 0:
#         qtd_pessoas += qtd
#         print(f"Agora tem {qtd_pessoas} pessoas (s) no elevador.")

#     destino = int(input("Digite o andar que deseja ir (0 a 20) ou -1 para sair : "))
#     if destino == -1:
#         print("Elevador desligado")
#         break
#     if destino < 0 or destino > 20:
#         print("Andar invalido")

#     print("/n Portas fechadas...")

#     while andar_atual != destino:
#       if andar_atual < destino:
#         andar_atual += 1
#         print(f"Subindo... andar:,{andar_atual}° andar | Aviso: Subindo!")
#     else:
#        andar_atual -= 1
#     print("Descendo... Andar:, {andar_atual}° andar | Aviso: Descendo!")
    
# print("Você chegou ao seu andar!! Portas Abertas. \n")

# Elevador do Bruno

# print("Bem-vindo ao Elevador Python!")
# andar_atual = 0
# while True:
#     try:
#         destino = int(input("Digite o andar de destino (0-10): "))
#         if destino < 0 or destino > 10:
#             raise ValueError("Andar inválido. Por favor, digite um número entre 0 e 10.")
        
#         print(f"Elevador se movendo do andar {andar_atual} para o andar {destino}...")
#         andar_atual = destino
#         print(f"Chegamos ao andar {andar_atual}!")

#         if input("Deseja escolher outro andar? (s/n): ").lower() != 's':
#             print("Obrigado por usar o Elevador Python! Até a próxima!")
#             break
#         for listagem in range(10):
#             print(f"Andar {listagem} - {'[X]' if listagem == andar_atual else '[ ]'}")

#     except ValueError as ve:
#         print(f"Erro: {ve}. Tente novamente.")
#     except Exception as e:
#         print(f"Ocorreu um erro inesperado: {e}. Tente novamente.")
#         print("Programa encerrado.")
#         break