# Funções
def comparar_opcoes(a, b):
    # a e b são tuplas (ganho, prioridade, nome_titular, chave_titular, chave_reserva)
    # Queremos ordenar por:
    # 1) maior ganho (decrescente)
    # 2) menor prioridade (crescente)
    # 3) maior nome titular lexicograficamente (decrescente)

    # Comparar ganho (maior primeiro)
    if a[0] != b[0]:
        return b[0] - a[0] # ordem decrescente de ganho

    # Comparar prioridade (menor primeiro)
    if a[1] != b[1]:
        return a[1] - b[1] # menor prioridade tem preferência

    # Comparar nome titular (maior lexicograficamente primeiro)
    if a[2] != b[2]:
        if a[2] > b[2]: # nome maior (vem depois na ordem alfabética)
            return -1
        else:
            return 1

    return 0 # se tudo for igual, empate



def ordenar_opcoes(opcoes):
    # Bubble sort usando a função comparar_opcoes
    n = len(opcoes)
    for i in range(n):
        for j in range(0, n - i - 1):
            if comparar_opcoes(opcoes[j], opcoes[j + 1]) > 0:
                # troca os elementos se a opção j deve vir depois de j+1
                opcoes[j], opcoes[j + 1] = opcoes[j + 1], opcoes[j]
    return opcoes # retorna a lista ordenada



def cartola(dados_gerais, tecnico_NAO_fez_substituicao, pontuacao_total_dos_tecnicos, pontuacao_titulares, pontuacao_reservas):
    # Calcula pontuação titulares e adiciona ao técnico
    for tecnico in dados_gerais:
        # pega a chave da chave: titulares e vamos repartir
        titulares = dados_gerais[tecnico]['titulares']

        for nome_jogador in titulares:
            # pega as informações dos titulares
            jogador = titulares[nome_jogador]
            partes = jogador.split(',')

            nome = partes[0].strip()
            posicao = partes[1].strip()
            gols_realizados = int(partes[2])
            assistencias = int(partes[3])
            amarelos = int(partes[4])
            vermelhos = int(partes[5])
            gols_sofridos = int(partes[6])

            # calcula a pontuação base
            pontos = (gols_realizados * 8) + (assistencias * 5) - (amarelos * 1) - (vermelhos * 3)

            # calcula o bônus
            if posicao in ['goleiro', 'zagueiro', 'lateral'] and gols_sofridos == 0:
                pontos += 5

            # já adiciona os pontos ao técnico
            pontuacao_total_dos_tecnicos[tecnico] += pontos
            # já adiciona os pontos de cada jogador treinado por cada técnico
            pontuacao_titulares[tecnico][nome_jogador] = pontos


    # Calcula pontuação reservas (não adiciona ao técnico ainda)
    for tecnico in dados_gerais:
        # pega as informações dos reservas
        reservas = dados_gerais[tecnico]['reservas']

        for nome_jogador in reservas:
            jogador = reservas[nome_jogador]
            partes = jogador.split(',')

            nome = partes[0].strip()
            posicao = partes[1].strip()
            gols_realizados = int(partes[2])
            assistencias = int(partes[3])
            amarelos = int(partes[4])
            vermelhos = int(partes[5])
            gols_sofridos = int(partes[6])

            # calcula a pontuação base
            pontos = (gols_realizados * 8) + (assistencias * 5) - (amarelos * 1) - (vermelhos * 3)

            # calcula o bônus
            if posicao in ['goleiro', 'zagueiro', 'lateral'] and gols_sofridos == 0:
                pontos += 5

            # adiciona os pontos do reserva de cada técnico, mas ainda não adicionamos os pontos aos pontos totais do técnico
            pontuacao_reservas[tecnico][nome_jogador] = pontos

    # Prioridade posição (menor = maior prioridade)
    prioridade_posicao = {
        'goleiro': 1,
        'lateral': 2,
        'zagueiro': 3,
        'meia': 4,
        'atacante': 5
    }

    substituicoes_feitas = {}

    # analisando os titulares e reservas de cada técnico
    for tecnico in dados_gerais:
        titulares = dados_gerais[tecnico]['titulares']
        reservas = dados_gerais[tecnico]['reservas']

        # adicionando a lista de melhores opções
        melhores_opcoes = []

        # itera os reservas
        for nome_reserva, dados_reserva in reservas.items():
            partes_r = dados_reserva.split(',')
            nome_r = partes_r[0].strip()
            posicao_r = partes_r[1].strip()
            # taca os pontos de cada reserva aqui
            pontos_r = pontuacao_reservas[tecnico][nome_reserva]

            # itera os titulares 
            for nome_titular, dados_titular in titulares.items():
                partes_t = dados_titular.split(',')
                nome_t = partes_t[0].strip()
                posicao_t = partes_t[1].strip()
                pontos_t = pontuacao_titulares[tecnico][nome_titular]

                # se a posição do reserva for igual a do titular
                if posicao_r == posicao_t:
                    # o ganho é avaliado entre os pontos do reserva e do titular
                    ganho = pontos_r - pontos_t
                    # se for positivo adiciona na lista os dados do reserva e do titular em questão
                    if ganho > 0:
                        melhores_opcoes.append((
                            ganho,
                            prioridade_posicao[posicao_r],
                            nome_t,
                            nome_titular,
                            nome_reserva
                        ))
        
        # se a lista não tá vazia, há pelo menos uma substituição que melhora o time do Corinthians 
        if melhores_opcoes:
            # ordena a lista
            ordenar_opcoes(melhores_opcoes)

            # a melhor opção vai sempre pro indice 0
            melhor = melhores_opcoes[0]
            # pegando os pontos da melhor opção
            ganho_melhor = melhor[0]
            # pega as chaves dos jogadores
            chave_titular = melhor[3]
            chave_reserva = melhor[4]

            # efetua a substituição
            dados_gerais[tecnico]['titulares'][chave_titular] = reservas[chave_reserva]

            # agora sim a gente usa os pontos dos reservas, já atualizados
            pontuacao_total_dos_tecnicos[tecnico] += ganho_melhor

            # verifica que fez substituição
            tecnico_NAO_fez_substituicao[tecnico] = False
            substituicoes_feitas[tecnico] = (chave_titular, chave_reserva)

        else:
            tecnico_NAO_fez_substituicao[tecnico] = True
            substituicoes_feitas[tecnico] = None

    return substituicoes_feitas



# Código principal 

n = int(input())

# dicionários
dados_gerais = {}
pontuacao_total_dos_tecnicos = {}
pontuacao_titulares = {}
pontuacao_reservas = {}

# analisando o técnico
for c in range(n):
    nome_do_tecnico = input()

    # o nome do técnico é a chave maior
    dados_gerais[nome_do_tecnico] = {'titulares': {}, 'reservas': {}}
    # começa com 0 né
    pontuacao_total_dos_tecnicos[nome_do_tecnico] = 0
    # começa vazio
    pontuacao_titulares[nome_do_tecnico] = {}
    pontuacao_reservas[nome_do_tecnico] = {}

    continuar = True
    while continuar:
        # recebe o comando dos jogadores
        comando = input()

        if comando == 'titulares':
            for i in range(1, 12):
                informacoes_titulares = input()
                dados_gerais[nome_do_tecnico]['titulares'][f'jogador_{i}'] = informacoes_titulares

        elif comando == 'reservas':
            for i in range(1, 6):
                informacoes_reservas = input()
                dados_gerais[nome_do_tecnico]['reservas'][f'reserva_{i}'] = informacoes_reservas

        # a ordem não é necessariamente Titular -> Reserva, então, enquanto os dois não estiverem preenchidos, o loop não termina
        if dados_gerais[nome_do_tecnico]['titulares'] and dados_gerais[nome_do_tecnico]['reservas']:
            continuar = False


# output 1
print(f"Os técnicos que participarão da avaliação da rodada serão {', '.join(dados_gerais.keys())}.")


# criando um dict novo que a chave é o nome de cada técnico (como mencionei antes) e assumimos que ninguem fez substituição ainda
tecnico_NAO_fez_substituicao = {t: True for t in dados_gerais}
# copiando o dicionário de titulares antes das substituições
titulares_antes = {t: dados_gerais[t]['titulares'].copy() for t in dados_gerais}

# chamando função
substituicoes = cartola(dados_gerais, tecnico_NAO_fez_substituicao, pontuacao_total_dos_tecnicos, pontuacao_titulares, pontuacao_reservas)

# flags
vencedor = None
pontuacao_vencedor = -1

# iterando
for tecnico in dados_gerais:
    if substituicoes[tecnico] != None:
        titular, reserva = substituicoes[tecnico]

        nome_titular = titulares_antes[tecnico][titular].split(',')[0]
        nome_reserva = dados_gerais[tecnico]['reservas'][reserva].split(',')[0]

        # output 2
        print(f"{tecnico} é um gênio da bola mesmo, a substituição de {nome_titular} por {nome_reserva} fez ele ganhar pontos!")
    else:
        # output 3
        print(f"Pode cortar {tecnico} dos candidatos a técnico da amarelinha, nem fazer uma substituição ele consegue...")

    if pontuacao_total_dos_tecnicos[tecnico] > pontuacao_vencedor:
        pontuacao_vencedor = pontuacao_total_dos_tecnicos[tecnico]
        vencedor = tecnico

# output 4
print(f"{vencedor} é incrível ganhou essa rodada com {pontuacao_vencedor} pontos!")

# output 5
if tecnico_NAO_fez_substituicao[vencedor]:
    print(f"Temos que pedir desculpas a {vencedor}, mesmo sem fazer uma substituição ele foi o melhor da rodada, talvez ele deva assumir a amarelinha depois do Ancelotti!")
