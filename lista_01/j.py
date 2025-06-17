cidade_um = str(input())
adversario_um = str(input())
resultado_partida_um = str(input())

sequestro_ocorreu = False
expressao_matematica = ''


if resultado_partida_um == 'Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!':
    expressao_matematica = str(input())
    sequestro_ocorreu = True
else:
    cidade_dois = str(input())
    adversario_dois = str(input())
    resultado_partida_dois = str(input())

    if resultado_partida_dois == 'Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!':
        expressao_matematica = str(input())
        sequestro_ocorreu = True


print('Byte, o cachorro mais promissor do futebol nordestino, acaba de calçar suas quatro chuteiras e está pronto para entrar em campo!')


partidas_jogadas = 0
partidas_vitoriosas = 0
qtd_de_derrotas = 0
catende = False
tabira = False
s, p, o, r, t = 'sport'


if cidade_um == 'Catende':
    print('É... mesmo com o Santa embalado, jogar em Catende ou Tabira é pedir pra sofrer. Byte, meu filho, você realmente tá no fundo do poço.')
    catende = True

if cidade_um == 'Tabira':
    print('É... mesmo com o Santa embalado, jogar em Catende ou Tabira é pedir pra sofrer. Byte, meu filho, você realmente tá no fundo do poço.')
    tabira = True

if catende and tabira:
    print('Não dá mais! Jogar nessas duas cidades é sinal de que o Santa Cruz precisa mais de magia do que de reforços...')



if s in adversario_um and p in adversario_um and o in adversario_um and r in adversario_um and t in adversario_um:
    print('Alerta máximo! O adversário é o inimigo histórico, o Voldemort do futebol pernambucano... aquele cujo nome não deve ser pronunciado!')



if resultado_partida_um == 'VENCEU':
    print('TRI-COO-LOOOOR!!! Byte mostrou que tem faro de artilheiro e garantiu mais uma vitória do Santinha!')
    partidas_vitoriosas += 1
    partidas_jogadas += 1

elif resultado_partida_um == 'perdeu':
    print('Dessa vez não deu... Até o Galhardo canino tem seus dias de luta...')
    qtd_de_derrotas += 1
    partidas_jogadas += 1

elif resultado_partida_um == 'Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!':
    print('Urgente! Sequestradores estão tentando raptar nosso craque peludo! A única saída é resolver uma equação... Isso mesmo, agora isso aqui virou ENEM!')

    numero_1 = int(expressao_matematica[0])
    operador = (expressao_matematica[1])
    numero_2 = int(expressao_matematica[2])

    if operador == '+':
        resultado_expressao_matematica = (numero_1 + numero_2)
    elif operador == '-':
        resultado_expressao_matematica = (numero_1 - numero_2)
    elif operador == '*':
        resultado_expressao_matematica = (numero_1 * numero_2)
    elif operador == '/':
        resultado_expressao_matematica = (numero_1 / numero_2)
    
    print('A expressão resolvida é: {:.2f}'.format(resultado_expressao_matematica))
    print('Chega! Vou voltar pra casa e passar o resto das férias no sofá, assistindo o RobôCIn na RoboCup. Futebol de verdade, sem sequestro!')
    partidas_vitoriosas += 1
    partidas_jogadas += 1



if resultado_partida_um != 'Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!':
    if cidade_dois == 'Catende':
        print('É... mesmo com o Santa embalado, jogar em Catende ou Tabira é pedir pra sofrer. Byte, meu filho, você realmente tá no fundo do poço.')
        catende = True

    if cidade_dois == 'Tabira':
        print('É... mesmo com o Santa embalado, jogar em Catende ou Tabira é pedir pra sofrer. Byte, meu filho, você realmente tá no fundo do poço.')
        tabira = True

    if catende and tabira:
        print('Não dá mais! Jogar nessas duas cidades é sinal de que o Santa Cruz precisa mais de magia do que de reforços...')
    

    if s in adversario_dois and p in adversario_dois and o in adversario_dois and r in adversario_dois and t in adversario_dois:
        print('Alerta máximo! O adversário é o inimigo histórico, o Voldemort do futebol pernambucano... aquele cujo nome não deve ser pronunciado!')
    

    if resultado_partida_dois == 'VENCEU':
        print('TRI-COO-LOOOOR!!! Byte mostrou que tem faro de artilheiro e garantiu mais uma vitória do Santinha!')
        partidas_vitoriosas += 1
        partidas_jogadas += 1

    elif resultado_partida_dois == 'perdeu':
        print('Dessa vez não deu... Até o Galhardo canino tem seus dias de luta...')
        qtd_de_derrotas += 1
        partidas_jogadas += 1

    elif resultado_partida_dois == 'Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!':
        print('Urgente! Sequestradores estão tentando raptar nosso craque peludo! A única saída é resolver uma equação... Isso mesmo, agora isso aqui virou ENEM!')

        numero1 = int(expressao_matematica[0])
        operador = (expressao_matematica[1])
        numero2 = int(expressao_matematica[2])

        if operador == '+':
            resultado_expressao_matematica = (numero1 + numero2)
        elif operador == '-':
            resultado_expressao_matematica = (numero1 - numero2)
        elif operador == '*':
            resultado_expressao_matematica = (numero1 * numero2)
        elif operador == '/':
            resultado_expressao_matematica = (numero1 / numero2)

        print('A expressão resolvida é: {:.2f}'.format(resultado_expressao_matematica))
        print('Chega! Vou voltar pra casa e passar o resto das férias no sofá, assistindo o RobôCIn na RoboCup. Futebol de verdade, sem sequestro!')
        partidas_vitoriosas += 1
        partidas_jogadas += 1



print()
print('RELATÓRIO DA PRÉ-TEMPORADA DO BYTE:')
print('- Partidas jogadas:', partidas_jogadas)
print('- Vitórias:', partidas_vitoriosas)
print('- Derrotas:', qtd_de_derrotas)


if sequestro_ocorreu:
    print('- Tentaram roubar o bixinho: sim :(')
else:
    print('- Tentaram roubar o bixinho: Não!!!! :D')


print('- Cidades visitadas: ', end='')
print(cidade_um, end='')

if resultado_partida_um != 'Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!':
    print(' e', cidade_dois)
else:
    print()

print('- Adversários enfrentados: ', end='')
print(adversario_um, end='')

if resultado_partida_um != 'Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!':
    print(' e', adversario_dois)
else:
    print()

print()
print('E assim termina a pré-temporada do Byte pelos gramados. Anotar tudo isso na mão dá uma trabalheira! Nas próximas férias o Byte deve esperar saber laços, listas, funções e muito mais pra registrar tudo com mais facilidade :)')
