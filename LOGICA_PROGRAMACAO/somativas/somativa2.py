# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# import tkinter as tk
# from tkinter import messagebox

# def janela_bemvindo():
#    nome = nome_operador.get()
#    turno = turno_do_operador.get()

#    if nome == "":
#         messagebox.showwarning("aviso", "Digite seu nome :)")
#    else:
#         messagebox.showinfo("Operador", f"{nome}")

#    if turno == "A" or turno == "B" or turno == "C":
#        messagebox.showwarning("Aviso", "Digite seu turno :)")
#    else:
#        messagebox.showinfo("Operador", f"{nome} registrado no {turno} Bom Trabalho!!")

# janela = tk.Tk()
# janela.geometry("800x400")
# janela.configure(bg="#FF5E46")

# lbl_nome = tk.Label(janela, text="Digite seu nome :)")
# lbl_nome.grid(row=0, column=0, pady=10, padx=10)
# lbl_turno = tk.Label(janela, text="Digite seu turno :)")
# lbl_turno.grid(row=1, column=0, pady=10, padx=10)

# nome_operador = tk.Entry(janela, font=("Arial", 12))
# nome_operador.grid(row=0, column=1, pady=10, padx=10)

# turno_do_operador = tk.Entry(janela, font=("Arial", 12))
# turno_do_operador.grid(row=1, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)

# janela.mainloop()

# 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.

# import tkinter as tk
# from tkinter import messagebox

# def calculador_peças():
#     peças = calcular_peças.get()

#     if peças == "":
#         messagebox.showwarning("")
#     else:
#         peças = int(calcular_peças.get())
#         total = peças * 8
#         messagebox.showinfo("Resultado", f"Em 8 horas foram feitas {total} peças")

# janela = tk.Tk()
# janela.geometry("800x400")
# janela.configure(bg="#FF5E46")

# lbl_calcular_peças = tk.Label(janela, text="Digite a quantidade de peças :)")
# lbl_calcular_peças.grid(row=0, column=0, pady=10, padx=10)

# calcular_peças = tk.Entry(janela, font=("Arial", 12))
# calcular_peças.grid(row=0, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Mensagem", command=calculador_peças)
# btn_mensagem.grid(row=1, column=0, pady=10, padx=10)

# janela.mainloop()

# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.

# import tkinter as tk
# from tkinter import messagebox

# def conversor_de_unidade():
#     bar = int(PSI_unidade.get())

#     if bar == "":
#         messagebox.showwarning("")
#     else:
#         total = bar * 14.5
#         messagebox.showinfo("Resultado", f"Foi convertido para decimais {total}")

# janela = tk.Tk()
# janela.geometry("800x400")
# janela.configure(bg="#FF5E46")

# lbl_PSI_unidade = tk.Label(janela, text="Digite o valor em bar :)")
# lbl_PSI_unidade.grid(row=0, column=0, pady=10, padx=10)

# PSI_unidade = tk.Entry(janela, font=("Arial", 12))
# PSI_unidade.grid(row=0, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Mensagem", command=conversor_de_unidade)
# btn_mensagem.grid(row=1, column=0, pady=10, padx=10)

# janela.mainloop()

# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.

# import tkinter as tk
# from tkinter import messagebox

# def calcular_media():
#     nota1 = int(campo_nota1.get())
#     nota2 = int(campo_nota2.get())
#     nota3 = int(campo_nota3.get())

#     media  = (nota1 + nota2 + nota3) /3

#     if nota1 == "" or nota2 == "" or nota3 == "":
#         messagebox.showwarning("Resultado" f"{media} numero de peças aprovada!!")
#     else:
#         messagebox.showinfo("Resultado", f"{media} numero de peças reprovada!!")

# janela = tk.Tk()
# janela.geometry("800x400")
# janela.configure(bg="#FF5E46")

# lbl_campo_nota1 = tk.Label(janela, text="Digite a primeira nota :)")
# lbl_campo_nota1.grid(row=0, column=0, pady=10, padx=10)

# lbl_campo_nota2 = tk.Label(janela, text="Digite a segunda nota :)")
# lbl_campo_nota2.grid(row=1, column=0, pady=10, padx=10)

# lbl_campo_nota3 = tk.Label(janela, text="Digite a terceira nota :)")
# lbl_campo_nota3.grid(row=2, column=0, pady=10, padx=10)

# campo_nota1 = tk.Entry(janela, font=("Arial", 12))
# campo_nota1.grid(row=0, column=1, pady=10, padx=10)

# campo_nota2 = tk.Entry(janela, font=("Arial", 12))
# campo_nota2.grid(row=1, column=1, pady=10, padx=10)

# campo_nota3 = tk.Entry(janela, font=("Arial", 12))
# campo_nota3.grid(row=2, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Enviar", command=calcular_media)
# btn_mensagem.grid(row=3, column=0, pady=10, padx=10)

# janela.mainloop()

# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# import tkinter as tk
# from tkinter import messagebox

# def verificar_temperatura():
#     temperatura = float(entrada.get())

#     if temperatura <40:
#         messagebox.showwarning("Resultado", "Baixa carga")

#     if temperatura <= 70:
#         messagebox.showwarning("Resultado", "Normal")
        
#     else:
#          messagebox.showinfo("ALERTA" "Resframento ativado")

# janela = tk.Tk()
# janela.geometry("800x400")
# janela.configure(bg="#FF5E46")

# lbl_entrada = tk.Label(janela, text="Digite a temperatura :)")
# lbl_entrada.grid(row=0, column=0, pady=10, padx=10)

# entrada = tk.Entry(janela, font=("Arial", 12))
# entrada.grid(row=0, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Enviar", command=verificar_temperatura)
# btn_mensagem.grid(row=1, column=0, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Fechar", command=verificar_temperatura)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)

# janela.mainloop()

# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

# import tkinter as tk
# from tkinter import messagebox

# def classificar():
#     alimentos = codigoA.get()
#     eletronicos = codigoE.get()
   
#     if alimentos == "A":
#          messagebox.showwarning("Resultado", "Alimentos")

#     if eletronicos == "E":
#         messagebox.showwarning("Resultado", "Eletrônicos")

#     else:
#         messagebox.showinfo("Alerta","Lote não encontrado")

# janela = tk.Tk()
# janela.geometry("800x400")
# janela.configure(bg="#FF5E46")

# lbl_codigoA = tk.Label(janela, text="Digite A para alimentos :)")
# lbl_codigoA.grid(row=0, column=0, pady=10, padx=10)

# codigoA = tk.Entry(janela, font=("Arial", 12))
# codigoA.grid(row=0, column=1, pady=10, padx=10)

# lbl_codigoE = tk.Label(janela, text="Digite E para eletrônicos :)")
# lbl_codigoE.grid(row=1, column=0, pady=10, padx=10)

# codigoE = tk.Entry(janela, font=("Arial", 12))
# codigoE.grid(row=1, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Enviar", command=classificar)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Fechar", command=classificar)
# btn_mensagem.grid(row=3, column=0, pady=10, padx=10)

# janela.mainloop()

# 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.

# import tkinter as tk
# from tkinter import messagebox

# def verificar_maquina():
#     sensor_porta = porta_fechada.get()
#     botao_emergencia = porta_desligando.get()

#     if sensor_porta == "fechada" and  botao_emergencia == "desligado":
#         messagebox.showwarning("Resultado", "A maquina não pode iniciar")

#     else:
#         messagebox.showerror("ALERTA", "Maquina não pode iniciar")

# janela = tk.Tk()
# janela.geometry("800x400")
# janela.configure(bg="#FF5E46")

# lbl_porta_fechada = tk.Label(janela, text="Sensor da maquina (fechada/aberta) :)")
# lbl_porta_fechada.grid(row=0, column=0, pady=10, padx=10)

# porta_fechada = tk.Entry(janela, font=("Arial", 12))
# porta_fechada.grid(row=0, column=1, pady=10, padx=10)

# lbl_porta_desligando = tk.Label(janela, text="Botão de Emergência ligado/desligado :)")
# lbl_porta_desligando.grid(row=1, column=0, pady=10, padx=10)

# porta_desligando = tk.Entry(janela, font=("Arial", 12))
# porta_desligando.grid(row=1, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Enviar", command=verificar_maquina)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="fechar", command=verificar_maquina)
# btn_mensagem.grid(row=3, column=0, pady=10, padx=10)

# janela.mainloop()

# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".

# import tkinter as tk
# from tkinter import messagebox

# def calcular_descarte():
#     total = int(entrada_total.get())
#     descarte = int(entrada_descarte.get())

#     percentual = (descarte/total)*100

#     if percentual <5:
#          messagebox.showwarning("Resultado", "revisar processo")

#     else:
#          messagebox.showinfo("Resultado",f"{percentual} processo otimizado")

# janela = tk.Tk()
# janela.geometry("800x400")
# janela.configure(bg="#FF5E46")

# lbl_entrada_total = tk.Label(janela, text=" Digite total de peças produzidas:)")
# lbl_entrada_total.grid(row=0, column=0, pady=10, padx=10)

# entrada_total= tk.Entry(janela, font=("Arial", 12))
# entrada_total.grid(row=0, column=1, pady=10, padx=10)

# lbl_entrada_descarte = tk.Label(janela, text=" Digite total de peças com defeito :)")
# lbl_entrada_descarte.grid(row=1, column=0, pady=10, padx=10)

# entrada_descarte = tk.Entry(janela, font=("Arial", 12))
# entrada_descarte.grid(row=1, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Enviar", command=calcular_descarte)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="fechar", command=calcular_descarte)
# btn_mensagem.grid(row=3, column=0, pady=10, padx=10)

# janela.mainloop()

# 9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo.

# import tkinter as tk
# from tkinter import messagebox

# def validar_medida():
#     medida = float(valor_da_medida.get())

#     if 9.8 <= medida <=10.2:
#         messagebox.showwarning("Resultado", "Dentro da tolerância")

#     if medida <=9.8:
#          messagebox.showwarning("Resultado", "Abaixo da tolerância")

#     else:
#         messagebox.showwarning("Resultado", "Acima da tolerância")

# janela = tk.Tk()
# janela.geometry("800x400")
# janela.configure(bg="#FF5E46")

# lbl_valor_da_medida = tk.Label(janela, text=" Digite a medida da peça :)")
# lbl_valor_da_medida.grid(row=0, column=0, pady=10, padx=10)

# valor_da_medida = tk.Entry(janela, font=("Arial", 12))
# valor_da_medida.grid(row=0, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Enviar", command=validar_medida)
# btn_mensagem.grid(row=1, column=0, pady=10, padx=10)

# janela.mainloop()

# 10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
# de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".

# import tkinter as tk
# from tkinter import messagebox

# def contage_regressiva():
#     for numero in range(10, 0, -1):
#         messagebox.showwarning("Contagem Regressiva", f"{numero}")
    
#     if numero >5:
#         messagebox.showwarning(f"contagem: {numero}")

#     else:
#         messagebox.showinfo("Resultado", "Prensa Ativada")

# janela = tk.Tk()
# janela.geometry("800x400")
# janela.configure(bg="#FF5E46")

# numero = tk.Label(janela, text="  :)")
# numero.grid(row=0, column=0, pady=10, padx=10)

# numero = tk.Entry(janela, font=("Arial", 12))
# numero.grid(row=0, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Enviar", command=contage_regressiva)
# btn_mensagem.grid(row=1, column=0, pady=10, padx=10)

# janela.mainloop()