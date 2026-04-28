# 1. O Laço 'for' (Repetições Determinadas)
# Use 'for' quando você sabe exatamente quantas vezs algo deve acontecer (como ler 10 sensores ou processar uma lista de peças).
# Exemplo: Relatório de Produção Diária
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# Exemplo 1
# for lote in range(1, 6):
#     print(f"Processando lote número {lote}...")
#     print("Qualidade  Verificada. [OK]")
#     print("Produção do dia finalizada!")

# # Exemplo 2
# for b in range(10):
#     print(f"Quantidade total {b} foi...")

# Exemplo 3
# Imagine o seguinte cenário, iremos produzir 20 discos de vinil.
for discos in range(21):
    print(f"quantidade de discos de vinil {discos} foi...")

# Exemplo 4
peças = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo", "Pregos", "Martelo", "Chave de Fenda"]
itempeças = ["Cilindricas", "Eixo Cônicos", "Radiais", "Madeira" "Bola", "Cabeça Chata", "Chave Metalica Verde" ]
for item in peças:
    print(f"Item em estoque: {item} e {itempeças}")
    for item2 in itempeças:
        print(f"Item de peças em estoque: {itempeças}")


# Exemplo 5
# Imagine a seguinte situaçaõ gostria de ter um menu onde pudesse perguntar qual opção voc~e deseja da seleção ele listar os produtos

print("Bem-Vindos a loja da MUNIKYNHA")
print("Opção 1- Roupas")
print("Opção 2- Sapatos")
menu = int(input("Escolha uma opção"))

Roupas = ["Blusa", "Croopd", "Saias"]
Sapatos = ["Tênis", "Papetes", "Botas"]

if menu == 1:
    for item1 in Roupas:
        print(f"Sua lista de Roupas {Roupas} são...")
elif menu == 2:
    for item2 in Sapatos:
        print(f"Sua lista de Sapatos {Sapatos} são...")
else:
    print("Opção inválida: Encerrando o sistema")

