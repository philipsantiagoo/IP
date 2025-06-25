# Declarando nível do Jinwoo
n_jinwoo = int(input())

# Declarando a quantidade de inimigos que Jinwoo vai enfrentar
qtd = int(input())

# Declarando flags para o loop 
contador = 0
fim_do_confronto = False


# Declarando as listas
exercito = []
quantidade = []


# Declarando o estado do Jinwoo
estado_jinwoo = ''

if qtd == 0:
    estado_jinwoo = 'vitória'
else:
    # Iniciando o loop
    while contador < qtd and fim_do_confronto == False:
        nome_da_criatura = input()
        nivel_criatura = int(input())

        # Declarando a vitória ou derrota
        if n_jinwoo <= nivel_criatura:
            # Declarando o estado de Jinwoo
            estado_jinwoo = 'derrota'
            fim_do_confronto = True
        else:
            # Declarando o estado de Jinwoo
            estado_jinwoo = 'vitória'
            n_jinwoo += nivel_criatura // 3
            resposta = input()

            # Declarando a aquisição ou não de uma criatura ao exército
            if resposta == 'Erga-se':
                if nome_da_criatura in exercito:
                    indice = exercito.index(nome_da_criatura)
                    quantidade[indice] += 1
                else:
                    exercito.append(nome_da_criatura)
                    quantidade.append(1)
        
        contador += 1


# Declarando o output
if estado_jinwoo == 'derrota':
    print(f'Jin-Woo foi derrotado por {nome_da_criatura}...')
elif estado_jinwoo == 'vitória':
    print('Jin-Woo sobreviveu à caçada, um verdadeiro Monarca das Sombras mesmo!')

print('===== Exército das Sombras de Jin-Woo =====')

# Analisando o tamanho do exército
if len(exercito) == 0:
    print('Jin-Woo não conseguiu formar seu exército...')
else:
    for i in range(len(exercito)):
        print(f'{exercito[i]}: {quantidade[i]}')
        