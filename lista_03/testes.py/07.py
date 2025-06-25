# Escrevendo uma matriz
num_linha = int(input())
num_coluna = int(input())


# lista vazia para armazenas os dados da matriz
matriz = []

# leitura dos dados da matriz
for i in range(num_linha):
    # lista vazia p/ armazenar uma linha da matriz
    linha_matriz = []
    # leitura dos dados de uma linha da matriz
    for j in range(num_coluna):
        linha_matriz.append(int(input()))
    # inclusão da nova linha na matriz
    matriz.append(linha_matriz)

# impressão da matriz criada
for i in range(num_linha):
    print(matriz[i])