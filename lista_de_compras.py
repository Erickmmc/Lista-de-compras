
"""
Programa: Lista de Compras Interativa
Descrição: Permite ao usuário adicionar, remover, listar e ordenar produtos com seus valores.
Autor: Erick Cruz
Data: Junho/2025
"""
# Imports
from os.path import exists
from functions import *

# Inicialização com variável para controle de comando.
comando = 0

# Lista para iniciar o cógido e testar funcionalidades.
lista_de_produtos = {}

# Carrega o arquivo de dados, se existir.
if exists("dados.json"):
    lista_de_produtos = carregar_do_arquivo()

# Loop principal, que começa em 0.
while comando != 9:
    # Exibição de menu.
    print(" ")
    print("O que deseja fazer?")
    print("1. Adicionar um produto e valor")
    print("2. Remover um produto")
    print("3. Listar produtos")
    print("4. Total")
    print("5. Produto mais caro")
    print("6. Produto mais barato")
    print("7. Ordenar por nome")
    print("8. Ordenar por valor")
    print("9. Sair")
    print("10. Alterar valor do item")
    print(" ")
    
    try:
        comando = int(input())
    except ValueError:
        mensagem_de_erro()
        continue

    if comando == 1:
    # Adiciona um novo produto
        adiciona_produto(lista_de_produtos)

    elif comando == 2:
    # Remove um produto da lista verificando se ele existe
        remove_produto(lista_de_produtos)

    elif comando == 3:
    # Exibe todos os produtos na minha lista
        exibir_produto(lista_de_produtos)    

    elif comando == 4:
    # Faz a contagem de itens e a soma dos valores
        contar_produto(lista_de_produtos)

    elif comando == 5:
    # Exibe qual é o produto mais caro da lista
        produto_mais_caro(lista_de_produtos)

    elif comando == 6:
    # Exibe qual é o produto mais barato da lista
        produto_mais_barato(lista_de_produtos)

    elif comando == 7:
    # Organiza os itens da lista por nome
        lista_de_produtos = organizar_por_nome(lista_de_produtos) 

    elif comando == 8:
    # Organiza os itens da lista por valor
        lista_de_produtos = organizar_por_valor(lista_de_produtos)

    elif comando == 9:
    # Finaliza o programa
        print(" ")
        salvar_em_arquivo(lista_de_produtos)
        print("Até mais!")
    
    elif comando == 10:
    # Altera valor de um item da lista
        alterar_valor(lista_de_produtos)    

    else:
    # Informa que o comando utilizado é inválido (Não é de 1 a 9)
        mensagem_de_erro()