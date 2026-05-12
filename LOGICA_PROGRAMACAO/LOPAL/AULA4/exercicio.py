# Exercicio 1
# Tente criar um código que conte de 1 a 10, mas use o continue para não imprimir o número 5 (simulando uma falha de ensor específicca no item 5).
 
# for sensor in range(1,11):
#     if sensor == 5:
#         print(f"Sensor nº{sensor}com falha")
#     print(f"Sensor {sensor} sem falha")
#     continue
# print("Fim! :)")


# Exercício 2
# Simule um semáforo com parada para cada cor. Determine um tempo que deseja para quando mudar para tal cor ele represente uma pausa cada cor. Use o continue para pular
# a cor amarela (simulando um semáfaro com defeito que não acende a luz amarela).

# import Time
# cores = ["Verde", "Amarelo", "Vermelho"]
# for cor in cores:
#      if cor == "Amarelo":
#          print(f"Semáfaro com defeito, pulando a cor {cor}...")
#          continue # pule a cor Amarela
#      print(f"Semáfaro na cor {cor}. Parando por 3 segundos...")
#      time.sleep(3) # Simule a pausa para cada cor
#  print("Fim do ciclo do semáfaro")


# Exercicio 3 - Soma de Cargas de Energia (for)
# uma fabrica tem 5 maquinas. Peça ao usuario (via input dentro do loop) o consumo em kwh de cada uma das maquinas 5. Ao final do loop,
# o programa deve exibir o consumo total da fabrica.

# total_consumo = 0
# for maquina in range(1,6):
#      consumo = float(input(f"Digite o consumo em khw da máquina {máquina}")):
#      total_consumo += consumo # Acumula o consumo total
# print(f"O consumo total da fábrica é de {total_consumo} kwh.")