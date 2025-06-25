# ENTRADA
entrada = input()
n = int(entrada.split('x')[0])
m = int(entrada.split('x')[1])

# FORMANDO A MATRIZ
matriz = []

for i in range(n):
    linha = input().split()
    if len(linha) == m:
        matriz.append(linha)

# Posições de M, F, L e D
posicoes_M = []
posicoes_F = []
posicoes_L = []
posicoes_D = []

# Percorrendo matriz para encontrar posições das letras
for i in range(n):
    for j in range(m):
        if matriz[i][j] == 'M':
            posicoes_M.append((i, j))
        elif matriz[i][j] == 'F':
            posicoes_F.append((i, j))
        elif matriz[i][j] == 'L':
            posicoes_L.append((i, j))
        elif matriz[i][j] == 'D':
            posicoes_D.append((i, j))

# Recebendo a energia da Florzinha, Lindinha e Docinho
energia_florzinha = int(input())
energia_lindinha = int(input())
energia_docinho = int(input())

# Condição de transposição da matriz
total_soma = 0

for i in range(n):
    for j in range(m):
        elemento = matriz[i][j]
        if elemento.isdigit():
            total_soma += int(elemento)

if total_soma % 2 == 0:
    transposta = []
    for j in range(m):
        nova_linha = []
        for i in range(n):
            nova_linha.append(matriz[i][j])
        transposta.append(nova_linha)

    # Novas posições de M, F, L e D
    novas_posicoes_M = []
    novas_posicoes_F = []
    novas_posicoes_L = []
    novas_posicoes_D = []

    for i in range(m):
        for j in range(n):
            if transposta[i][j] == 'M':
                novas_posicoes_M.append((i, j))
            elif transposta[i][j] == 'F':
                novas_posicoes_F.append((i, j))
            elif transposta[i][j] == 'L':
                novas_posicoes_L.append((i, j))
            elif transposta[i][j] == 'D':
                novas_posicoes_D.append((i, j))

# ----------------- SIMULAÇÃO -----------------

macaco_capturado = False
vencedora = ''

# Definindo matriz ativa e posições iniciais
matriz_ativa = matriz
if total_soma % 2 == 0:
    matriz_ativa = transposta
    pos_F = novas_posicoes_F[0]
    pos_L = novas_posicoes_L[0]
    pos_D = novas_posicoes_D[0]
    pos_M = novas_posicoes_M[0]
else:
    pos_F = posicoes_F[0]
    pos_L = posicoes_L[0]
    pos_D = posicoes_D[0]
    pos_M = posicoes_M[0]

houve_movimento = True

while not macaco_capturado and (energia_florzinha > 0 or energia_lindinha > 0 or energia_docinho > 0) and houve_movimento:

    houve_movimento = False

    # ---------------- FLORZINHA ----------------
    if not macaco_capturado and energia_florzinha > 0:
        movimentos = []
        direcoes = [[-1,0], [1,0], [0,-1], [0,1]]

        for d in direcoes:
            ni = pos_F[0] + d[0]
            nj = pos_F[1] + d[1]
            if 0 <= ni < len(matriz_ativa) and 0 <= nj < len(matriz_ativa[0]):
                destino = matriz_ativa[ni][nj]
                if destino == 'M':
                    movimentos.append([ni, nj, 0])
                elif destino.isdigit() and destino != '0':
                    custo = int(destino)
                    if energia_florzinha >= custo:
                        movimentos.append([ni, nj, custo])

        if len(movimentos) > 0:
            distancias = []
            for mov in movimentos:
                dist = abs(mov[0] - pos_M[0]) + abs(mov[1] - pos_M[1])
                distancias.append(dist)

            menor_dist = min(distancias)

            melhores = []
            for i in range(len(movimentos)):
                if distancias[i] == menor_dist:
                    melhores.append(movimentos[i])

            menor_custo = melhores[0][2]
            escolhido = melhores[0]
            for mov in melhores:
                if mov[2] < menor_custo:
                    menor_custo = mov[2]
                    escolhido = mov

            destino_final = matriz_ativa[escolhido[0]][escolhido[1]]

            matriz_ativa[pos_F[0]][pos_F[1]] = '0'
            pos_F = (escolhido[0], escolhido[1])

            houve_movimento = True

            if destino_final == 'M':
                matriz_ativa[pos_F[0]][pos_F[1]] = 'F'
                macaco_capturado = True
                vencedora = 'Florzinha'
            else:
                energia_florzinha -= escolhido[2]
                matriz_ativa[pos_F[0]][pos_F[1]] = 'F'

    # ---------------- LINDINHA ----------------
    if not macaco_capturado and energia_lindinha > 0:
        movimentos = []
        direcoes = [[-1,0], [1,0], [0,-1], [0,1]]

        for d in direcoes:
            ni = pos_L[0] + d[0]
            nj = pos_L[1] + d[1]
            if 0 <= ni < len(matriz_ativa) and 0 <= nj < len(matriz_ativa[0]):
                destino = matriz_ativa[ni][nj]
                if destino == 'M':
                    movimentos.append([ni, nj, 0])
                elif destino.isdigit() and destino != '0':
                    custo = int(destino)
                    if energia_lindinha >= custo:
                        movimentos.append([ni, nj, custo])

        if len(movimentos) > 0:
            distancias = []
            for mov in movimentos:
                dist = abs(mov[0] - pos_M[0]) + abs(mov[1] - pos_M[1])
                distancias.append(dist)

            menor_dist = min(distancias)

            melhores = []
            for i in range(len(movimentos)):
                if distancias[i] == menor_dist:
                    melhores.append(movimentos[i])

            menor_custo = melhores[0][2]
            escolhido = melhores[0]
            for mov in melhores:
                if mov[2] < menor_custo:
                    menor_custo = mov[2]
                    escolhido = mov

            destino_final = matriz_ativa[escolhido[0]][escolhido[1]]

            matriz_ativa[pos_L[0]][pos_L[1]] = '0'
            pos_L = (escolhido[0], escolhido[1])

            houve_movimento = True

            if destino_final == 'M':
                matriz_ativa[pos_L[0]][pos_L[1]] = 'L'
                macaco_capturado = True
                vencedora = 'Lindinha'
            else:
                energia_lindinha -= escolhido[2]
                matriz_ativa[pos_L[0]][pos_L[1]] = 'L'

    # ---------------- DOCINHO ----------------
    if not macaco_capturado and energia_docinho >= 0:
        movimentos = []
        direcoes = [[-1,0], [1,0], [0,-1], [0,1]]

        for d in direcoes:
            ni = pos_D[0] + d[0]
            nj = pos_D[1] + d[1]
            if 0 <= ni < len(matriz_ativa) and 0 <= nj < len(matriz_ativa[0]):
                destino = matriz_ativa[ni][nj]
                if destino == 'M':
                    movimentos.append([ni, nj, 0])
                elif destino.isdigit() and destino != '0':
                    custo = int(destino)
                    if energia_docinho >= custo:
                        movimentos.append([ni, nj, custo])

        if len(movimentos) > 0:
            distancias = []
            for mov in movimentos:
                dist = abs(mov[0] - pos_M[0]) + abs(mov[1] - pos_M[1])
                distancias.append(dist)

            menor_dist = min(distancias)

            melhores = []
            for i in range(len(movimentos)):
                if distancias[i] == menor_dist:
                    melhores.append(movimentos[i])

            menor_custo = melhores[0][2]
            escolhido = melhores[0]
            for mov in melhores:
                if mov[2] < menor_custo:
                    menor_custo = mov[2]
                    escolhido = mov

            destino_final = matriz_ativa[escolhido[0]][escolhido[1]]

            matriz_ativa[pos_D[0]][pos_D[1]] = '0'
            pos_D = (escolhido[0], escolhido[1])

            houve_movimento = True

            if destino_final == 'M':
                matriz_ativa[pos_D[0]][pos_D[1]] = 'D'
                macaco_capturado = True
                vencedora = 'Docinho'
            else:
                energia_docinho -= escolhido[2]
                matriz_ativa[pos_D[0]][pos_D[1]] = 'D'

# Resultados

if macaco_capturado:
    if vencedora == "Florzinha":
        print("Florzinha usou sua inteligência e capturou o Macaco Louco com um plano perfeito!")
    elif vencedora == "Lindinha":
        print("Lindinha, com coragem e coração, chegou primeiro e prendeu o Macaco Louco!")
    else:
        print("Docinho não deu chance: partiu pra cima e derrotou o Macaco Louco com atitude!")

    print("Situação final da cidade de Townsville após a batalha:")

    for i in range(len(matriz_ativa)):
        linha = ''
        for j in range(len(matriz_ativa[0])):
            linha += matriz_ativa[i][j] + ' '
        print(linha.strip())

    print("E assim, mais uma vez, AS MENINAS SUPERPODEROSAS salvaram o dia!")

else:
    print("O Macaco Louco escapou! As Meninas não conseguiram alcançá-lo a tempo…")
