quantidade_atletas = int(input())

vogais = 'a', 'e', 'i', 'o', 'u'



ranking_1 = ''
pontos_suspeito_1 = -1

ranking_2 = ''
pontos_suspeito_2 = -1

ranking_3 = ''
pontos_suspeito_3 = -1



if quantidade_atletas == 2:
    atleta_1 = str(input())
    posicao = int(input())
    ranking = int(input())
    velocidade = float(input())

    atleta_2 = str(input())
    posicao = int(input())
    ranking = int(input())
    velocidade = float(input())
    print(f'Caso encerrado: {atleta_1} e {atleta_2} roubaram o troféu!')
elif quantidade_atletas == 1:
    atleta_unico = str(input())
    posicao = int(input())
    ranking = int(input())
    velocidade = float(input())
    print(f'Não há dúvidas... {atleta_unico} é o culpado!')
else:
    for num_rodada in range(1, quantidade_atletas + 1):
        print(f'COMEÇANDO A {num_rodada}ª RODADA DE INVESTIGAÇÃO')
        atleta = str(input())
        posicao = int(input())
        ranking = int(input())
        velocidade = float(input())

        contador = 0
        pontos_de_suspeito = 0
        hum_suspeito = False

        for letra in atleta:
            if letra.lower() in vogais:
                contador += 1

        if contador % 2 == 0:
            pontos_de_suspeito += 10
        else:
            pontos_de_suspeito += 5


        if 45 <= posicao <= 135:
            print(f'{atleta} estava em posição estratégica para pegar o troféu... muito suspeito!')
            pontos_de_suspeito += 10
            hum_suspeito = True
        elif 225 <= posicao <= 315:
            pontos_de_suspeito += 5
        else:
            pontos_de_suspeito += 2
        
        if ranking <= 10:
            print(f'{atleta} é um dos melhores do mundo... e também um dos principais suspeitos!')
            pontos_de_suspeito += 10
            hum_suspeito = True
        elif 11 <= ranking < 50:
            pontos_de_suspeito += 5
        else:
            pontos_de_suspeito += 2
        
        if velocidade > 140:
            print(f'Alta velocidade detectada! {atleta} pode ter fugido rapidamente com o troféu!')
            pontos_de_suspeito += 10
            hum_suspeito = True
        elif 100 < velocidade < 140:
            pontos_de_suspeito += 5
        else:
            pontos_de_suspeito += 2

        if not hum_suspeito:
            print(f'Hum, esse {atleta} sei não viu... Deve tá escondendo alguma coisa.')
        

        if pontos_de_suspeito > pontos_suspeito_1:
            pontos_suspeito_3 = pontos_suspeito_2
            ranking_3 = ranking_2

            pontos_suspeito_2 = pontos_suspeito_1
            ranking_2 = ranking_1

            pontos_suspeito_1 = pontos_de_suspeito
            ranking_1 = atleta
        elif pontos_de_suspeito > pontos_suspeito_2:
            pontos_suspeito_3 = pontos_suspeito_2
            ranking_3 = ranking_2

            pontos_suspeito_2 = pontos_de_suspeito
            ranking_2 = atleta

        elif pontos_de_suspeito > pontos_suspeito_3:
            pontos_suspeito_3 = pontos_de_suspeito
            ranking_3 = atleta

    print()

    print('RESULTADOS DAS INVESTIGAÇÕES:')

    print()

    print('Os 3 principais suspeitos são:')
    print(f'1. {ranking_1} - {pontos_suspeito_1} pontos')
    print(f'2. {ranking_2} - {pontos_suspeito_2} pontos')
    print(f'3. {ranking_3} - {pontos_suspeito_3} pontos')

    print()

    if pontos_suspeito_1 == pontos_suspeito_2:
        print(f'Que absurdo... {ranking_1} e {ranking_2} roubaram o troféu juntos!')
    else:
        print(f'Mistério resolvido: O culpado é {ranking_1}! Ele roubou o troféu de Calderano.')
