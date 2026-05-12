# Exercícios de Programação Python: "O Caça-Erros"

# 1. O Problema da Idade
# Erro
# idade = input("Digite sua idade:")
# if idade >= 18:
#     print("Você é maior de iudade")

# Corrigido
# idade = int(input("Digite sua idade"))
# if idade >= 18:
#     print("Você é maior de idade")

# Melhorado
# idade = int(input("Digite sua idade:"))
# if idade >= 18:
#     print("Você é maior de idade")
# else:
#     print("Você é menor de idade")

# 2. A Escrita Fiel
# Erro
# nome="Mariana"
# print("Seja bem-vinda,nome!")

# Corrigido
# nome = "Mariana"
# print(f"Seja bem-vinda, {nome}!")

# Melhorado
# nome = "Mariana"
# print("=" * 30)
# print(f" Seja muito bem-vinda, {nome}!")
# print("=" * 30)

# 3. Falta de Espaço
# Erro
# numero = 10
# if numero > 5:
# print("O número é maior que cinco.")
# else:
# print("O número é menor ou igual a cinco.")

# Corrigido
# numero = 10
# if numero > 5:
#     print("O número é maior que cinco.")
# else:
#     print("O número é menor ou igual a cinco.")

# Melhorado
# numero = int(input("Digite um numero: "))
# if numero > 5:
#     print(f"O numero {numero} é maior que cinco. ")
# else:
#     print(f"O numero é menor {numero} ou igual que cinco. ")

# 4. Esquecimento Fatal
# Erro
# usuario = "aluno123"
# if usuario == "aluno123"
#    print("Login realizado com sucesso.")

# Corrigido
# usuario = "aluno123"
# if usuario == "aluno123":
#     print("Login realizado com sucesso.")

# Melhorado
# usuario = input("Digite seu usuario: ")
# if usuario == "aluno123":
#      print("Login realizado com sucesso.")
# else:
#      print("Usuario incorreto. Tente novamente")

# 5. Atribuição vs. Comparação
# Erro
# clima = "ensolarado"
# if clima = "chuvoso":
#    print("Leve um guarda-chuva!")

# Corrigido
# clima = "ensolarado"
# if clima == "chuvoso":
#    print("Leve um guarda-chuva!")

# Melhorado
# clima = input("Como está o Clima hoje? "). lower()
# if clima == "chuvoso":
#     print("Leve um guarda-chuva! ")
# elif clima == "ensolarado":
#     print("Está ensolarado")
# else:
#     print("Clima frio")

# 6. Misturando Alhos com Bugalhos
# Erro
# pontos = 50
# print("Parabéns! Você fez " + pontos + " pontos.")

# Corrigido
# pontos = 50
# print(f"Parabéns! Você fez " + str(pontos) + " pontos.")

# Melhorado
# pontos = int(input("Digite a quantidade de pontos: "))
# print(f"Parabéns! Você fez {pontos} pontos.")

# 7. A Ordem dos Fatores
# O sistema deve dar "Excelente" para notas 9 ou 10.
# Erro
# nota = 9.5
# if nota >= 7:
#    print("Aprovado")
# elif nota >= 9:
#    print("Excelente!")

# Corrigido
# nota = 9.5
# if nota >= 7:
#     print("Aprovado")
#     if nota >= 9:
#         print("Excelente")

# Melhorado
# nota = float(input("Digite a nota do aluno: "))
# if nota >= 7:
#     print("Aprovado")
#     if nota >= 9:
#         print("Excelente")
# elif nota >= 5:
#     print("Recuperção")
# else:
#     print("Reprovado")

# 8. O Contador de 1 a 5
# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.
# # Erro
# for i in range(5):
#   print(i)

# Corrigido
# for i in range(1, 6):
#     print(i)

# Melhorada
# print("Contador de 1 a 5:")
# for numero in range(1,6):
#     print(numero)

# 9. O Loop Eterno
# Erro
# tentativas = 1
# while tentativas <= 3:
#   print("Tentando conectar...")
#    O código deveria parar após 3 tentativas

# Corrigido
# tentativas = 1
# while tentativas <= 3:
#     print("Tentando conectar...")
#     tentativas = tentativas + 1

# Melhorado
# tentativas = 1
# while tentativas <= 3:
#     print(f"tentativas {tentativas}: tentando conectar...")
#     tentativas += 1
#     print("\n Numero maximo de tentativas atingida. Processo finalizado")

# 10. A Senha Teimosa
# O programa deve pedir a senha até que o usuário digite "python123"
# Erro
# senha = ""
# while senha == "python123":
#   senha = input("Digite a senha secreta: ")
# print("Acesso concedido!")

# Corrigido
# senha = ""
# while senha != "python123":
#     senha =input("Digite a senha secreta: ")
# print("Acesso concedido!")

# Melhorado
# senha = ""
# while senha != "python123":
#     senha = input("Digite a senh secreta: ")
#     if senha != "python123":
#         print("Senha incorreta, tente novamente: ")
# print("\n Aceso concedido!")