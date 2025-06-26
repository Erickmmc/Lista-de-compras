import tkinter as tk
from os.path import exists
from functions import salvar_em_arquivo, carregar_do_arquivo

# Criar janela principal
janela = tk.Tk()
janela.title("Lista de Compras")
janela.geometry("400x400")  # Largura x Altura

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


# Funções
lista_de_produtos = {}

if exists("dados.json"):
    lista_de_produtos = carregar_do_arquivo()

for produto, valor in lista_de_produtos.items():
    lista_visual.insert(tk.END, f"{produto} - R$ {valor:.2f}")

def adicionar_produto():
    nome = entrada_nome.get().strip().title()
    valor = entrada_valor.get().strip()

    if nome and valor:
        try:
            valor_float = float(valor)

            # ✅ Atualiza o dicionário
            lista_de_produtos[nome] = valor_float

            # ✅ Atualiza a Listbox
            lista_visual.insert(tk.END, f"{nome} - R$ {valor_float:.2f}")

            # ✅ Salva automaticamente
            salvar_em_arquivo(lista_de_produtos)

            # ✅ Limpa os campos
            entrada_nome.delete(0, tk.END)
            entrada_valor.delete(0, tk.END)

        except ValueError:
            print("Valor inválido. Use apenas números.")


botao_adicionar = tk.Button(janela, text="Adicionar Produto", command=adicionar_produto)
botao_adicionar.pack()

botao_salvar = tk.Button(janela, text="Salvar lista", command=lambda: salvar_em_arquivo(lista_de_produtos))
botao_salvar.pack()

# Inicia o loop da interface
janela.mainloop()

