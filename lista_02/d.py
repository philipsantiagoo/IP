F_max = int(input())
forca_inicial = int(input())
nivel = str(input())
forca_media_jogador = int(input())

print('Robô Hugo 4.0 foi inicializado…')

incremento = 0
tempo = 1
contador = 1
forca_acumulada = 0

tempo_partida = 0
contador_rebatidas = 0


if nivel == 'facil':
    print('Iniciando no modo iniciante... Ótimo para aquecer os motores!')
    incremento += 1
elif nivel == 'medio':
    print('Você escolheu o modo intermediário. Hora de mostrar técnica e estratégia!')
    incremento += 3
elif nivel == 'dificil':
    print('Modo lendário ativado! Hugo 4.0 está a todo vapor — prepare-se para o combate definitivo!')
    incremento += 5


continuar = True

while continuar:
    F_rebatida = forca_inicial + (tempo * incremento)

    tempo_partida += 1
    contador_rebatidas += 1

    if F_rebatida > 150:
        print('Bola fora! A força da rebatida excedeu os limites da mesa.')
        continuar = False
    else:
        forca_acumulada += F_rebatida

        print(f'Rebatida {contador}: força = {F_rebatida}, força acumulada = {forca_acumulada}')

        tempo += 1
        contador += 1
        
        if forca_acumulada > F_max:
            print('Energia do robô esgotada! Encerrando o confronto…')
            continuar = False
        


print('Partida finalizada! Estas são as estatísticas do embate:')

print(f'O robô realizou {contador_rebatidas} rebatidas em {tempo_partida} segundos, com força total de {forca_acumulada}.')

if tempo_partida > 0:
    Forca_media_robo = forca_acumulada // tempo_partida 
    print(f'Força média do robô: {Forca_media_robo}')
    print(f'Força média do jogador: {forca_media_jogador}')

    if Forca_media_robo > forca_media_jogador:
        print('Vitória do Hugo 4.0! O robô mostrou quem manda na quadra!')
    elif Forca_media_robo < forca_media_jogador:
        print('Vitória do jogador! O talento humano ainda é imbatível!')
    else:
        print('Empate técnico! Um duelo digno de mestres do tênis de mesa.')
        