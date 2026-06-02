# Projeto de Revisão: Sistema de Empréstimo "Biblioteca Digital"

import tkinter as tk
from tkinter import messagebox


def janela_bemvindo():
    aluno = aluno_usuario.get()
    nome_do_livro = nome_do_livro_usuario.get()
    comunidade = comunidade_usuario.get()

    if aluno == "" and nome_do_livro == "":
        messagebox.showwarning("aviso", "Digite seu nome :)")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá aluno, {aluno} - Seja bem-vindo a biblioteca")

    if comunidade == "":
        messagebox.showwarning("aviso", "Digite sim se for da comunidade")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá comunidade, {comunidade} - seja bem-vindo a biblioteca")
    
    
janela = tk.Tk()
janela.title("Exemplo 2")
janela.geometry("800x400")
janela.configure(bg="#FF5E46")

lbl_aluno = tk.Label(janela, text="Digite seu nome :)")
lbl_nome_do_livro = tk.Label(janela, text="Digite o nome do livro :)")
lbl_comunidade = tk.Label(janela, text="Digite sim se for da comunidade")

lbl_aluno.grid(row=0, column=0, pady=10, padx=10)
lbl_nome_do_livro.grid(row=1, column=0, pady=10, padx=10)
lbl_comunidade.grid(row=2, column=0, pady=10, padx=10)

aluno_usuario = tk.Entry(janela, font=("Arial", 12))
aluno_usuario.grid(row=0, column=1, pady=10, padx=10)

nome_do_livro_usuario = tk.Entry(janela, font=("Arial", 12))
nome_do_livro_usuario.grid(row=1, column=1, pady=10, padx=10)

comunidade_usuario = tk.Entry(janela, font=("Arial", 12))
comunidade_usuario.grid(row=2, column=1, pady=10, padx=10)

btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
btn_mensagem.grid(row=3, column=0, pady=10, padx=10)

janela.mainloop()