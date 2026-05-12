# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
#
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código

#Passo 1

print("Seja bem-Vindo ao Shopping da MUNYKINHA")
print("escolha uma das opcções")
print("1 - Ticket \n2 - TAG \n3 - Interfone")
metodo_entrada = input("Ticket / TAG / interfone")

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
