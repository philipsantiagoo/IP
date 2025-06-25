# Lista dos alfabetos: codificado e normal
alfabeto_codificado = [
    'k', 'q', 'f', 'm', 'x', 'e', 't', 'z', 'r', 'h', 'v', 'n', 'd', 'l', 'j', 'a', 's', 'u', 'y', 'b', 'g', 'w', 'p', 'o', 'i', 'c', ' '
]

alfabeto_normal = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '
]

# Lista do teen team
teen_team = [
    'rex splode', 'duplikate', 'atom eve', 'robot'
]

# Lista dos inimigos
nomes_inimigos = [
    ['general kregg'], ['conquista'], ['anissa']

]

poder_inimigos = [
    [110], [100], [90]
]

# Definindo a listas de nomes e poderes
nomes_herois = []
poder_herois = []


# Definindo o número de equipes
n = int(input())


# Loop de equipes
contador = 1
while contador <= n:
    nomes_herois.append([])
    poder_herois.append([])
    contador += 1


# Loop das ações
acao = ''
while acao != 'FIM':
    acao = input()

    # Se for adicionar heróis
    if acao == 'adicionar':
        print('Quem será o próximo integrante do time?')
        nome_poder = input()
        time = int(input())

        # Separando o nome dos poderes
        if ' - ' in nome_poder:
            divisao_nome_poder = nome_poder.split(' - ')
            nome = divisao_nome_poder[0].strip()
            poder = divisao_nome_poder[1].strip()
        
        # Decodificando o nome do herói
        nome_decodificado = ''
        for letra in nome:
            for indice in range(len(alfabeto_codificado)):
                if letra == alfabeto_codificado[indice]:
                    nome_decodificado += alfabeto_normal[indice]
        
        
        # Adicionando o nome e seu poder nas listas, de acordo com seus índices
        if 0 <= time < len(nomes_herois):
            nomes_herois[time].append(nome_decodificado)
            poder_herois[time].append(poder)

            # Verificação do teen team
            if nome_decodificado == 'rex splode':
                print('Eu vou te detonar!')
            elif nome_decodificado == 'atom eve':
                print('Eu reescrevo a matéria... incluindo a SUA.')
            elif nome_decodificado == 'duplikate':
                print('Quantas de mim você acha que consegue lidar?')
            elif nome_decodificado == 'robot':
                print('Minha lógica diz que você vai perder.')
    
    
    # Se tiver um metamorfo 
    elif acao == 'metamorfo':
        print('Atenção!!! Metamorfo encontrado, quem deverá ser removido do time?')

        nome_decodificado = input()
        time_encontrado = -1
        posicao = -1
        achou = False

        # Procurando o herói nas equipes
        for i in range(len(nomes_herois)):
            if achou == False:
                for j in range(len(nomes_herois[i])):
                    if nomes_herois[i][j] == nome_decodificado:
                        time_encontrado = i
                        posicao = j
                        achou = True
        
        
        # Achou o maluco
        if time_encontrado != -1:
            nomes_herois[time_encontrado].pop(posicao)
            poder_herois[time_encontrado].pop(posicao)

            print('Quem você gostaria de colocar no lugar?')
            novo_nome_poder = input()

            # Separando o nome dos poderes
            if ' - ' in novo_nome_poder:
                divisao_novo_nome_poder = novo_nome_poder.split(' - ')
                nome_codificado = divisao_novo_nome_poder[0].strip()
                poder = divisao_novo_nome_poder[1].strip()
            
            # Decodificando o nome do herói
            novo_nome_decodificado = ''
            for letra in nome_codificado:
                for indice in range(len(alfabeto_codificado)):
                    if letra == alfabeto_codificado[indice]:
                        novo_nome_decodificado += alfabeto_normal[indice]
            
            # Inserindo nas mesmas posições
            nomes_herois[time_encontrado].insert(posicao, novo_nome_decodificado)
            poder_herois[time_encontrado].insert(posicao, poder)

            # Verificando o  teen team
            if novo_nome_decodificado == 'rex splode':
                print('Eu vou te detonar!')
            elif novo_nome_decodificado == 'atom eve':
                print('Eu reescrevo a matéria... incluindo a SUA.')
            elif novo_nome_decodificado == 'duplikate':
                print('Quantas de mim você acha que consegue lidar?')
            elif novo_nome_decodificado == 'robot':
                print('Minha lógica diz que você vai perder.')


# Verificando se o teen team está completamente formado
indice_time = 0
teenTeam = False

while indice_time < len(nomes_herois):
    membros_encontrados = 0
    indice_teen = 0

    while indice_teen < len(teen_team):
        nome = teen_team[indice_teen]
        # Se nome está em nome_herois
        if nome in nomes_herois[indice_time]:
            membros_encontrados += 1
        indice_teen += 1
    
    if membros_encontrados == 4 and teenTeam == False:
        print('O teen team esta completo, Cecil esta muito contente!')
        teenTeam = True

        # Buf de poder pq heróis sempre tem vantagem blá, blá, blá
        indice_poder = 0
        while indice_poder < len(poder_herois[indice_time]):
            poder_str = poder_herois[indice_time][indice_poder]
            poder_num = float(poder_str)
            # Buf ridículo
            novo_poder = poder_num * 1.1
            # Caçando os heróis pra bufar todo mundo 
            poder_herois[indice_time][indice_poder] = str(round(novo_poder, 2))
            indice_poder += 1
    
    indice_time += 1


# Verificando o time de maior poder
indice_time = 0
maior_poder = -1
indice_maior = -1

while indice_time < len(poder_herois):
    soma_poder = 0
    indice_poder = 0

    while indice_poder < len(poder_herois[indice_time]):
        soma_poder += float(poder_herois[indice_time][indice_poder])
        indice_poder += 1
    
    if soma_poder > maior_poder:
        maior_poder = soma_poder
        indice_maior = indice_time

    indice_time += 1

# Verificando se o time tem pelo menos 3 integrantes, para tretar com os inimigos
if indice_maior != -1 and len(nomes_herois[indice_maior]) >= 3:
    time_nomes = nomes_herois[indice_maior]
    time_poderes = poder_herois[indice_maior]

    # Cria lista de (nome, poder float)
    lista_herois = []
    i = 0
    while i < len(time_nomes):
        lista_herois.append((time_nomes[i], float(time_poderes[i])))
        i += 1

    # Seleciona top 3 heróis (sem ordenar tudo, só pega os 3 maiores)
    top_herois = []
    while len(top_herois) < 3:
        maior_poder = -1
        indice_maior_heroi = -1
        j = 0
        while j < len(lista_herois):
            if lista_herois[j][1] > maior_poder:
                maior_poder = lista_herois[j][1]
                indice_maior_heroi = j
            j += 1
        top_herois.append(lista_herois[indice_maior_heroi])
        lista_herois.pop(indice_maior_heroi)

    # Imprime o time
    print("Aqui está o poderoso time da terra: {}, {}, {}".format(
        top_herois[0][0], top_herois[1][0], top_herois[2][0]
    ))

    # Organiza inimigos por poder (decrescente)
    inimigos = []
    i = 0
    while i < len(nomes_inimigos):
        inimigos.append((nomes_inimigos[i][0], poder_inimigos[i][0]))
        i += 1

    # Seleciona os top 3 inimigos (mesma lógica)
    top_inimigos = []
    while len(top_inimigos) < 3 and len(inimigos) > 0:
        maior_poder = -1
        indice_maior_inimigo = -1
        j = 0
        while j < len(inimigos):
            if inimigos[j][1] > maior_poder:
                maior_poder = inimigos[j][1]
                indice_maior_inimigo = j
            j += 1
        top_inimigos.append(inimigos[indice_maior_inimigo])
        inimigos.pop(indice_maior_inimigo)

    # Rodada dos duelos
    rodada = 1
    vitorias_herois = 0
    vitorias_inimigos = 0
    i = 0
    while i < len(top_herois) and i < len(top_inimigos):
        print("{} Duelo: {} X {}".format(rodada, top_herois[i][0], top_inimigos[i][0]))
        if top_herois[i][1] > top_inimigos[i][1]:
            vitorias_herois += 1
        else:
            vitorias_inimigos += 1
        rodada += 1
        i += 1

    # Resultado final
    if vitorias_herois > vitorias_inimigos:
        print("A terra venceu!")
    else:
        print("Infelizmente o imperio viltrumita conquistou a terra!")
