# Funções
def semifinal(dict_semifinal, ranking_fase1, gols_jogadores, jogador_time):
    jogos_e_gols_semifinal = {}
    vencedores = {}

    # Preparar tupla com os quatro times classificados
    times_classificados = ()
    for time in dict_semifinal:
        times_classificados += (time,)

    # Organizar os jogos: (0 x 3) e (1 x 2)
    jogos = {
        'Jogo_1': (times_classificados[0], times_classificados[3]),
        'Jogo_2': (times_classificados[1], times_classificados[2])
    }

    for nome_jogo in jogos:
        print('Vai começar o confronto, quem será que vence?')

        time1 = jogos[nome_jogo][0]
        time2 = jogos[nome_jogo][1]

        jogos_e_gols_semifinal[nome_jogo] = {}
        placar = {}

        entrada = ''
        contador = 1

        while entrada != 'FIM':
            entrada = input()
            if entrada != 'FIM':
                jogador, time = entrada.split(' - ')
                chave = f'goleador_{contador}'
                jogos_e_gols_semifinal[nome_jogo][chave] = (jogador, time)

                # Atualizar placar
                if time not in placar:
                    placar[time] = 0
                placar[time] += 1

                # artilharia 
                chave_jogador = f'{jogador} - {time}'

                if chave_jogador not in gols_jogadores:
                    gols_jogadores[chave_jogador] = 0
                gols_jogadores[chave_jogador] += 1

                if chave_jogador not in jogador_time:
                    jogador_time[chave_jogador] = time

                print(f'Gol do {time}, {jogador} é o nome da emoção')
                contador += 1

        print('Fim de jogo.')

        # Garantir que os dois times estejam no placar com 0 se necessário
        if time1 not in placar:
            placar[time1] = 0
        if time2 not in placar:
            placar[time2] = 0

        gols1 = placar[time1]
        gols2 = placar[time2]

        # Mostrar o placar
        if gols1 > gols2:
            print(f'Placar: {time1} {gols1} X {gols2} {time2}')
            print(f'O {time1} venceu e foi para a final, será que vai ser campeão?')
            vencedores[nome_jogo] = time1

        elif gols2 > gols1:
            print(f'Placar: {time2} {gols2} X {gols1} {time1}')
            print(f'O {time2} venceu e foi para a final, será que vai ser campeão?')
            vencedores[nome_jogo] = time2

        else:
            # Desempate com base no ranking da fase 1
            vencedor_empate = ''
            encontrado = False

            for time in ranking_fase1:
                if not encontrado:
                    if time == time1:
                        vencedor_empate = time1
                        encontrado = True
                    elif time == time2:
                        vencedor_empate = time2
                        encontrado = True

            print(f'Placar: {time1} {gols1} X {gols2} {time2}')
            print(f'O {vencedor_empate} passa para a final após vencer nos pênaltis, será que vai ser campeão?')
            vencedores[nome_jogo] = vencedor_empate

    return vencedores




def final(vencedores_semifinal, ranking_fase1, gols_jogadores, jogador_time):
    print('Vai começar a grande decisão, quem será o campeão brasileiro de 1987?')

    time1 = vencedores_semifinal['Jogo_1']
    time2 = vencedores_semifinal['Jogo_2']

    placar = {time1: 0, time2: 0}

    entrada = ''
    contador = 1

    while entrada != 'FIM':
        entrada = input()
        if entrada != 'FIM':
            jogador, time = entrada.split(' - ')

            # Atualizar placar
            if time not in placar:
                placar[time] = 0
            placar[time] += 1

            chave_jogador = f'{jogador} - {time}'

            if chave_jogador not in gols_jogadores:
                gols_jogadores[chave_jogador] = 0
            gols_jogadores[chave_jogador] += 1

            if chave_jogador not in jogador_time:
                jogador_time[chave_jogador] = time



            print(f'Gol do {time}, {jogador} é o nome da emoção')
            contador += 1

    print('Fim de jogo.')

    gols1 = placar[time1]
    gols2 = placar[time2]

    if gols1 > gols2:
        print(f'Placar: {time1} {gols1} X {gols2} {time2}')
        campeão = time1
        vice = time2

    elif gols2 > gols1:
        print(f'Placar: {time2} {gols2} X {gols1} {time1}')
        campeão = time2
        vice = time1

    else:
        # Desempate com base no ranking da fase 1
        vencedor_empate = ''
        vice_temp = ''

        for time in ranking_fase1:
            if vencedor_empate == '':
                if time == time1:
                    vencedor_empate = time1
                    vice_temp = time2
                elif time == time2:
                    vencedor_empate = time2
                    vice_temp = time1

        print(f'Placar: {time1} {gols1} X {gols2} {time2}')
        campeão = vencedor_empate
        vice = vice_temp
    
    # artilharia
    maior_gols = -1
    lista_artilheiros = ()

    for jogador in gols_jogadores:
        gols = gols_jogadores[jogador]
        if gols > maior_gols:
            maior_gols = gols
            lista_artilheiros = (jogador,)
        elif gols == maior_gols:
            lista_artilheiros += (jogador,)

    if maior_gols <= 0:
        artilheiro = 'nenhum'
    else:
        # Desempate por ordem alfabética
        artilheiro = min(lista_artilheiros)

    return campeão, vice, artilheiro




# Código principal
dict_time_estado_regiao = {
    'Norte': ('AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO'),
    'Nordeste': ('AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'),
    'Centro-Oeste': ('DF', 'GO', 'MT', 'MS'),
    'Sudeste': ('ES', 'MG', 'RJ', 'SP'),
    'Sul': ('PR', 'RS', 'SC')
}

# Dicionário para armazenar os clubes por região
dict_times_por_regiao = {
    'Norte': {},
    'Nordeste': {},
    'Centro-Oeste': {},
    'Sudeste': {},
    'Sul': {}
}

clube = ''
qtd_de_time = 0

while clube != 'FIM' and qtd_de_time < 6:
    clube = input()

    if clube != 'FIM':
        estado = input()

        regiao_do_estado = ''  

        # achando a região do estado
        for regiao in dict_time_estado_regiao:
            if regiao_do_estado == '':  # só se ainda não foi achada
                estados = dict_time_estado_regiao[regiao]
                for i in range(len(estados)):
                    if estados[i] == estado:
                        regiao_do_estado = regiao

        if regiao_do_estado == '':
            print('Estado inválido.')
        else:
            times_da_regiao = dict_times_por_regiao[regiao_do_estado]
            if len(times_da_regiao) >= 2:
                print(f'Cota para a região {regiao_do_estado} atingida. Por favor, insira um clube de outro estado, de outra região.')
            else:
                novo_nome = f'time_{len(times_da_regiao)+1}'
                times_da_regiao[novo_nome] = clube
                qtd_de_time += 1


# output 2
if clube == 'FIM' and qtd_de_time != 6:
    print(f'Ai não dá, com {qtd_de_time} somente não dá para fazer um campeonato, essa ideia de Copa União foi um fiasco mesmo, #VOLTACBF')
else:
    # input 2
    # variáveis
    vitoria = 3
    empate = 1
    derrota = 0

    # dicionário de confrontos 
    dict_confrontos = {}

    for confronto in range(1, 16):
        confrontos = input()

        dict_confrontos[f'Confronto_{confronto}'] = confrontos


    # dicionário para armazenar os pontos do time, com saldos de gols feitos e sofridos: {'Corinthians': {'pontos': 999, 'gols feitos': 200, 'gols sofridos': 0}, ...}
    dict_pontos = {}

    for i in range(1, 16):
        tretas = dict_confrontos[f'Confronto_{i}']

        # repartindo
        dados = tretas.split()

        # me baseando no X, Guilherme esculhambou tbm viu, pourran...
        posicao_do_X = dados.index('X')

        time1 = ' '.join(dados[:posicao_do_X - 1])
        gols1 = int(dados[posicao_do_X - 1])

        time2 = ' '.join(dados[posicao_do_X + 2:])
        gols2 = int(dados[posicao_do_X + 1])

        # eita, tem ninguêm ainda
        if time1 not in dict_pontos:
            dict_pontos[time1] = {'pontos': 0, 'gols feitos': 0, 'gols sofridos': 0}
        if time2 not in dict_pontos:
            dict_pontos[time2] = {'pontos': 0, 'gols feitos': 0, 'gols sofridos': 0}
        
        # gols, gols, GOOOOOOOOOOOOOOOOOLLLLLL DO CORINTHIAAAAAAAAANS
        dict_pontos[time1]['gols feitos'] += gols1
        dict_pontos[time1]['gols sofridos'] += gols2

        dict_pontos[time2]['gols feitos'] += gols2
        dict_pontos[time2]['gols sofridos'] += gols1

        # Brasileirão 2025: "Mais um Brasileirão e o IMPARÁVEL Corinthians assume a liderança"
        if gols1 > gols2:
            dict_pontos[time1]['pontos'] += vitoria
            dict_pontos[time2]['pontos'] += derrota
        elif gols1 < gols2:
            dict_pontos[time1]['pontos'] += derrota
            dict_pontos[time2]['pontos'] += vitoria
        else:
            dict_pontos[time1]['pontos'] += empate
            dict_pontos[time2]['pontos'] += empate


    # dicionário da organização básica
    ranking_fase1 = {}

    while len(ranking_fase1) < len(dict_pontos):
        maior_pontos = -1
        melhor_saldo_de_gols = -1000
        time_mais_bem_pontuado = None

        for time in dict_pontos:
            if time not in ranking_fase1:
                pontos = dict_pontos[time]['pontos']

                # saldo de gols lá (ridículo o primeiro input fazer o Corinthians tomar 10 gols)
                saldo_de_gols = dict_pontos[time]['gols feitos'] - dict_pontos[time]['gols sofridos']

                # se tiver mais pontos, ou se tiver mesmo pontos e saldo maior, atualiza
                if (pontos > maior_pontos) or (pontos == maior_pontos and saldo_de_gols > melhor_saldo_de_gols):
                    maior_pontos = pontos
                    melhor_saldo_de_gols = saldo_de_gols
                    time_mais_bem_pontuado = time
        
        # organizando do melhor ao pior, e já deu pra ver que Guilherme não gosta do brilho do Corinthians
        ranking_fase1[time_mais_bem_pontuado] = dict_pontos[time_mais_bem_pontuado]


    # output 3
    for time in ranking_fase1:
        print(f'{time} - {ranking_fase1[time]["pontos"]} pontos')


    # adicionando os times para a semifinal
    dict_semifinal = {}
    contador = 0

    for time in ranking_fase1:
        if contador < 4:
            dict_semifinal[time] = ranking_fase1[time]
            contador += 1


    # output 4
    print('Os confrontos foram definidos:')

    # escolhendo os 4 times que avançaram para a semifnial para disputarem!
    times_classificados = ()

    for time in dict_semifinal:
        times_classificados += (time,)

    print(f'{times_classificados[0]} X {times_classificados[3]}')
    print(f'{times_classificados[1]} X {times_classificados[2]}')

    # chamando a função
    gols_jogadores = {}
    jogador_time = {}
    vencedores_semifinal = semifinal(dict_semifinal, ranking_fase1, gols_jogadores, jogador_time)


    # final
    campeao, vice, artilheiro = final(vencedores_semifinal, ranking_fase1, gols_jogadores, jogador_time)

    campeao_original = campeao
    vice_original = vice

    # Regras de repasse de título — ajustadas conforme nova lógica
    times_da_semifinal = ()
    for time in dict_semifinal:
        times_da_semifinal += (time,)

    # CASO 1: Sport campeão
    if campeao_original == 'Sport':
        print("Quem deixou o Sport participar, a Copa União só permite clubes grandes de participarem, tirem ele daqui que do jeito que eles são é capaz de irem no tribunal pedir o reconhecimento do 'Brasileiro de Questão de IP'")

        if vice_original == 'Santa Cruz':
            print('O terror do Nordeste agradece o reconhecimento, porém recusa o titulo, diferente do seu rival ele prefere ganhar o título em campo, e não em imaginação')

            # Passar para melhor semifinalista restante (que não seja Sport ou Santa)
            novo_campeao = ''
            maior_pontuacao = -1
            for time in ranking_fase1:
                if time in times_da_semifinal and time != 'Sport' and time != 'Santa Cruz':
                    pontos = ranking_fase1[time]['pontos']
                    if pontos > maior_pontuacao:
                        maior_pontuacao = pontos
                        novo_campeao = time
            if novo_campeao != '':
                campeao = novo_campeao
        else:
            # título vai para o vice diretamente
            campeao = vice_original

    # CASO 2: Santa Cruz campeão
    elif campeao_original == 'Santa Cruz':
        print('O terror do Nordeste agradece o reconhecimento, porém recusa o titulo, diferente do seu rival ele prefere ganhar o título em campo, e não em imaginação')

        if vice_original == 'Sport':
            print("Quem deixou o Sport participar, a Copa União só permite clubes grandes de participarem, tirem ele daqui que do jeito que eles são é capaz de irem no tribunal pedir o reconhecimento do 'Brasileiro de Questão de IP'")

            # Passar para melhor semifinalista restante (que não seja Sport ou Santa)
            novo_campeao = ''
            maior_pontuacao = -1
            for time in ranking_fase1:
                if time in times_da_semifinal and time != 'Sport' and time != 'Santa Cruz':
                    pontos = ranking_fase1[time]['pontos']
                    if pontos > maior_pontuacao:
                        maior_pontuacao = pontos
                        novo_campeao = time
            if novo_campeao != '':
                campeao = novo_campeao
        else:
            # título vai para o vice diretamente
            campeao = vice_original

    # Mensagem final do campeão reconhecido
    if campeao == 'Flamengo':
        print('Em 1987, o Flamengo é o campeão inquestionável! Conquistou na bola e com o reconhecimento merecido. Qualquer outra conversa é história para boi dormir.')
    else:
        print(f'E o campeão do real Campeonato Brasileiro de 1987 foi o {campeao}, ouvi dizer que a CBF tava querendo fazer um outro campeonato chamado módulo amarelo, ainda bem que todo mundo entendeu que aquilo é somente uma serie B')


    # Verificar e imprimir mensagem sobre o artilheiro
    if artilheiro == 'nenhum':
        print('Esse ano o nivel foi fraco, não tivemos um artilheiro')

    else:
        # Encontrar o time do artilheiro no dicionário gols_jogadores
        achou_time = jogador_time[artilheiro]
        nome_artilheiro = artilheiro.split(' - ')[0]

        if achou_time == campeao:
            print(f'{nome_artilheiro} garantiu o título do campeonato e a artilharia, que ano feliz para ele')
        else:
            print(f'Apesar de não ter sido campeão, pelo menos {nome_artilheiro} foi o artilheiro, a culpa não foi dele')
