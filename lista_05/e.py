# ========== ÁREA DE FUNÇÕES ==========
def buscando_o_menor_caminho(i, j, custo_de_movimento_atual, menor_custo_de_movimento_encontrado, visitado, qtd_de_movimentos, matriz):
    n = len(matriz)
    m = len(matriz[0])

    # Veirificando se está fora dos limites permitidos
    if i < 0 or i >= n or j < 0 or j >= m:
        return
    
    # Opa, é uma barreira
    if matriz[i][j] == '0':
        return
    
    # Já passei por aqui
    if visitado[i][j]:
        return
    
    # Já estou num caminho pior do que o melhor até agora
    if custo_de_movimento_atual >= menor_custo_de_movimento_encontrado[0]:
        return
    
    # Oii, Cesar. Te achei menó
    if (i == n - 1) and (j == m - 1):
        if custo_de_movimento_atual < menor_custo_de_movimento_encontrado[0]:
            menor_custo_de_movimento_encontrado[0] = custo_de_movimento_atual
            return
    
    # Cesar da peste, bicho se esconde e não é pouco
    visitado[i][j] = True

    # Movimentando para cima
    nova_linha_ni_cima = i - 1
    nova_linha_ji_cima = j

    if 0 <= nova_linha_ni_cima < n and 0 <= nova_linha_ji_cima < m:
        if matriz[nova_linha_ni_cima][nova_linha_ji_cima] != '0':
            if matriz[nova_linha_ni_cima][nova_linha_ji_cima] == '3':
                novo_custo = custo_de_movimento_atual + 3
            else:
                novo_custo = custo_de_movimento_atual + 1
            
            buscando_o_menor_caminho(nova_linha_ni_cima, nova_linha_ji_cima, novo_custo, menor_custo_de_movimento_encontrado, visitado, qtd_de_movimentos + 1, matriz)
    

    # Movimento para baixo
    nova_linha_ni_baixo = i + 1
    nova_linha_ji_baixo = j

    if 0 <= nova_linha_ni_baixo < n and 0 <= nova_linha_ji_baixo < m:
        if matriz[nova_linha_ni_baixo][nova_linha_ji_baixo] != '0':
            if matriz[nova_linha_ni_baixo][nova_linha_ji_baixo] == '3':
                novo_custo = custo_de_movimento_atual + 3
            else:
                novo_custo = custo_de_movimento_atual + 1
            
            buscando_o_menor_caminho(nova_linha_ni_baixo, nova_linha_ji_baixo, novo_custo, menor_custo_de_movimento_encontrado, visitado, qtd_de_movimentos + 1, matriz)

    
    # Movimento para a esquerda
    nova_linha_ni_esquerda = i
    nova_linha_ji_esquerda = j - 1

    if 0 <= nova_linha_ni_esquerda < n and 0 <= nova_linha_ji_esquerda < m:
        if matriz[nova_linha_ni_esquerda][nova_linha_ji_esquerda] != '0':
            if matriz[nova_linha_ni_esquerda][nova_linha_ji_esquerda] == '3':
                novo_custo = custo_de_movimento_atual + 3
            else:
                novo_custo = custo_de_movimento_atual + 1
            
            buscando_o_menor_caminho(nova_linha_ni_esquerda, nova_linha_ji_esquerda, novo_custo, menor_custo_de_movimento_encontrado, visitado, qtd_de_movimentos + 1, matriz)
    

    # Movimento para a direita
    nova_linha_ni_direita = i
    nova_linha_ji_direita = j + 1

    if 0 <= nova_linha_ni_direita < n and 0 <= nova_linha_ji_direita < m:
        if matriz[nova_linha_ni_direita][nova_linha_ji_direita] != '0':
            if matriz[nova_linha_ni_direita][nova_linha_ji_direita] == '3':
                novo_custo = custo_de_movimento_atual + 3
            else:
                novo_custo = custo_de_movimento_atual + 1
            
            buscando_o_menor_caminho(nova_linha_ni_direita, nova_linha_ji_direita, novo_custo, menor_custo_de_movimento_encontrado, visitado, qtd_de_movimentos + 1, matriz)


    # Verificando o caso de viga '2'
    if matriz[i][j] == '2':
        destino_i_cima = i - 2
        destino_j_cima = j
        
        # Direção: cima pow
        if 0 <= destino_i_cima < n and 0 <= destino_j_cima < m:
            if matriz[destino_i_cima][destino_j_cima] != '0':
                buscando_o_menor_caminho(destino_i_cima, destino_j_cima, custo_de_movimento_atual + 1, menor_custo_de_movimento_encontrado, visitado, qtd_de_movimentos + 1, matriz)
        
        destino_i_baixo = i + 2
        destino_j_baixo = j

        # Direção: 'Os Baixinhos!!', disse Xuxa
        if 0 <= destino_i_baixo < n and 0 <= destino_j_baixo < m:
            if matriz[destino_i_baixo][destino_j_baixo] != '0':
                buscando_o_menor_caminho(destino_i_baixo, destino_j_baixo, custo_de_movimento_atual + 1, menor_custo_de_movimento_encontrado, visitado, qtd_de_movimentos + 1, matriz)
        
        destino_i_esquerda = i
        destino_j_esquerda = j - 2

        # Direção: ia fazer piada política, mas vou me abster 
        if 0 <= destino_i_esquerda < n and 0 <= destino_j_esquerda < m:
            if matriz[destino_i_esquerda][destino_j_esquerda] != '0':
                buscando_o_menor_caminho(destino_i_esquerda, destino_j_esquerda, custo_de_movimento_atual + 1, menor_custo_de_movimento_encontrado, visitado, qtd_de_movimentos + 1, matriz)
        
        destino_i_direita = i
        destino_j_direita = j + 2

        # Direção: ia fazer piada política, mas vou me abster 
        if 0 <= destino_i_direita < n and 0 <= destino_j_direita < m:
            if matriz[destino_i_direita][destino_j_direita] != '0':
                buscando_o_menor_caminho(destino_i_direita, destino_j_direita, custo_de_movimento_atual + 1, menor_custo_de_movimento_encontrado, visitado, qtd_de_movimentos + 1, matriz)
    
    visitado[i][j] = False
        
            
# ========== ÁREA DE CÓDIGO PRINCIPAL ==========

# Recebendo os dados da matriz N x M
n = int(input())
m = int(input())

# Montando a matriz
matriz = []

for i in range(n):
    linha = input().split()
    if len(linha) == m:
        matriz.append(linha)

# Printando as mensagens
print('=== SEKIRO: O RESGATE DE CESAR ===')
print('Wolf deve resgatar CESAR!')


visitado = []
for _ in range(n):
    visitado.append([False] * m)

menor_custo_de_movimento_encontrado = [float('inf')]

# Chamando a função
buscando_o_menor_caminho(0, 0, 0, menor_custo_de_movimento_encontrado, visitado, 0, matriz)

# Mensagens finais
if menor_custo_de_movimento_encontrado[0] == float('inf'):
    print('MORTE! Wolf não conseguiu resgatar Cesar... ele nunca saberá quem venceu Satoru Gojo ou Sukuna!')
else:
    movimentos = menor_custo_de_movimento_encontrado[0]
    print(f'SUCESSO! Wolf resgatou o Cesar em {movimentos} movimentos!')
    if movimentos <= 4:
        print('PERFEITO! Verdadeiro Shinobi! Cesar está ORGULHOSO!!')
    elif movimentos < 8:
        print('BOM! Caminho eficiente! Mas você quase decepcionou Cesar')
    else:
        print('Wolf chegou, mas pode melhorar... Cesar está decepcionado, quase morreu de tédio!')
