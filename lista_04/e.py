# =============== ÁREA DE FUNÇÕES ===============
def funcao_prefixa(expressao):
    caracteres = expressao.split()
    pilha = []

    for indice in range(len(caracteres) - 1, -1, -1):
        caractere = caracteres[indice]

        if caractere.isnumeric():
            pilha.append(int(caractere))
        else:
            if len(pilha) >= 2:
                a = pilha.pop()
                b = pilha.pop()

                if caractere == '+':
                    resultado_pilha = a + b
                elif caractere == '-':
                    resultado_pilha = a - b
                elif caractere == '*':
                    resultado_pilha = a * b
                elif caractere == '/':
                    resultado_pilha = a / b

                pilha.append(resultado_pilha)
            else:
                return 0  

    if len(pilha) > 0:
        return pilha.pop()
    else:
        return 0


def verificando_primo(resultado_expressao):
    # Verifica se é número inteiro 
    if resultado_expressao % 1 != 0:
        return 'Não é primo'

    resultado_expressao = int(resultado_expressao)  

    if resultado_expressao <= 1:
        return 'Não é primo'
    if resultado_expressao == 2:
        return 'É primo'
    if resultado_expressao % 2 == 0:
        return 'Não é primo'

    i = 3
    while i * i <= resultado_expressao:
        if resultado_expressao % i == 0:
            return 'Não é primo'
        i += 2

    return 'É primo'


def decimal_binario(numero_resultado_expressao):
    numero_resultado_expressao = int(numero_resultado_expressao)
    binario = ''

    if numero_resultado_expressao == 0:
        return '0'

    while numero_resultado_expressao > 0:
        binario = str(numero_resultado_expressao % 2) + binario
        numero_resultado_expressao = numero_resultado_expressao // 2

    return binario


def binario_decimal(numero_binario):
    # Converte o número para binário como string
    binario = list(decimal_binario(numero_binario))

    # Verifica se é primo
    if verificando_primo(numero_binario) == 'É primo':
        binario.append('1')
    else:
        binario.append('0')

    # Converte a lista de caracteres binários para decimal
    decimal_final = 0
    potencia = 0

    for i in range(len(binario) - 1, -1, -1):
        decimal_final += int(binario[i]) * (2 ** potencia)
        potencia += 1

    return decimal_final


def processando_coordenadas(coordenadaXouY, n):
    num_convertido = binario_decimal(coordenadaXouY)
    coordenada = num_convertido % n
    return coordenada


def esfera_mais_proxima():
    menor_distancia = 999999
    esfera_mais_proxima = [0, 0]

    for esfera in esferas:
        x = esfera[0]
        y = esfera[1]
        distancia = abs(x - xGOKU) + abs(y - yGOKU)

        if distancia < menor_distancia:
            menor_distancia = distancia
            esfera_mais_proxima = [x, y]

    return esfera_mais_proxima


# =============== ÁREA DE CÓDIGO PRINCIPAL ===============
print('🟠 Vamos conquistar as esferas do dragão! 🟠')
print('--------------------------------------------------------------------------')
print()

# Rcebendo o valor da matriz N x N maior ou igual a 3
n = int(input())

# Recebendo as coordenadas cartesianas de Goku
coordenadasGOKU = input()
coordenadasGOKU = coordenadasGOKU.strip("()").split(",")
xGOKU = int(coordenadasGOKU[0])
yGOKU = int(coordenadasGOKU[1])

# Lista de esferas
esferas = []

# Recebendo linha vazia
input()

# Determinando o loop
entrada = ''

while entrada != 'Todos os bits foram decodificados':
    expressoes_x = []
    entrada = input()

    if entrada != 'Todos os bits foram decodificados':
        # =========== LENDO EXPRESSÕES DE X ============
        while entrada != '':
            expressoes_x.append(entrada)
            entrada = input()

        # =========== LENDO EXPRESSÕES DE Y ============
        expressoes_y = []
        entrada = input()

        while entrada != '':
            expressoes_y.append(entrada)
            entrada = input()

        # =========== LENDO A LINHA ============  
        entrada = input()

        # =========== PROCESSANDO COORDENADA X ============
        binario_x = ''
        for expressao in expressoes_x:
            if len(expressao.strip().split()) >= 3:
                resultado = funcao_prefixa(expressao)
                if verificando_primo(resultado) == 'É primo':
                    binario_x += '1'
                else:
                    binario_x += '0'

        decimal_x = int(binario_x, 2)
        coordenada_x = decimal_x % n

        # =========== PROCESSANDO COORDENADA Y ============
        binario_y = ''
        for expressao in expressoes_y:
            resultado = funcao_prefixa(expressao)
            if verificando_primo(resultado) == 'É primo':
                binario_y += '1'
            else:
                binario_y += '0'

        decimal_y = int(binario_y, 2)
        coordenada_y = decimal_y % n

        # =========== OUTPUT DAS COORDENADAS ============
        indice = len(esferas) + 1
        print(f'Coordenada x da {indice}ª esfera do dragão obtida pelo código binário {binario_x}: {coordenada_x}')
        print(f'Coordenada y da {indice}ª esfera do dragão obtida pelo código binário {binario_y}: {coordenada_y}')
        print(f'As coordenadas da {indice}ª esfera do dragão são: ({coordenada_x}, {coordenada_y})')
        print()

        # =========== SALVANDO A ESFERA ============
        esferas.append([coordenada_x, coordenada_y])

# =========== LINHA TRACEJADA ============
print('--------------------------------------------------------------------------')
print()

# =========== PRINTANDO A MATRIZ ============
for linha in range(n):
    linha_atual = ''
    for coluna in range(n):
        if linha == xGOKU and coluna == yGOKU:
            linha_atual += 'G'
        elif [linha, coluna] in esferas:
            linha_atual += '☆'
        else:
            linha_atual += '.'
        if coluna < n - 1:
            linha_atual += ' '
    print(linha_atual)

# =========== CAMINHO DE GOKU ============
print()

posicoes_visitadas = [[xGOKU, yGOKU]]
goku_x = xGOKU
goku_y = yGOKU
esferas_restantes = esferas.copy()

while len(esferas_restantes) > 0:
    menor_distancia = 999999
    indice_mais_proxima = 0

    for i in range(len(esferas_restantes)):
        x = esferas_restantes[i][0]
        y = esferas_restantes[i][1]
        distancia = ((x - goku_x)**2 + (y - goku_y)**2) ** 0.5

        if distancia < menor_distancia:
            menor_distancia = distancia
            indice_mais_proxima = i

    proxima_esfera = esferas_restantes.pop(indice_mais_proxima)
    goku_x = proxima_esfera[0]
    goku_y = proxima_esfera[1]
    posicoes_visitadas.append([goku_x, goku_y])

print('Trajetória completa de Goku: ', end='')
for i in range(len(posicoes_visitadas)):
    x = posicoes_visitadas[i][0]
    y = posicoes_visitadas[i][1]
    print(f'({x}, {y})', end='')
    if i < len(posicoes_visitadas) - 1:
        print(' -> ', end='')
print()

# =========== FRASE FINAL ============
print('Missão cumprida! Conseguimos todas as esferas do dragão!🟠🐉')
