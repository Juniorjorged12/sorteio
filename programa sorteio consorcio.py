import tkinter as tk
import random

nomes = []

def adicionar_nome():
    nome = entrada_nome.get()
    if nome and nome.lower() != "sair":
        nomes.append(nome)
        lista_nomes.config(text=f"Nomes: {', '.join(nomes)}")
    entrada_nome.delete(0, tk.END)

def sortear_nome():
    if nomes:
        resultado.config(text="Sorteando...")
        # Espera 3000 ms (3 segundos) e depois chama mostrar_resultado
        janela.after(3000, mostrar_resultado)
    else:
        resultado.config(text="Nenhum nome foi adicionado!")

def mostrar_resultado():
    sorteado = random.choice(nomes)
    resultado.config(text=f"O nome sorteado foi: {sorteado}")

# Criando janela principal
janela = tk.Tk()
janela.title("Sorteio de Nomes")

entrada_nome = tk.Entry(janela, width=30)
entrada_nome.pack(pady=5)

botao_adicionar = tk.Button(janela, text="Adicionar Nome", command=adicionar_nome)
botao_adicionar.pack(pady=5)

lista_nomes = tk.Label(janela, text="Nomes: ")
lista_nomes.pack(pady=5)

botao_sortear = tk.Button(janela, text="Sortear Nome", command=sortear_nome)
botao_sortear.pack(pady=10)

resultado = tk.Label(janela, text="")
resultado.pack(pady=10)

janela.mainloop()