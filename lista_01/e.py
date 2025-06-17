nome_cao1 = str(input())
pontuacao_cao1_prova_1 = int(input())
pontuacao_cao1_prova_2 = int(input())
pontuacao_cao1_prova_3 = int(input())

soma_cao1 = pontuacao_cao1_prova_1 + pontuacao_cao1_prova_2 + pontuacao_cao1_prova_3

if nome_cao1 == 'Byte':
    print('Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!')
elif soma_cao1 == 30:
    print(f'Com uma pontuação perfeita, {nome_cao1} conquista o título de mascote do CIn!')
else:
    nome_cao2 = str(input())
    pontuacao_cao2_prova_1 = int(input())
    pontuacao_cao2_prova_2 = int(input())
    pontuacao_cao2_prova_3 = int(input())

    soma_cao2 = pontuacao_cao2_prova_1 + pontuacao_cao2_prova_2 + pontuacao_cao2_prova_3

    if nome_cao2 == 'Byte':
        print('Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!')
    elif soma_cao2 == 30:
        print(f'Com uma pontuação perfeita, {nome_cao2} conquista o título de mascote do CIn!')
    else:
        nome_cao3 = str(input())
        pontuacao_cao3_prova_1 = int(input())
        pontuacao_cao3_prova_2 = int(input())
        pontuacao_cao3_prova_3 = int(input())

        soma_cao3 = pontuacao_cao3_prova_1 + pontuacao_cao3_prova_2 + pontuacao_cao3_prova_3

        if nome_cao3 == 'Byte':
            print('Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!')
        elif soma_cao3 == 30:
            print(f'Com uma pontuação perfeita, {nome_cao3} conquista o título de mascote do CIn!')
        else:
            if soma_cao1 < 15:
                print(f'Infelizmente {nome_cao1} está fora da disputa')
            if soma_cao2 < 15:
                print(f'Infelizmente {nome_cao2} está fora da disputa')
            if soma_cao3 < 15:
                print(f'Infelizmente {nome_cao3} está fora da disputa')


            if soma_cao1 > soma_cao2 and soma_cao1 > soma_cao3:
                print(f'Após uma disputa acirrada, o novo mascote do CIn é {nome_cao1}!')
            elif soma_cao2 > soma_cao1 and soma_cao2 > soma_cao3:
                print(f'Após uma disputa acirrada, o novo mascote do CIn é {nome_cao2}!')
            elif soma_cao3 > soma_cao1 and soma_cao3 > soma_cao2:
                print(f'Após uma disputa acirrada, o novo mascote do CIn é {nome_cao3}!')