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

# btn_mensagem = tk.Button(janela, text="Mensagem", command=calcular_media)
# btn_mensagem.grid(row=3, column=0, pady=10, padx=10)

# janela.mainloop()
