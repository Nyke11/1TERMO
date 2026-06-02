# Interface Gráfica TKINTER
# Componetes Principais (Widgets)

# tk: janela principal
# Label: texto ou rotulo
# Buton: um botão clicável
# Entry: um campo de entrada de texto

# import tkinter as tk
# from tkinter import messagebox

# 1. Criar a janela principal
# janela = tk.Tk()
# janela.title("Minha primeira janela GUI")
# janela.geometry("400x200") # Largura x Altura

# 2. Criar a Função que o botão irá executar
# def mostrar_mensagem():
#     messagebox.showinfo("Suceso!," "Você clicou no botão :)")

# 3. Criar os componetes
# lbl_titulo_pagina = tk.Label(janela, text="Bem-Vindo a aula de Interface Gráfica!", font=("Arial", 14, "bold"))
# lbl_titulo_pagina = tk.Label(janela, text=" AULA 12 Interface Gráfica!", font=("Arial", 14, "bold"))
# btn_clique_pagina = tk.Button(janela, text="Clique Aqui", font=("Arial", 14), bg="#ff5e00", fg="white", command=mostrar_mensagem)
# btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), bg)
# 4. Possiciona os componentes na jenela
# lbl_titulo_pagina.pack(pady=20) #pady adiciona espaçamento vertical
# btn_clique_pagina.pack(pady=10)
# btn_fechar_janela.pack(pady=10)

# 5. Rodar o loop da interface
# janela.mainloop()