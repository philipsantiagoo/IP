produtos_vendidos = ['peixe', 'lagosta', 'polvo', 'camarão', 'lagostine']

produtos_estoque = ['carangueijo', 'caviar', 'carangueijo', 'lula', 'peixe']


for produto in produtos_vendidos:
    # consulta produto no produtos_estoque
    quantidade = 0
    for prod_estoque in produtos_estoque:
        if prod_estoque == produto:
            quantidade += 1
    print(f'Existem(m) {quantidade} {produto}(s) no estoque!')