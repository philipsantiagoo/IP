# ========== Área de funções ==========
def distancia_euclidiana(a, b):
    distancia = 0

    distancia = ((a**2) + (b**2)) ** 0.5
    return(distancia)


# ========== Área de código ==========

# Verificando a quantidade de objetos que serão analisados
qtd_objetos = int(input())

# Verificando a quantidade de esferas encontradas
qtd_esferas = 0
menor_distancia = 999

# Loop dos blocos
for obj in range(1, qtd_objetos + 1):
    nome_objeto = input()
    coordenada_x = int(input())
    coordenada_y = int(input())

    # Verificando esfera
    if nome_objeto == 'esfera':
        qtd_esferas += 1
        if qtd_esferas >= 1:
            distancia = distancia_euclidiana(coordenada_x, coordenada_y)

            if distancia < menor_distancia:
                menor_distancia = distancia
                posicao_no_radar = obj

    # Verificando rocha, árvore, nave ou outros objetos
    else:  
        if nome_objeto == 'rocha':
            print("Radar: Rocha detectada! Bulma resmunga: 'Só um pedregulho cósmico... Sem valor para mim!'")
        elif nome_objeto == 'árvore':
            print("Radar: Árvore à vista! Bulma comenta: 'Interessante, mas não brilha como uma esfera. Próximo alvo!'")
        elif nome_objeto == 'nave':
            print("Radar: Sinal de nave! Bulma alerta: 'Pode ser Pilaf ou a Patrulha Vermelha! Melhor ficar atenta, mas o foco são as esferas!'")
        else:
            print(f"Radar: Detectado um(a) {nome_objeto}. Não parece ser uma esfera... Continuando a busca.")


# Mensagem final
if qtd_esferas == 0:
    print('Radar varreu a área. Nenhuma esfera do dragão à vista desta vez!')
else:
    print(f'ALVO PRIORITÁRIO: Esfera | Distância: {distancia:.2f}m | Detecção Original: {posicao_no_radar}°')