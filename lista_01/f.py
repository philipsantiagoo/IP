nome_1 = str(input()).lower()
quem_indicou_1 = str(input()).lower()

nome_2 = str(input()).lower()
quem_indicou_2 = str(input()).lower()

nome_3 = str(input()).lower()
quem_indicou_3 = str(input()).lower()

ponto_nome_1 = 0
ponto_nome_2 = 0
ponto_nome_3 = 0

if 'cin' in nome_1:
    ponto_nome_1 += 10
if 'cin' in nome_2:
    ponto_nome_2 += 10
if 'cin' in nome_3:
    ponto_nome_3 += 10

ponto_nome_1 += len(nome_1)
ponto_nome_2 += len(nome_2)
ponto_nome_3 += len(nome_3)

if 'gato' in nome_1:
    ponto_nome_1 = 0
if 'felino espião' in quem_indicou_1:
    ponto_nome_1 = 0

if 'gato' in nome_2:
    ponto_nome_2 = 0
if 'felino espião' in quem_indicou_2:
    ponto_nome_2 = 0

if 'gato' in nome_3:
    ponto_nome_3 = 0
if 'felino espião' in quem_indicou_3:
    ponto_nome_3 = 0

if 'cin' in nome_1 and 'felino espião' not in quem_indicou_1:
    print('Os melhores nomes são aqueles que fazem referência a minha casinha :)')
if 'cin' in nome_2 and 'felino espião' not in quem_indicou_2:
    print('Os melhores nomes são aqueles que fazem referência a minha casinha :)')
if 'cin' in nome_3 and 'felino espião' not in quem_indicou_3:
    print('Os melhores nomes são aqueles que fazem referência a minha casinha :)')

if quem_indicou_1 == 'felino espião':
    print('Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.')
if quem_indicou_2 == 'felino espião':
    print('Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.')
if quem_indicou_3 == 'felino espião':
    print('Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.')


print('RANKING DOS NOMES:')
if ponto_nome_1 > ponto_nome_2 and ponto_nome_1 > ponto_nome_3:
    print(f'Primeiro lugar: {nome_1}')
    if ponto_nome_2 > ponto_nome_3:
        print(f'Segundo lugar: {nome_2}')
        print(f'Terceiro lugar: {nome_3}')
    else:
        print(f'Segundo lugar: {nome_3}')
        print(f'Terceiro lugar: {nome_2}')
elif ponto_nome_2 > ponto_nome_1 and ponto_nome_2 > ponto_nome_3:
    print( f'Primeiro lugar: {nome_2}')
    if ponto_nome_1 > ponto_nome_3:
        print(f'Segundo lugar: {nome_1}')
        print(f'Terceiro lugar: {nome_3}')
    else:
        print(f'Segundo lugar: {nome_3}')
        print(f'Terceiro lugar: {nome_1}')
else:
    print(f'Primeiro lugar: {nome_3}')
    if ponto_nome_1 > ponto_nome_2:
        print(f'Segundo lugar: {nome_1}')
        print(f'Terceiro lugar: {nome_2}')
    else:
        print(f'Segundo lugar: {nome_2}')
        print(f'Terceiro lugar: {nome_1}')