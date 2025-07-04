# =============== ÁREA DE FUNÇÕES ===============
def atualizar_motivacao(motivacao_atual, vida_restante_vegeta, vida_inicial_oponente):
    # Atualizando a motivação
    nova_motivacao = motivacao_atual * (1 + (vida_restante_vegeta / vida_inicial_oponente))
    return nova_motivacao


def dano(tipo_de_golpe):
    # Analisando o tipo de golpe
    if tipo_de_golpe == 'Normal':
        return 20
    elif tipo_de_golpe == 'Potente':
        return 40


def turnos_e_batalhas(motivacao_inicial):
    print('A saga de Vegeta começa!')
    print()

    nome_oponentes = ['Piccolo', 'Gohan', 'Goku']
    hp_oponentes = [100, 100, 200]

    motivacao_vegeta = motivacao_inicial
    vegeta_vivo = True
    vitorias = 0

    # Loop de batalhas
    indice = 0
    while indice < len(nome_oponentes) and vegeta_vivo:
        oponente = nome_oponentes[indice]
        hp_oponente = hp_oponentes[indice]
        hp_vegeta = 100

        # Motivação do oponente
        motivacao_guerreiroZ = float(input())

        print(f'--- Iniciando o combate contra {oponente} ---')
        print()

        # Loop de turnos
        numero_do_turno = 1
        golpe_anterior_vegeta = ''

        while hp_vegeta > 0 and hp_oponente > 0 and vegeta_vivo:
            print(f'--- Turno {numero_do_turno} ---')

            # Vegeta ataca primeiro
            golpe_vegeta = input()
            if golpe_vegeta == 'Potente' and golpe_anterior_vegeta == 'Potente':
                print('Vegeta usou dois Golpes Potentes seguidos e desmaiou com o esforço!')
                vegeta_vivo = False
                hp_vegeta = 0
            else:
                dano_vegeta = int(dano(golpe_vegeta) * motivacao_vegeta)
                hp_oponente -= dano_vegeta

                if hp_oponente < 0:
                    hp_oponente = 0

                print(f'Vegeta usou Golpe {golpe_vegeta} e causou {dano_vegeta} de dano!')

                if hp_oponente > 0 and vegeta_vivo:
                    # Oponente vai atacar
                    golpe_do_oponente = input()
                    dano_do_oponente = int(dano(golpe_do_oponente) * motivacao_guerreiroZ)
                    hp_vegeta -= dano_do_oponente

                    if hp_vegeta < 0:
                        hp_vegeta = 0

                    print(f'{oponente} usou Golpe {golpe_do_oponente} e causou {dano_do_oponente} de dano!')

            # Status do turno
            print(f'|Vegeta: {hp_vegeta} HP vs {oponente}: {hp_oponente} HP|')
            print()

            numero_do_turno += 1
            golpe_anterior_vegeta = golpe_vegeta

        # Se Vegeta foi ou não derrotado
        if not vegeta_vivo or hp_vegeta <= 0:
            vegeta_vivo = False
            print(f'Vegeta foi derrotado! A Terra está a salvo graças a {oponente}!')
        else:
            print('Vitória de Vegeta!')
            print(f'Vegeta venceu a batalha contra {oponente} com {hp_vegeta} HP restantes!')
            hp_oponente_inicial = hp_oponentes[indice]
            motivacao_vegeta = atualizar_motivacao(motivacao_vegeta, hp_vegeta, hp_oponente_inicial)
            vitorias += 1
            print()

        indice += 1

    # Se teve 3 vitórias
    if vitorias == len(nome_oponentes) and vegeta_vivo:
        print('Vegeta derrotou todos os Guerreiros Z! A Terra foi conquistada!')


# =============== ÁREA DE CÓDIGO PRINCIPAL ==============
motivacao_inicial_vegeta = float(input())
turnos_e_batalhas(motivacao_inicial_vegeta)
