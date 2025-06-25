# Definindo a ordem da matriz quadrada (N x N)
n = int(input())


# Criando a matriz linha por linha
matriz = []


for i in range(n):
    linha = input().split()
    matriz.append(list(linha))


# Achando a posição do Spider 
for i in range(n):
    for j in range(n):
        if matriz[i][j] == 'H':
            # Coordenadas do menino vermelho
            x, y = i, j


# Contar quarteirões já destruídos ('X') no início
destruidos = 0
for i in range(n):
    for j in range(n):
        if matriz[i][j] == 'X':
            destruidos += 1


# Comandos do Miranha
entrada = ''
dia = 0
sem_restaurar = 0
fim_forcado = 0
restaurados = 0


# Flag de vitória
vitoria = 0

while entrada != 'FIM' and dia < 7:
    entrada = input()


    # Contando quarteirões corrompidos
    total_corrompidos = 0
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 'E':
                total_corrompidos += 1


    # Verificando a vitória do menino Parker
    if total_corrompidos == 0:
        vitoria = 1
        entrada = 'FIM'
    elif entrada != 'FIM':
        dia += 1


        # Movimentos do Peter
        movimentoX, movimentoY = 0, 0

        if entrada == 'Cima':
            movimentoX, movimentoY = -1, 0
        elif entrada == 'Baixo':
            movimentoX, movimentoY = 1, 0
        elif entrada == 'Esquerda':
            movimentoX, movimentoY = 0, -1
        elif entrada == 'Direita':
            movimentoX, movimentoY = 0, 1

        novo_cartesiano_x = x + movimentoX
        novo_cartesiano_y = y + movimentoY


        # Miranha passou por aqui
        movimento_ok = 0
        restaurou_hoje = 0

        if novo_cartesiano_x >= 0 and novo_cartesiano_x < n and novo_cartesiano_y >= 0 and novo_cartesiano_y < n:
            if matriz[novo_cartesiano_x][novo_cartesiano_y] != 'X':
                movimento_ok = 1

        if movimento_ok == 1:
            matriz[x][y] = '.'

            if matriz[novo_cartesiano_x][novo_cartesiano_y] == 'E':
                sem_restaurar = 0
                restaurados += 1
                restaurou_hoje = 1
            else:
                sem_restaurar += 1
                restaurou_hoje = 0

            matriz[novo_cartesiano_x][novo_cartesiano_y] = 'H'
            x = novo_cartesiano_x
            y = novo_cartesiano_y

        else:
            restaurou_hoje = 0
            sem_restaurar += 1


        # 3 dias sem restauração
        if sem_restaurar == 3:
            destruiu = 0
            for i in range(n):
                for j in range(n):
                    if destruiu == 0:
                        if matriz[i][j] == 'E':
                            matriz[i][j] = 'X'
                            destruidos += 1
                            destruiu = 1
            sem_restaurar = 0


        # Mensagens
        print(f'Dia {dia}')
        for i in range(n):
            linha = ''
            for j in range(n):
                linha = linha + matriz[i][j] + ' '
            print(linha.strip())

        print('Posição atual do Homem-Aranha: (' + str(x) + ', ' + str(y) + ')')
        print('Quarteirões restaurados: ' + str(restaurados) + ' | Quarteirões destruídos: ' + str(destruidos))

        if movimento_ok == 1:
            if restaurou_hoje == 1:
                print('O Miranha restaurou um quarteirão!')
            else:
                print('O Electro está ganhando espaço!')
        else:
            print('Ai! O Miranha tentou passar, mas acabou se machucando. Tenha mais cuidado!')
        print()


    elif entrada == 'FIM':
        fim_forcado = 1



# Mensagem final
if vitoria == 1 and restaurados > 0:
    print('Missão cumprida! Nova York está segura e o Miranha faz tudo novamente!')
elif dia == 7 and total_corrompidos > 0:
    print('O Miranha não conseguiu restaurar a cidade a tempo, o Electro venceu!')
elif fim_forcado == 1 and total_corrompidos > 0:
    print('Ainda existem quarteirões corrompidos! O Miranha não pode ir embora agora!')
