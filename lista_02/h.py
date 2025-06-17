print('A partida de revanche de Hugo Calderano contra a China, Potência Mundial do Tênis de Mesa, está prestes a começar!')

nacionalidade_atleta = input()
nome_atleta = input()

while nacionalidade_atleta != 'Chinês':
    print(f'O {nome_atleta} não poderá disputar a partida, pois sua nacionalidade não é chinesa!')
    nacionalidade_atleta = input()
    nome_atleta = input()

print(f'{nome_atleta} foi convocado para vingar o massacre feito durante o mundial de Tênis de Mesa!')


pontos_hugo = 0
pontos_china = 0
continuar = True

while continuar:
    numero_adversario = int(input())
    numero_hugo = int(input())

    if numero_adversario == numero_hugo:
        pontos_hugo += 1
        print('A bola bateu na rede e felizmente caiu no lado adversário!!! Hugo marca mais um ponto!')
    elif numero_adversario >= numero_hugo * 2:
        pontos_china += 2
        print('Que bela jogada, essa merece ponto extra!')
    elif numero_hugo >= numero_adversario * 2:
        pontos_hugo += 2
        print('Que bela jogada, essa merece ponto extra!')
    elif numero_adversario > numero_hugo:
        pontos_china += 1
        print('Vamos Hugo, não deixe ele vencer!')
    else:
        pontos_hugo += 1
        print('Hugo Calderano marcou um ponto de maneira esplendida!')

    if abs(pontos_hugo - pontos_china) >= 3:
        continuar = False


if pontos_hugo < 3:
    print('A China vence esta partida!')
elif pontos_hugo == 3:
  print('Hugo Calderano mostrou o porquê ele é o atual campeão mundial, uma partida relâmpago!')
elif 3 < pontos_hugo < 10:
    print('Não demorou muito, mas o resultado era esperado, Hugo Calderano vence!')
elif pontos_hugo > 10:
    print('Demorou, mas o previsto aconteceu! Hugo Calderano não deixa dúvidas do porquê ele é o Campeão Mundial!')


print(f'Placar Final: {pontos_hugo}x{pontos_china}')
print()
print('Aqui está o merecido prêmio de Hugo Calderano:')


largura = pontos_hugo
comprimento = pontos_china

if comprimento <= 2:
    comprimento = 3
elif comprimento % 2 == 0:
    comprimento -= 1

if comprimento < 3:
    comprimento = 3

for c in range(1, largura + 1):
    print('-', end='')
print()


linha_interna = comprimento - 2
meio_trofeu = linha_interna // 2
contador = 0

while contador < linha_interna:
    print('|', end='')
    if contador == meio_trofeu:
        for i in range(largura - 2):
            print('#', end='')
    else:
        for i in range(largura - 2):
            print(' ', end='')
    print('|')
    contador += 1


for c in range(1, largura + 1):
    print('-', end='')
print()