fome = str(input()).lower()

if fome == 'sim':
    comida = str(input()).lower()
    print('O Byte está com fome?')
    print('O que você vai dar para ele comer?')
    if comida == 'carne' or comida == 'ração' or comida == 'petisco':
        print(f'Byte comeu {comida} e está feliz!')
        print('Depois desse banquete, Byte pode tirar um cochilo feliz')
    else:
        print(f'Byte não gosta de {comida}')
        print('Byte se irritou e foi dormir pra ver se sonha com suas refeições prediletas...')

elif fome == 'não':
    chovendo = str(input()).lower()
    print('O Byte está com fome?')
    print('Já que Byte não está com fome, ele pode passear')
    print('Está chovendo?')
    if chovendo == 'sim':
        print('Já que está chovendo, Byte vai ter que brincar em casa')
    elif chovendo == 'não':
        print('Byte está indo passear')
    else:
        print('Insira uma resposta válida')

else:
    print('Insira uma resposta válida')