# Adicionar

def adicionar():
    output.clear()
    nome = input('Digite o nome do item: ')
    cat = input('Digite a categoria do item: ')
    quant = int(input('Digite a quantidade do item: '))
    preco = float(input('Digite o preço do item: '))
    dados = {'nome': nome, 'categoria': cat, 'quantidade': quant, 'preco_unitario': preco, 'preco_total': preco * quant
    }
    cursor.execute("""
    INSERT INTO estoque
    (nome, categoria, quantidade, preco_unitario, preco_total)
    VALUES (:nome, :categoria, :quantidade, :preco_unitario, :preco_total)
    """, dados)
    conexao.commit()
    print('\nItem adicionado com sucesso!')
    input('Enter para continuar...')

# Listar

def listar():
    output.clear()
    cursor.execute('SELECT * FROM estoque')
    itens = cursor.fetchall()
    print('{:<5} {:<15} {:<15} {:<12} {:<12} {:<12}'.format('ID', 'Nome', 'Categoria', 'Quantidade', 'Preço', 'Total'))
    print('-' * 75)
    for item in itens:
      print('{:<5} {:<15} {:<15} {:<12} {:<12.2f} {:<12.2f}'.format(item['codigo'], item['nome'], item['categoria'], item['quantidade'], item['preco_unitario'], item['preco_total']))
    input('\nPressione ENTER para continuar...')

# Atualizar e Remover

def atualizar():
    output.clear()
    cursor.execute('SELECT * FROM estoque')
    itens = cursor.fetchall()
    opca = input('1_ Mudar completamente \n2_ Subtrair \n3_ Adicionar \n4_ Remover do estoque \nEscolha uma opção: ')
    if opca == '1':
      print('{:<5} {:<15} {:<15} {:<12} {:<12} {:<12}'.format('ID', 'Nome', 'Categoria', 'Quantidade', 'Preço', 'Total'))
      print('-' * 75)
      for item in itens:
        print('{:<5} {:<15} {:<15} {:<12} {:<12.2f} {:<12.2f}'.format(item['codigo'], item['nome'], item['categoria'], item['quantidade'], item['preco_unitario'], item['preco_total']))
      codigo = int(input('Digite o ID do item: '))
      if codigo == 'item[codigo]':
        nome = input('Novo nome: ')
        cat = input('Nova categoria: ')
        quant = int(input('Nova quantidade: '))
        preco = float(input('Novo preço: '))
        dados = {
          'codigo': codigo,
          'nome': nome,
          'categoria': cat,
          'quantidade': quant,
          'preco_unitario': preco,
          'preco_total': preco * quant
        }
        cursor.execute("""
        UPDATE estoque
        SET
            nome = :nome,
            categoria = :categoria,
            quantidade = :quantidade,
            preco_unitario = :preco_unitario,
            preco_total = :preco_total
        WHERE codigo = :codigo
        """, dados)
        conexao.commit()
        print('\nItem atualizado!')
        input('Enter para continuar...')
      else:
        print('Item não encontrado!')
        input('Enter para continuar...')
      # Sub
    elif opca == '2':
      print('{:<5} {:<15} {:<15} {:<12} {:<12} {:<12}'.format('ID', 'Nome', 'Categoria', 'Quantidade', 'Preço', 'Total'))
      print('-' * 75)
      for item in itens:
        print('{:<5} {:<15} {:<15} {:<12} {:<12.2f} {:<12.2f}'.format(item['codigo'], item['nome'], item['categoria'], item['quantidade'], item['preco_unitario'], item['preco_total']))
      codigo = int(input('Digite o ID do item: '))
      quant = int(input('Digite a quantidade a ser subtraída: '))
      cursor.execute("""
      UPDATE estoque
      SET
          quantidade = quantidade - :quant
      WHERE codigo = :codigo
      """, {'codigo': codigo, 'quant': quant})
      conexao.commit()
      print('\nItem atualizado!')
      input('Enter para continuar...')
    # Add
    elif opca == '3':
      print('{:<5} {:<15} {:<15} {:<12} {:<12} {:<12}'.format('ID', 'Nome', 'Categoria', 'Quantidade', 'Preço', 'Total'))
      print('-' * 75)
      for item in itens:
        print('{:<5} {:<15} {:<15} {:<12} {:<12.2f} {:<12.2f}'.format(item['codigo'], item['nome'], item['categoria'], item['quantidade'], item['preco_unitario'], item['preco_total']))
      codigo = int(input('Digite o ID do item: '))
      quant = int(input('Digite a quantidade a ser adicionada: '))
      cursor.execute("""
      UPDATE estoque
      SET
          quantidade = quantidade + :quant
      WHERE codigo = :codigo
      """, {'codigo': codigo, 'quant': quant})
      conexao.commit()
      print('\nItem atualizado!')
      input('Enter para continuar...')
    # Remover
    elif opca == '4':
      print('{:<5} {:<15} {:<15} {:<12} {:<12} {:<12}'.format('ID', 'Nome', 'Categoria', 'Quantidade', 'Preço', 'Total'))
      print('-' * 75)
      for item in itens:
        print('{:<5} {:<15} {:<15} {:<12} {:<12.2f} {:<12.2f}'.format(item['codigo'], item['nome'], item['categoria'], item['quantidade'], item['preco_unitario'], item['preco_total']))
      codigo = int(input('Digite o ID do item: '))
      # remove o item
      cursor.execute("""
      DELETE FROM estoque
      WHERE codigo = ?
      """, (codigo,))
      # reorganiza os IDs
      cursor.execute("""
      CREATE TABLE estoque_temp (
          codigo INTEGER PRIMARY KEY AUTOINCREMENT,
          nome TEXT NOT NULL,
          categoria TEXT NOT NULL,
          quantidade INTEGER NOT NULL,
          preco_unitario REAL NOT NULL,
          preco_total REAL NOT NULL
      )
      """)
      # copia os dados sem os IDs antigos
      cursor.execute("""
      INSERT INTO estoque_temp
      (nome, categoria, quantidade, preco_unitario, preco_total)
      SELECT nome, categoria, quantidade, preco_unitario, preco_total
      FROM estoque
      """)
      # apaga tabela antiga
      cursor.execute("DROP TABLE estoque")
      # renomeia tabela nova
      cursor.execute("""
      ALTER TABLE estoque_temp
      RENAME TO estoque
      """)
      conexao.commit()
      print('\nItem removido!')
      input('Enter para continuar...')
    # Erro
    else:
      print('Opção inválida. \nVoltando à tela inicial...')
      time.sleep(3)