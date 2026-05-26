from modulos.arquivos import salvar_dados


def cadastrar_produto(dados, nome, categoria, preco, quantidade):

    dados["ultimo_id"] += 1

    produto = {
        "id": dados["ultimo_id"],
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }

    dados["produtos"].append(produto)

    salvar_dados(dados)

    print("\nProduto cadastrado com sucesso!")


def buscar_produto(dados, produto_id):

    for p in dados["produtos"]:
        if p["id"] == produto_id:
            return p

    return None


def registrar_entrada(dados, produto_id, quantidade):

    produto = buscar_produto(dados, produto_id)

    if produto:
        produto["quantidade"] += quantidade
        salvar_dados(dados)

        print("Entrada registrada.")

    else:
        print("Produto inexistente.")


def registrar_saida(dados, produto_id, quantidade):

    produto = buscar_produto(dados, produto_id)

    if not produto:
        print("Produto inexistente.")
        return

    if produto["quantidade"] < quantidade:
        print("Estoque insuficiente.")
        return

    produto["quantidade"] -= quantidade

    salvar_dados(dados)

    print("Saída registrada.")


def consultar_estoque(dados, produto_id):

    produto = buscar_produto(dados, produto_id)

    if produto:

        print("\n------ PRODUTO ------")

        for k, v in produto.items():
            print(f"{k}: {v}")

    else:
        print("Produto não encontrado.")


def alertar_estoque_baixo(dados, limite):

    encontrados = False

    print("\nESTOQUE BAIXO")

    for p in dados["produtos"]:

        if p["quantidade"] < limite:

            encontrados = True

            print(
                f'{p["nome"]} → {p["quantidade"]}'
            )

    if not encontrados:
        print("Nenhum produto crítico.")


def gerar_relatorio(dados):

    print("\nRELATÓRIO DE ESTOQUE")

    valor_total = 0

    for p in dados["produtos"]:

        total = p["preco"] * p["quantidade"]

        valor_total += total

        print(
            f'{p["nome"]} | '
            f'Qtd: {p["quantidade"]} | '
            f'R$ {total:.2f}'
        )

    print(f"\nValor total: R$ {valor_total:.2f}")