pontos_atributo_ataque = 0
pontos_atributo_defesa = 0
contador = 0
erros = 0


print('------- Início do Treino -------')


qtd_de_bolas_rebatidas = int(input())

while contador < qtd_de_bolas_rebatidas:
    bola_lançada = str(input())
    golpe_executado = str(input())

    if bola_lançada == 'Ataque':
        if golpe_executado == 'Topspin':
            pontos_atributo_ataque += 5
            print(f'Você conseguiu rebater uma bola de {bola_lançada}! Golpe executado: {golpe_executado}.')
        elif golpe_executado == 'Smash':
            pontos_atributo_ataque += 10
            print(f'Você conseguiu rebater uma bola de {bola_lançada}! Golpe executado: {golpe_executado}.')
        elif golpe_executado == 'Errou':
            erros += 1
            print('Você errou! Levanta a cabeça que ainda tem mais.')
            pontos_atributo_ataque -= 10
    
    elif bola_lançada == 'Defesa':
        if golpe_executado == 'Chop':
            pontos_atributo_defesa += 10
            print(f'Você conseguiu rebater uma bola de {bola_lançada}! Golpe executado: {golpe_executado}.')
        elif golpe_executado == 'Push':
            pontos_atributo_defesa += 5
            print(f'Você conseguiu rebater uma bola de {bola_lançada}! Golpe executado: {golpe_executado}.')
        elif golpe_executado == 'Errou':
            erros += 1
            print('Você errou! Levanta a cabeça que ainda tem mais.')
            pontos_atributo_defesa -= 10
    
    contador += 1


if pontos_atributo_defesa < 0:
    pontos_atributo_defesa = 0
if pontos_atributo_ataque < 0:
    pontos_atributo_ataque = 0


if pontos_atributo_ataque > pontos_atributo_defesa:
    print('Ter um bom jogo ofensivo será fundamental para ganhar o InterCin!')
elif pontos_atributo_defesa > pontos_atributo_ataque:
    print('Defesa ganha campeonatos! Agora sim estou preparado.')
else:
    print('Foi um treino equilibrado.')

if erros >= 1:
    print('Infelizmente não foi um treino perfeito, mas pude melhorar muito.')

print('------- Atributos -------')
print('Ataque:', pontos_atributo_ataque)
print('Defesa:', pontos_atributo_defesa)
