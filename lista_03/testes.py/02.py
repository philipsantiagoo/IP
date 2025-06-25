# Criando estoque
produtos_vendidos = ['martelo', 'alicate', 'chave de fenda', 'chave estrela', 'tesoura']

produtos_estoque = ['martelo', 'alicate', 'martelo', 'martelo', 'chave de fenda', 'alicate', 'chave estrela']


# Recebendo a entrada
entrada = input()

# Percorrendo a lista
vende_produto = False


for produto_vendido in produtos_vendidos:
    if produto_vendido == entrada:
        vende_produto = True

if vende_produto:
    # Verifica a quantidade em estoque
    quantidade = 0
    for prod_estoque in produtos_estoque:
        if prod_estoque == entrada:
            quantidade += 1

# Imprime relatório
if not vende_produto:
    print(f'Infelizmente, a loja não vende {entrada}...')
elif quantidade > 0:
    print(f'Existe(m) {quantidade} {entrada}(s) no estoque')
else:
    print('Não temos em estoque')