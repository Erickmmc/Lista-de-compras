import tkinter as tk

# Criar janela principal
janela = tk.Tk()
janela.title("Lista de Compras")
janela.geometry("400x400")  # Largura x Altura

# Funções


# Criando Label
lblLista = tk.Label(janela, text="Bem vindo(a) a lista de compras")
lblLista.pack()

rotulo_nome = tk.Label(janela, text="Nome do Produto:")
rotulo_nome.pack()

entrada_nome = tk.Entry(janela)
entrada_nome.pack()

rotulo_valor = tk.Label(janela, text="Valor do Produto:")
rotulo_valor.pack()

entrada_valor = tk.Entry(janela)
entrada_valor.pack()

lista_visual = tk.Listbox(janela, width=40)
lista_visual.pack()

def adicionar_produto():
    nome = entrada_nome.get().strip().title()
    valor = entrada_valor.get().strip()

    if nome and valor:
        try:
            valor_float = float(valor)
            lista_visual.insert(tk.END, f"{nome} - R$ {valor_float:.2f}")
            entrada_nome.delete(0, tk.END)
            entrada_valor.delete(0, tk.END)
        except ValueError:
            print("Valor inválido. Use apenas números.")

botao_adicionar = tk.Button(janela, text="Adicionar Produto", command=adicionar_produto)
botao_adicionar.pack()


# Inicia o loop da interface
janela.mainloop()

