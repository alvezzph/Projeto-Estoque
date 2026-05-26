from modulos.arquivos import carregar_dados

from modulos.estoque import *

dados = carregar_dados()


while True:

    print("""
======== ESTOQUE ========

1 - Cadastrar produto
2 - Entrada
3 - Saída
4 - Consultar
5 - Alerta estoque baixo
6 - Relatório
0 - Sair

========================
""")

    op = input("Escolha: ")

    try:

        if op == "1":

            nome = input("Nome: ")

            categoria = input("Categoria: ")

            preco = float(
                input("Preço: ")
            )

            qtd = int(
                input("Quantidade: ")
            )

            cadastrar_produto(
                dados,
                nome,
                categoria,
                preco,
                qtd
            )

        elif op == "2":

            registrar_entrada(
                dados,
                int(input("ID: ")),
                int(input("Qtd: "))
            )

        elif op == "3":

            registrar_saida(
                dados,
                int(input("ID: ")),
                int(input("Qtd: "))
            )

        elif op == "4":

            consultar_estoque(
                dados,
                int(input("ID: "))
            )

        elif op == "5":

            alertar_estoque_baixo(
                dados,
                int(input("Limite: "))
            )

        elif op == "6":

            gerar_relatorio(dados)

        elif op == "0":

            print("Encerrando...")

            break

        else:

            print("Opção inválida.")

    except:

        print("Entrada inválida.")