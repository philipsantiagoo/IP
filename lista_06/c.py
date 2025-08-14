# Funções
def definindo_primeiros_segundos_ultimos_colocados(informes_gerais):

    resultados = {}

    # percorrendo informes gerais: vou olhar o dicionário maior e separar cada grupo pra ser analisado separadamente
    for grupo_atual, times_por_grupo in informes_gerais.items():
        # colocação dos times: aqui a gente quer os pontos mesmo: int() tlgd
        maior_pontuacao = 0
        segunda_maior_pontuacao = 0
        # qualquer valor é menor que esse (eu to supondo que os pontos sejam 'normais' né... se bem que se for o corinthians... aiai)
        menor_pontuacao = 999999

        # colocação dos times: aqui a gente quer os nomes ok - strings (eu to falando assim mais pra me ajudar do que pra vc que vai corrigir)
        primeiro_colocado = ''
        segundo_colocado = ''
        ultimo_colocado = ''

        # percorrendo agora os times por grupo: vou olhar time por time nessa budega pq é assim que a vida é e VAI CORINTHIANS!!!!!
        for time_atual, pontos in times_por_grupo.items():
            # suponto que o primeiro colocado tenha atualmente 1000 pontos
            if pontos > maior_pontuacao:
                # eita, chegou uma pontuação maior na área, o segundo pega a pontuação anterior
                segunda_maior_pontuacao = maior_pontuacao
                segundo_colocado = primeiro_colocado
                # esse recebe a maior pontuação
                maior_pontuacao = pontos
                primeiro_colocado = time_atual
            
            elif pontos > segunda_maior_pontuacao and pontos != maior_pontuacao:
                segunda_maior_pontuacao = pontos
                segundo_colocado = time_atual
            
            if pontos < menor_pontuacao:
                menor_pontuacao = pontos
                ultimo_colocado = time_atual
        
        resultados[grupo_atual] = {
            'primeiro': primeiro_colocado,
            'segundo': segundo_colocado,
            'ultimo': ultimo_colocado
        }
    
    return resultados

                
# Código principal
# Que fique claro: sou corintiano então é bom que um test case tenha o Corinthians vencendo.


# informes gerais: {{}, {}, {}, ...}
informes_gerais = {}

qtd_grupos = int(input())

for c in range(1, qtd_grupos + 1):
    # dicionários internos para organizar, cada grupo tem seu próprio dicionário de 4 times
    # times por grupo: {{'...', '...', '...', '...'}, ...}
    times_por_grupo = {}

    for i in range(4):
        # recebendo os nomes e pontos
        nome_timeX_pontuação_timeX = input()
        nome_time, pontuacao = nome_timeX_pontuação_timeX.split(' - ')
        # nome_time é a chave do time, a chave do grupo é logo abaixo 'nome_do_grupo', nome_time recebe o valor (pontuação) do time
        # {{'Corinthians': 999, 'Palmeiras': -1, 'São Paulo': -100, 'Flamengo': -1000000}, ...}
        times_por_grupo[nome_time] = int(pontuacao)
    
    # organização ne pai, agora que tuplas são permitidas... e nem espere que eu use recursão!
    nome_do_grupo = c
    # nome do grupo: {'Grupo 1': {'Corinthians': 999, 'Palmeiras': -1, 'São Paulo': -100, 'Flamengo': -1000000}, 'Grupo 2': {}, 'Grupo 3': {}, 'Grupo 4': {}, ...}
    informes_gerais[nome_do_grupo] = times_por_grupo


# Definindo a disputa
confrontos = []
for disputa in range(qtd_grupos // 2):
    confronto = input()
    confrontos.append(confronto)


# Outputs - confrontos
if qtd_grupos < 2 or qtd_grupos % 2 == 1:             
    print(f'Mas como que vamos fazer um torneio com {qtd_grupos} grupos Samir!?')

else:
    print('Roda os dados Samir!')
    print()

    colocacoes = definindo_primeiros_segundos_ultimos_colocados(informes_gerais)

    ultimos_colocados = []

    # trata dos times
    rodadas = 1
    for confronto in confrontos:
        timeA, timeB = confronto.split(' x ')
        timeA = int(timeA)
        timeB = int(timeB)

        primeiroA = colocacoes[timeA]['primeiro']
        primeiroB = colocacoes[timeB]['primeiro']

        segundoA = colocacoes[timeA]['segundo']
        segundoB = colocacoes[timeB]['segundo']

        ultimoA = colocacoes[timeA]['ultimo']
        ultimoB = colocacoes[timeB]['ultimo']

        ultimos_colocados.append(ultimoA)
        ultimos_colocados.append(ultimoB)

        # outputs
        print(f'Confrontos chave {rodadas}:')
        print(f'{primeiroA} x {segundoB}')
        print(f'{segundoA} x {primeiroB}')
        print()

        rodadas += 1


    # outputs
    # acessando os últimos colocados diretamente do input, ao invés do confronto
    for grupo in range(1, qtd_grupos + 1):
        ultimo = colocacoes[grupo]['ultimo']
        print(f'O time {ultimo} ficou em último lugar em seu grupo e foi rebaixado!')
