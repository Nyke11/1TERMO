# Projeto Cancelas


print("Seja bem-Vindo ao Shopping da MUNYKINHA")
print("escolha uma das opcções")
print("1 - Ticket \n2 - TAG \n3 - Interfone")
metodo_entrada = input("Ticket / TAG / interfone")

try:
    if metodo_entrada == "Ticket":

        print("Seja Bem-Vindo ao Shopping da MUNYKINHA")
        hora_entrada = float(input("Digite a hora de entrada"))
        valor_estacionamento = float(input("Digite o valor a cobrar"))
        hora_saida = float(input("Digite a hora da saida"))
        total_permanencia = hora_saida - hora_entrada
        print(f"Seu tempo de permanência {total_permanencia} em horas")
        total_estacionamento = total_permanencia * valor_estacionamento
        print(f"O valor a ser cobrado foi de R${total_estacionamento:.2f}")

    elif metodo_entrada == "Tag":
        print("Bem-Vindo ao Shopping")
        print("Sua permanência no Shopping será cobrada na sua fatura")

    elif metodo_entrada == "Interfone":
        print("Bem-Vindo ao Shopping")
        print("Liberando acesso pelo Interfone")
        print("Sua saída deverá ser feita também pelo Interfone")

    else:
        print("Obrigado pela visita, volte sempre para o Shopping da MUNYKINHA")

except ValueError:
    print("Erro")