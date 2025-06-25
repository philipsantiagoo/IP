# Exibindo a mensagem inicial
print('Vamos lá, Vanellope! Vou te ajudar a montar um carro CINistro!')

# Definindo a lista do carro montado
carro_montado = [None, None, None]

# Definindo as listas de peças
estrutura = [None] # corresponde ao elemento 0 da lista do carro montado
volante = [None] # corresponde ao elemento 1 da lista do carro montado
roda = [None] # corresponde ao elemento 2 da lista do carro montado

# Definindo a lista de descarte
descarte = []

# Definindo a entrada do usuário
entrada = ''

# Loop para receber a entrada do usuário
while entrada != 'Recursos Esgotados':
    entrada = input()

    if 'estragado' in entrada:
        # Adiciona a peça estragada à lista de descarte
        descarte.append(entrada)

    # Verifica a entrada de sabotagem
    if 'O REI DOCE ESTÁ ROUBANDO TODOS OS INGREDIENTES!' in entrada:
        print('Ah não!! Ele vai destruir seu carro, Vanellope! CUIDADO')
        # Remove a peça das listas de peças e adiciona ao descarte
        if roda[0] is not None:
            descarte.append(roda[0])
            roda[0] = None
        if estrutura[0] is not None:
            descarte.append(estrutura[0])
            estrutura[0] = None
        if volante[0] is not None:
            descarte.append(volante[0])
            volante[0] = None
        
        estrutura.clear()
        volante.clear()
        roda.clear()
        estrutura.append(None)
        volante.append(None)
        roda.append(None)
    
    # Verifica a substituição de doces 
    # Estrutura
    if 'Bolo de rolo' in entrada or 'Barra de chocolate' in entrada or 'Banda de ovo de Páscoa' in entrada:
        if 'alta qualidade' in entrada:
            if estrutura[0] is None:
                estrutura[0] = entrada
            elif 'alta qualidade' in estrutura[0]:
                descarte.append(entrada)
            elif 'qualidade mediana' in estrutura[0]:
                descarte.append(estrutura[0])
                estrutura[0] = entrada
        elif 'qualidade mediana' in entrada:
            if estrutura[0] is None:
                estrutura[0] = entrada
            else:
                descarte.append(entrada)

    # Volante
    if 'Pretzel' in entrada or 'Donuts' in entrada:
        if 'alta qualidade' in entrada:
            if volante[0] is None:
                volante[0] = entrada
            elif 'alta qualidade' in volante[0]:
                descarte.append(entrada)
            elif 'qualidade mediana' in volante[0]:
                descarte.append(volante[0])
                volante[0] = entrada
        elif 'qualidade mediana' in entrada:
            if volante[0] is None:
                volante[0] = entrada
            else:
                descarte.append(entrada)

    # Roda
    if 'Mentos' in entrada or 'Jujuba' in entrada:
        if 'alta qualidade' in entrada:
            if roda[0] is None:
                roda[0] = entrada
            elif 'alta qualidade' in roda[0]:
                descarte.append(entrada)
            elif 'qualidade mediana' in roda[0]:
                descarte.append(roda[0])
                roda[0] = entrada
        elif 'qualidade mediana' in entrada:
            if roda[0] is None:
                roda[0] = entrada
            else:
                descarte.append(entrada)
    
carro_montado[0] = estrutura[0]
carro_montado[1] = volante[0]
carro_montado[2] = roda[0]


# Verificando se o carro montado está completo só com peças de qualidade mediana
if (carro_montado[0] is not None and carro_montado[1] is not None and carro_montado[2] is not None and
    'qualidade mediana' in carro_montado[0] and 'qualidade mediana' in carro_montado[1] and 'qualidade mediana' in carro_montado[2]):
    print('Pelo menos anda! Você consegue!')

# Verificando se o carro montado está completo com pelo menos uma peça de alta qualidade
if (carro_montado[0] is not None and carro_montado[1] is not None and carro_montado[2] is not None and
    ('alta qualidade' in carro_montado[0] or 'alta qualidade' in carro_montado[1] or 'alta qualidade' in carro_montado[2])):
    print('Conseguimos! Impossível você não ganhar essa corrida, Vanellope!')
    print(f'Para fazer o carro você utilizou {carro_montado[0].split(" - ")[0]} para ser a estrutura do carro, {carro_montado[1].split(" - ")[0]} para o volante, {carro_montado[2].split(" - ")[0]} para compor as rodas!')

# Carro diabético incompleto
if carro_montado[0] is None or carro_montado[1] is None or carro_montado[2] is None:
    print('Sinto muito, Vanellope. Não consegui te ajudar dessa vez.')

# Exibindo as peças descartadas
nomes = [doce.split(" - ")[0] for doce in descarte]
if descarte: 
    print('Alguns doces foram descartados. São eles:')
    print(', '.join(nomes))