# Definindo a lista das cores dos rangers
rangers = [
    "Vermelho",
    "Verde",
    "Rosa",
    "Preto", 
    "Azul",
    "Amarela",  
]

# Definindo a lista dos nomes dos rangers
nomes_1 = []
nomes_2 = []
nomes_3 = []

# Definindo a lista dos níveis dos zords
niveis_1 = []
niveis_2 = []
niveis_3 = []

# Definindo a mensagem de boas-vindas
print('Go! Go! Power Rangers!')

# Definindo a entrada do usuário
entrada = input()

# Verificando se a entrada contém o nome do robô lendário
if 'robocin' in [parte.strip() for parte in entrada.split('-')]:
    print('Os rangers encontraram o zord lendário!!!! O Robocin!!!! Eles não precisam mais de outros zords!')
# Verificando caso não tenha o nome do robô lendário
else:
    dados = entrada.split('-')

    indice = 0
    # Processando os dados de entrada da treta brutal dos zords 
    # O melhor Power Rangers é o Space e quam discorda tá errado.
    while indice < len(dados):
        nome = dados[indice]
        nivel = int(dados[indice+1])

        indice += 2

        # Definindo para qual lista o zord será adicionado
        if nivel <= 10:
            nomes_3.append(nome)
            niveis_3.append(nivel)
        
        elif 10 < nivel <= 30:
            nomes_2.append(nome)
            niveis_2.append(nivel)
        
        else:
            nomes_1.append(nome)
            niveis_1.append(nivel)

    # Tipo 1
    maior_nivel = -1 
    segundo_maior_nivel = -1
    tem_vermelho = False
    tem_verde = False

    # Verificando o maior nível dos zords
    for nivel in niveis_1:
        # Se o nível do zord for maior que o maior nível encontrado até agora
        if nivel > maior_nivel:
            # Segundo maior nível passa a ser o maior nível encontrado anteriormente
            segundo_maior_nivel = maior_nivel
            # O maior nível passa a ser o nível atual
            maior_nivel = nivel
        # Se o nível do zord for maior que o segundo maior nível encontrado até agora
        elif nivel > segundo_maior_nivel:
            # O segundo maior nível passa a ser o nível atual
            segundo_maior_nivel = nivel

    # Verificando se existem pelo menos dois zords do tipo 1
    if len(niveis_1) >= 2:
        # Encontrando os índices dos maiores níveis e segundo maiores níveis
        indice_maior = niveis_1.index(maior_nivel)
        indice_segundo_maior = niveis_1.index(segundo_maior_nivel)
        print(f'Zord do Ranger {rangers[0]}: {nomes_1[indice_maior]}')
        print(f'Zord do Ranger {rangers[1]}: {nomes_1[indice_segundo_maior]}')
        tem_vermelho = True
        tem_verde = True
    # Verificando se existe apenas um zord do tipo 1
    elif len(niveis_1) == 1:
        print(f'Zord do Ranger {rangers[0]}: {nomes_1[0]}')
        print(f'Ranger {rangers[1]} ficou sem zord!')
        tem_vermelho = True
    # Se não houver zords do tipo 1    
    else:
        print(f'Ranger {rangers[0]} ficou sem zord!')
        print(f'Ranger {rangers[1]} ficou sem zord!')

    # Tipo 2
    maior_nivel = -1 
    segundo_maior_nivel = -1
    tem_rosa = False
    tem_preto = False

    # Mesma lógica do tipo 1 para encontrar os maiores níveis dos zords
    for nivel in niveis_2:
        if nivel > maior_nivel:
            segundo_maior_nivel = maior_nivel
            maior_nivel = nivel
        elif nivel > segundo_maior_nivel:
            segundo_maior_nivel = nivel

    # Mesma lógica
    if len(niveis_2) >= 2:
        indice_maior = niveis_2.index(maior_nivel)
        indice_segundo_maior = niveis_2.index(segundo_maior_nivel)
        print(f'Zord da Ranger {rangers[2]}: {nomes_2[indice_maior]}')
        print(f'Zord do Ranger {rangers[3]}: {nomes_2[indice_segundo_maior]}')
        tem_rosa = True
        tem_preto = True
    elif len(niveis_2) == 1:
        print(f'Zord da Ranger {rangers[2]}: {nomes_2[0]}')
        print(f'Ranger {rangers[3]} ficou sem zord!')
        tem_rosa = True
    else:
        print(f'Ranger {rangers[2]} ficou sem zord!')
        print(f'Ranger {rangers[3]} ficou sem zord!')

    # Tipo 3
    maior_nivel = -1 
    segundo_maior_nivel = -1
    tem_azul = False
    tem_amarela = False

    # Verificando o maior nível dos zords mesma lógica do tipo 1 e 2
    for nivel in niveis_3:
        if nivel > maior_nivel:
            segundo_maior_nivel = maior_nivel
            maior_nivel = nivel
        elif nivel > segundo_maior_nivel:
            segundo_maior_nivel = nivel

    # ...
    if len(niveis_3) >= 2:
        indice_maior = niveis_3.index(maior_nivel)
        indice_segundo_maior = niveis_3.index(segundo_maior_nivel)
        print(f'Zord do Ranger {rangers[4]}: {nomes_3[indice_maior]}')
        print(f'Zord da Ranger {rangers[5]}: {nomes_3[indice_segundo_maior]}')
        tem_azul = True
        tem_amarela = True
    elif len(niveis_3) == 1:
        print(f'Zord do Ranger {rangers[4]}: {nomes_3[0]}')
        print(f'Ranger {rangers[5]} ficou sem zord!')
        tem_azul = True
    else:
        print(f'Ranger {rangers[4]} ficou sem zord!')
        print(f'Ranger {rangers[5]} ficou sem zord!')

    # Relatório dos zords por tipo e ordem decrescente de nível
    # Verifica de um em um a lista de nomes_1
    for i in range(len(nomes_1)):
        # Ordena os zords do tipo 1 em ordem decrescente de nível
        for j in range(i + 1, len(nomes_1)):
            # Se o nível do zord i for menor que o nível do zord j, troca os nomes e níveis
            if niveis_1[i] < niveis_1[j]:
                # Troca os nomes e níveis dos zords
                nomes_1[i], nomes_1[j] = nomes_1[j], nomes_1[i]
                niveis_1[i], niveis_1[j] = niveis_1[j], niveis_1[i]

    if len(nomes_1) > 0:
        print(f'Zords do tipo 1: {", ".join(nomes_1)}')
    else:
        print('Não temos nenhum zord do tipo 1 :(')

    # ...
    for i in range(len(nomes_2)):
        for j in range(i + 1, len(nomes_2)):
            if niveis_2[i] < niveis_2[j]:
                nomes_2[i], nomes_2[j] = nomes_2[j], nomes_2[i]
                niveis_2[i], niveis_2[j] = niveis_2[j], niveis_2[i]

    if len(nomes_2) > 0:
        print(f'Zords do tipo 2: {", ".join(nomes_2)}')
    else:
        print('Não temos nenhum zord do tipo 2 :(')

    # ...
    for i in range(len(nomes_3)):
        for j in range(i + 1, len(nomes_3)):
            if niveis_3[i] < niveis_3[j]:
                nomes_3[i], nomes_3[j] = nomes_3[j], nomes_3[i]
                niveis_3[i], niveis_3[j] = niveis_3[j], niveis_3[i]

    if len(nomes_3) > 0:
        print(f'Zords do tipo 3: {", ".join(nomes_3)}')
    else:
        print('Não temos nenhum zord do tipo 3 :(')

    # Verificando se todos os rangers ficaram com zords ou se algum ranger ficou sem zord
    if tem_vermelho and tem_verde and tem_rosa and tem_preto and tem_azul and tem_amarela:
        print('Os Rangers estão prontos para montar o Megazord e derrotar Rita!')
    else:
        print('Ai ai ai, essa não!! Não temos zords suficientes para formar o Megazord! Os ranger não vão conseguir derrotar Rita!')
