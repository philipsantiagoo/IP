# Definindo a lista de locais em Paris
Paris = [
    'Torre Eiffel',
    'Museu do Louvre',
    'Catacombas de Paris',
    'Biblioteca Nacional',
    'Galeria Lafayette',
    'Parque dos Príncipes',
    'Catedral de Notre-Dame',
    'Jardim de Luxemburgo',
    'Padaria Dupain Cheng'
]

# Definindo a lista de horários para o início e fim do dia
horarios_inicio = ['09:00', '08:00', '10:00', '07:00', '10:00', '06:00', '08:00', '07:00', '04:00']
horarios_fim = ['23:00', '18:00', '20:00', '22:00', '21:00', '23:00', '18:30', '19:00', '20:00']

# Definindo a entrada de suspeitos e o contador de suspeitos
entrada = []
contador = 1

# Definindo o loop
while contador <= 6:
    entrada.append(input())
    contador += 1

# Definindo as listas para armazenar os dados dos suspeitos
nome = []
horario = []
local = []
testemunha = []

# Separando os dados dos suspeitos em suas respectivas listas
for suspeito in entrada:
    dados = suspeito.split(' - ')
    nome.append(dados[0])
    horario.append(dados[1])
    local.append(dados[2])
    testemunha.append(dados[3])


# Verifica se local é válido, se não for, adiciona à lista de inválidos e seu respectivo suspeito
invalidos = []

for i in range(len(local)):
    if local[i] not in Paris:
        invalidos.append([local[i], nome[i]])

if invalidos:
    # Separa novamente os locais e suspeitos ordenados
    locais_invalidos = [lugar for lugar, suspeito in invalidos]
    suspeitos_invalidos = [suspeito for lugar, suspeito in invalidos]

    locais_invalidos.sort()
    suspeitos_invalidos.sort()

    if len(locais_invalidos) == 1:
        print(f'Esse lugar {locais_invalidos[0]} nem existe! {suspeitos_invalidos[0]} com certeza foi akumatizado!')
    else:
        print(f"{', '.join(locais_invalidos)} nem existem! {', '.join(suspeitos_invalidos)} estão mentindo!")


# Verifica se o local é válido, se for, verifica se o horário é válido
else:
    # Lista de horários inválidos
    horarios_invalidos = []
    # Verificando se o horário está dentro do intervalo permitido
    for i in range(len(local)):
        # Pegamos o índice do local na lista Paris
        indice_local = 0
        encontrou = False
        while indice_local < len(Paris) and not encontrou:
            if Paris[indice_local] == local[i]:
                encontrou = True
            else:
                indice_local += 1
        
        horario_suspeito = int(horario[i][0:2]) * 60 + int(horario[i][3:5])

        total_inicio = int(horarios_inicio[indice_local][0:2]) * 60 + int(horarios_inicio[indice_local][3:5])
        total_fim = int(horarios_fim[indice_local][0:2]) * 60 + int(horarios_fim[indice_local][3:5])

        if horario_suspeito < total_inicio or horario_suspeito > total_fim:
            horarios_invalidos.append([local[i], nome[i], i])

    if horarios_invalidos:
        locais_horarios = [item[0] for item in horarios_invalidos]
        suspeitos_horarios = [item[1] for item in horarios_invalidos]
        indices_horarios = [item[2] for item in horarios_invalidos]

        locais_horarios.sort()
        suspeitos_horarios.sort()

        if len(locais_horarios) == 1:
            indice_hora = indices_horarios[0]
            print(f'{locais_horarios[0]} nem estava aberto às {horario[indice_hora]}! {suspeitos_horarios[0]} recebeu memórias falsas!')
        else:
            print(f'{", ".join(locais_horarios)} estavam fechados nesse horário! {", ".join(suspeitos_horarios)} podem ter sido manipulados pelo Hawk Moth!')
    
    # Se todos os locais e horários forem válidos, verifica a segurança baixa com todos os álibis válidos
    else:
        # Lista para armazenar locais de baixa segurança
        locais_baixa_seguranca = ['Catacumba de Paris', 'Parque dos Príncipes', 'Padaria Dupain Cheng']

        # Analisando se algum meliante esteve em um local de baixa segurança
        suspeitos_baixa_seguranca = []
        for i in range(len(local)):
            if local[i] in locais_baixa_seguranca:
                suspeitos_baixa_seguranca.append([local[i], nome[i]])
        
        if suspeitos_baixa_seguranca:
            suspeitos_baixa_seguranca.sort()

            locais_baixa = [lugar for lugar, suspeito in suspeitos_baixa_seguranca]
            suspeitos_baixa = [suspeito for lugar, suspeito in suspeitos_baixa_seguranca]

            if len(locais_baixa) == 1:
                print(f'{suspeitos_baixa[0]} estava em um local de segurança baixa... Ele pode ter mentido!')
            else:
                print(f"{', '.join(suspeitos_baixa)} estavam em locais de segurança baixa... Eles podem estar forjando um álibi!")
        
        # Se não tem local inválido, horário inválido ou segurança baixa, verifica se todos os suspeitos têm testemunhas
        else: 
            testemunhas_ausentes = []

            for i in range(len(testemunha)):
                if testemunha[i] == 'nenhuma':
                    testemunhas_ausentes.append([local[i], nome[i]])
            
            if testemunhas_ausentes:
                locais_testemunhas = [lugar for lugar, suspeito in testemunhas_ausentes]
                suspeitos_testemunhas = [suspeito for lugar, suspeito in testemunhas_ausentes]

                locais_testemunhas.sort()
                suspeitos_testemunhas.sort()

                if len(locais_testemunhas) == 1:
                    print(f'{suspeitos_testemunhas[0]} não teve testemunha para confirmar o álibi. É o mais suspeito até agora.')
                elif 1 < len(locais_testemunhas) < 6:
                    print(f"{', '.join(suspeitos_testemunhas)} não foram confirmados por ninguém. O Hawk Moth pode vir atrás deles de novo")
                else:
                    print('Ninguém viu ninguém… estranho!!')
            # Se tá todo mundo limpo
            else:
                print('Poxa vida, todos os àlibis parecem válidos… mas algo continua errado')

