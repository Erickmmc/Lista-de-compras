import json
import os
import unicodedata

#Testando push

# CAMINHO_BASE: caminho absoluto da pasta onde o script está localizado.
CAMINHO_BASE = os.path.dirname(os.path.abspath(__file__))

# CAMINHO_DADOS: caminho completo para o arquivo "dados.json" dentro da pasta do script.
CAMINHO_DADOS = os.path.join(CAMINHO_BASE, "dados.json")


# Adiciona um novo produto à lista com seu respectivo valor
def adiciona_produto(lista_de_produtos):
    print(" ")
    print("Qual é o produto?")
    produto = input().strip().capitalize()
    print("Qual é o valor?")
    valor = verifica_valor()
    lista_de_produtos[produto] = valor
    print(" ")
    print(f"O produto {produto} foi adicionado com o valor de R$ {valor:.2f} na sua lista")


# Remove um produto da lista, se ele existir
def remove_produto(lista_de_produtos):
    print(" ")
    print("Qual é o produto que deseja remover?")
    entrada_usuario = input().strip()
    produto_normalizado = normalizar(entrada_usuario)

    for nome_original in lista_de_produtos:
        if normalizar(nome_original) == produto_normalizado:
            if confirmacao_usuario("Remove", nome_original):
                del lista_de_produtos[nome_original]
                print(f"Produto '{nome_original}' removido com sucesso")
                return
            else:
                print("Ação cancelada")
                return

    print(f"Produto '{entrada_usuario}' não encontrado na lista")


# Exibe todos os produtos com seus respectivos valores
def exibir_produto(lista_de_produtos):
    print(" ")
    print("Produtos na sua lista:")
    for prod, val in lista_de_produtos.items():
        print(f"{prod}: R$ {val:.2f}")


# Mostra a quantidade de produtos e o valor total da lista
def contar_produto(lista_de_produtos):
    print(" ")
    valor_total = sum(lista_de_produtos.values())
    print(f"Você possui {len(lista_de_produtos)} produtos e a soma total é de R$ {valor_total:.2f}")


# Identifica e exibe o produto mais caro da lista
def produto_mais_caro(lista_de_produtos):
    produto_mais_caro = max(lista_de_produtos.items(), key=lambda item: item[1])
    print(f"Produto mais caro: {produto_mais_caro[0]} - R$ {produto_mais_caro[1]:.2f}")


# Identifica e exibe o produto mais barato da lista
def produto_mais_barato(lista_de_produtos):
    print(" ")
    produto_mais_barato = min(lista_de_produtos.items(), key=lambda item: item[1])
    print(f"Produto mais barato: {produto_mais_barato[0]} - R$ {produto_mais_barato[1]:.2f}")


# Retorna a lista ordenada alfabeticamente por nome
def organizar_por_nome(lista_de_produtos):
    print(" ")
    print("Lista organizada por nome")
    return dict(sorted(lista_de_produtos.items()))


# Retorna a lista ordenada do produto mais barato para o mais caro
def organizar_por_valor(lista_de_produtos):
    print(" ")
    print("Lista organizada por valor")
    return dict(sorted(lista_de_produtos.items(), key=lambda item: item[1]))


# Permite ao usuário alterar o valor de um produto já existente
def alterar_valor(lista_de_produtos):
    print(" ")
    print("Qual item deseja alterar?")
    entrada_usuario = input().strip()
    produto_normalizado = normalizar(entrada_usuario)

    for nome_original in lista_de_produtos:
        if normalizar(nome_original) == produto_normalizado:
            if confirmacao_usuario("Altera", nome_original):
                print("Qual é o novo valor do item?")
                novo_valor = verifica_valor()
                lista_de_produtos[nome_original] = novo_valor
                print(f"O valor de '{nome_original}' foi atualizado para R$ {novo_valor:.2f}")
                return
            else:
                print("Ação cancelada")
                return

    print("Item não encontrado")


# Salva a lista de produtos no arquivo JSON
def salvar_em_arquivo(lista_de_produtos):
    with open(CAMINHO_DADOS, "w", encoding="utf-8") as dados:
        json.dump(lista_de_produtos, dados, indent=2, ensure_ascii=False)
        print("Lista salva com sucesso")


# Carrega os dados do arquivo JSON, se ele existir
def carregar_do_arquivo():
    if os.path.exists(CAMINHO_DADOS):
        with open(CAMINHO_DADOS, "r", encoding="utf-8") as dados:
            lista_carregada = json.load(dados)
            print("Lista carregada com sucesso")
            return lista_carregada
    else:
        return {}


# Exibe uma mensagem de erro caso o comando do menu seja inválido
def mensagem_de_erro():
    print(" ")
    print("Comando inválido! Por favor, digite um número de 1 a 10.")


# Valida se o valor digitado é um número (float). Repete até o usuário digitar corretamente.
def verifica_valor():
    while True:
        try:
            return float(input())
        except ValueError:
            print(" ")
            print("Valor inválido! Digite apenas números usando ponto para separar decimais.")


# Normaliza o texto removendo acentos, espaços extras e deixando em minúsculo
def normalizar(texto):
    return unicodedata.normalize("NFKD", texto) \
                      .encode("ASCII", "ignore") \
                      .decode("ASCII") \
                      .lower() \
                      .strip()

# Confirma se o usuário deseja mesmo realizar essa ação
def confirmacao_usuario(acao, nome_item):
    print(" ")
    if acao == "Remove":
        resposta = input(f"Você deseja prosseguir com remoção do item '{nome_item}'? (s/n) ").strip().lower()
    elif acao == "Altera":
        resposta = input(f"Você deseja alterar o valor do produto '{nome_item}'? (s/n) ").strip().lower()
    else:
        return False  # Caso a ação não seja reconhecida

    return resposta == "s"
