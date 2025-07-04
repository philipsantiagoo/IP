# =============== ÁREA DE FUNÇÕES ===============
def forca_jogador(tecnica1, tecnica2, tecnica3=None):
    if tecnica3 is None:
        poder1 = len(tecnica1) % 8
        poder2 = len(tecnica2) % 8
        return [poder1, poder2]
    else:
        poder1 = len(tecnica1) % 8
        poder2 = len(tecnica2) % 8
        poder3 = len(tecnica3) % 8
        return [poder1, poder2, poder3]


def terceiro_jogador():
    lutador3, tecnica3 = input().split(' - ')
    return lutador3, tecnica3


# =============== ÁREA DE CÓDIGO PRINCIPAL ===============
# Recebendo a quantidade de batalhas
qtd_batalhas = int(input())

# Mensagem inicial
print(f'O torneio do poder irá começar com {qtd_batalhas} batalhas no dia de hoje! Vamos ver quais universos vão conseguir se manter vivos até o final do dia!')

# Loop das batalhas
contador = 0
while contador < qtd_batalhas:
    # Inicializando tecnica3, lutador3 e aliado_do_terceiro para controle
    tecnica3 = None
    lutador3 = None
    aliado_do_terceiro = None

    # Recebendo, separadamente o nome do lutador e sua técnica
    lutador1, tecnica1 = input().split(' - ')
    lutador2, tecnica2 = input().split(' - ')

    # Verificando a ocorrência de terceiro lutador e definindo aliado
    if (lutador1 == 'Goku' and lutador2 == 'Jiren') or (lutador1 == 'Jiren' and lutador2 == 'Goku'):
        lutador3, tecnica3 = terceiro_jogador()
        aliado_do_terceiro = 'Goku'
        print(f'A intensidade dos dois lutadores motivou {lutador3} a entrar na batalha também!')

    elif (lutador1 == 'Frieza' and lutador2 == 'Jiren') or (lutador1 == 'Jiren' and lutador2 == 'Frieza'):
        lutador3, tecnica3 = terceiro_jogador()
        aliado_do_terceiro = 'Frieza'
        print(f'A intensidade dos dois lutadores motivou {lutador3} a entrar na batalha também!')

    elif (lutador1 == 'Gohan' and lutador2 == 'Namekuseijins') or (lutador1 == 'Namekuseijins' and lutador2 == 'Gohan'):
        lutador3, tecnica3 = terceiro_jogador()
        aliado_do_terceiro = 'Gohan'
        print(f'A intensidade dos dois lutadores motivou {lutador3} a entrar na batalha também!')

    elif (lutador1 == 'Androide 17' and lutador2 == 'Ribrianne') or (lutador1 == 'Ribrianne' and lutador2 == 'Androide 17'):
        lutador3, tecnica3 = terceiro_jogador()
        aliado_do_terceiro = 'Androide 17'
        print(f'A intensidade dos dois lutadores motivou {lutador3} a entrar na batalha também!')

    # Vendo o vencedor
    if tecnica3 is None:
        poderes = forca_jogador(tecnica1, tecnica2)
        poder1 = poderes[0]
        poder2 = poderes[1]

        if poder1 > poder2:
            vencedor = lutador1
            print(f'Incrível! {vencedor} mostrou sua força e defenderá seu universo até o final!')
        else:
            vencedor = lutador2
            print(f'Incrível! {vencedor} mostrou sua força e defenderá seu universo até o final!')

    else:
        poderes = forca_jogador(tecnica1, tecnica2, tecnica3)
        poder1 = poderes[0]
        poder2 = poderes[1]
        poder3 = poderes[2]

        lutadores = [lutador1, lutador2, lutador3]
        poderes = [poder1, poder2, poder3]

        indice_aliado = lutadores.index(aliado_do_terceiro)
        soma_aliado_terceiro = poderes[indice_aliado] + poderes[2]

        indices_adversarios = [0, 1]
        indices_adversarios.remove(indice_aliado)
        indice_adversario = indices_adversarios[0]

        poder_adversario = poderes[indice_adversario]

        if soma_aliado_terceiro > poder_adversario:
            vencedores = f"{aliado_do_terceiro} e {lutador3}"
        elif soma_aliado_terceiro < poder_adversario:
            vencedores = lutadores[indice_adversario]
        else:
            vencedores = f"{aliado_do_terceiro}, {lutadores[indice_adversario]} e {lutador3} (empate épico!)"

        print(f'Uma batalha brutal entre 3 lutadores! Os espectadores vão à loucura com essas amostras de {tecnica1}, {tecnica2} e {tecnica3}! A batalha acaba com {vencedores} no topo!')

    # Contador do while
    contador += 1
