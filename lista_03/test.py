# Recebendo os valores de (N x M) da matriz
entrada = input()
n = int(entrada.split('x')[0])
m = int(entrada.split('x')[1])


# Criando a lista da matriz N x M
matriz = []


# Variáveis para armazenar as posições das meninas e do Macaco Louco
linha_florzinha = -1
coluna_florzinha = -1

linha_lindinha = -1
coluna_lindinha = -1

linha_docinho = -1
coluna_docinho = -1

linha_macaco = -1
coluna_macaco = -1


# Criando a matriz N x M
i = 0
while i < n:
    linha_str = input().split()
    linha = []
    j = 0
    while j < m:
        if linha_str[j] == 'F':
            linha_florzinha = i
            coluna_florzinha = j
            linha.append(0)
        elif linha_str[j] == 'L':
            linha_lindinha = i
            coluna_lindinha = j
            linha.append(0)
        elif linha_str[j] == 'D':
            linha_docinho = i
            coluna_docinho = j
            linha.append(0)
        elif linha_str[j] == 'M':
            linha_macaco = i
            coluna_macaco = j
            linha.append(0)
        else:
            linha.append(int(linha_str[j]))
        j = j + 1
    matriz.append(linha)
    i = i + 1


# Recebendo a energia da Florzinha, Lindinha e Docinho
energia_florzinha = int(input())
energia_lindinha = int(input())
energia_docinho = int(input())


# Condição de transposição da matriz
total_soma = 0

for i in range(n):
    for j in range(m):
        total_soma += matriz[i][j]


# Verificando os resultados
if total_soma % 2 == 0:
    matriz_transposta = []
    i = 0
    while i < m:
        linha_transposta = []
        j = 0
        while j < n:
            linha_transposta.append(matriz[j][i])  # CORRETO: acessa matriz[j][i]
            j = j + 1
        matriz_transposta.append(linha_transposta)
        i = i + 1
    matriz = matriz_transposta


    # atualizar posições
    aux = linha_florzinha
    linha_florzinha = coluna_florzinha
    coluna_florzinha = aux

    aux = linha_lindinha
    linha_lindinha = coluna_lindinha
    coluna_lindinha = aux

    aux = linha_docinho
    linha_docinho = coluna_docinho
    coluna_docinho = aux

    aux = linha_macaco
    linha_macaco = coluna_macaco
    coluna_macaco = aux

    aux = n
    n = m
    m = aux


# Início da simulação
capturado = False
todas_paradas = False
vencedora = ""

while not capturado and not todas_paradas:
    todas_paradas = True

    heroina_linhas = [linha_florzinha, linha_lindinha, linha_docinho]
    heroina_colunas = [coluna_florzinha, coluna_lindinha, coluna_docinho]
    energias = [energia_florzinha, energia_lindinha, energia_docinho]

    i = 0
    while i < 3:
        linha = heroina_linhas[i]
        coluna = heroina_colunas[i]
        energia = energias[i]

        movimentos = []

        if linha > 0:
            custo = matriz[linha - 1][coluna]
            if energia >= custo:
                movimentos.append([linha - 1, coluna, custo])
        if linha < n - 1:
            custo = matriz[linha + 1][coluna]
            if energia >= custo:
                movimentos.append([linha + 1, coluna, custo])
        if coluna > 0:
            custo = matriz[linha][coluna - 1]
            if energia >= custo:
                movimentos.append([linha, coluna - 1, custo])
        if coluna < m - 1:
            custo = matriz[linha][coluna + 1]
            if energia >= custo:
                movimentos.append([linha, coluna + 1, custo])

        menor_dist = 9999
        menor_custo = 9999
        destino_linha = -1
        destino_coluna = -1
        custo_escolhido = -1

        j = 0
        while j < len(movimentos):
            ml = movimentos[j][0]
            mc = movimentos[j][1]
            custo = movimentos[j][2]
            dist = abs(ml - linha_macaco) + abs(mc - coluna_macaco)
            if dist < menor_dist or (dist == menor_dist and custo < menor_custo):
                menor_dist = dist
                menor_custo = custo
                destino_linha = ml
                destino_coluna = mc
                custo_escolhido = custo
            j = j + 1

        if destino_linha != -1:
            matriz[linha][coluna] = 0
            energia = energia - custo_escolhido
            linha = destino_linha
            coluna = destino_coluna
            todas_paradas = False

        if i == 0:
            linha_florzinha = linha
            coluna_florzinha = coluna
            energia_florzinha = energia
        elif i == 1:
            linha_lindinha = linha
            coluna_lindinha = coluna
            energia_lindinha = energia
        else:
            linha_docinho = linha
            coluna_docinho = coluna
            energia_docinho = energia

        if linha == linha_macaco and coluna == coluna_macaco:
            capturado = True
            if i == 0:
                vencedora = "Florzinha"
            elif i == 1:
                vencedora = "Lindinha"
            else:
                vencedora = "Docinho"

        i = i + 1

if capturado:
    if vencedora == "Florzinha":
        print("Florzinha usou sua inteligência e capturou o Macaco Louco com um plano perfeito!")
    elif vencedora == "Lindinha":
        print("Lindinha, com coragem e coração, chegou primeiro e prendeu o Macaco Louco!")
    else:
        print("Docinho não deu chance: partiu pra cima e derrotou o Macaco Louco com atitude!")

    print("Situação final da cidade de Townsville após a batalha:")
    i = 0
    while i < n:
        j = 0
        linha_resultado = []
        while j < m:
            linha_resultado.append(str(matriz[i][j]))
            j = j + 1
        print(" ".join(linha_resultado))
        i = i + 1

    print("E assim, mais uma vez, AS MENINAS SUPERPODEROSAS salvaram o dia!")

else:
    print("O Macaco Louco escapou! As Meninas não conseguiram alcançá-lo a tempo…")

