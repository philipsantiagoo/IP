# ========== ÁREA DE FUNÇÕES ==========
def simulando_as_batalhas(qtd_tentativas, experiencia_do_jogador, vida_inicial_jogador, dps_inicial_jogador,
                          nome_do_mandachuva, vida_do_mandachuva, dps_mandachuva,
                          vida_atual_do_jogador=None, vida_atual_do_mandachuva=None, sif_ferida=False):

    # Inicializa vida atual na primeira chamada
    if vida_atual_do_jogador == None:
        vida_atual_do_jogador = vida_inicial_jogador
    if vida_atual_do_mandachuva == None:
        vida_atual_do_mandachuva = vida_do_mandachuva

    # Simulando a batalha - um turno recursivo
    if vida_atual_do_jogador > 0 and vida_atual_do_mandachuva > 0:

        vida_atual_do_mandachuva -= dps_inicial_jogador

        if nome_do_mandachuva == 'Sif, a Grande Loba Cinzenta' and vida_atual_do_mandachuva < 3432 * 0.10:
            if not sif_ferida:
                dps_mandachuva -= 15
                print('Sif, a Grande Loba Cinzenta está gravemente ferida! Essa é sua chance, acabe com o sofrimento dela!')
                sif_ferida = True

        elif nome_do_mandachuva == 'Gwyn, Lorde das Cinzas' and vida_atual_do_mandachuva < 4185 * 0.5:
            vida_atual_do_jogador -= 10

        if vida_atual_do_mandachuva <= 0:
            # Vitória
            if nome_do_mandachuva == 'Sif, a Grande Loba Cinzenta':
                print(f'Você precisou de {qtd_tentativas} tentativas para vencer o(a) {nome_do_mandachuva}!')

                if experiencia_do_jogador == 'Iniciante':
                    if qtd_tentativas <= 5:
                        print('Esse iniciante teve muita sorte, no próximo boss ele vai conhecer a verdadeira DOR!!!')
                    elif 5 <= qtd_tentativas <= 10:
                        print('Até que não foi tão ruim assim, continue assim novato!')
                    else:
                        print('Bem vindo a Dark Souls.')
                elif experiencia_do_jogador == 'Veterano':
                    if qtd_tentativas <= 5:
                        print('Você já andou por Lordran antes, não é? Impressionante.')
                    elif 5 <= qtd_tentativas <= 10:
                        print('Nada mal, guerreiro. Mas os próximos desafios não terão piedade.')
                    else:
                        print('Mesmo os veteranos sangram em Dark Souls...')
                else:
                    if qtd_tentativas == 1:
                        print('Inacreditável. Um verdadeiro Mestre do Souls. Está destinado a se tornar o Dark Lord!')
                    elif 1 <= qtd_tentativas <= 10:
                        print('Seu conhecimento sobre o ciclo é profundo. Quase como se já tivesse vivido isso mil vezes...')
                    else:
                        print('Nem mesmo os Mestres escapam ilesos da chama...')

                print('A grande loba cai com honra. No fundo dos seus olhos, havia apenas lealdade.')

            elif nome_do_mandachuva == 'Gwyn, Lorde das Cinzas':
                print(f'Você precisou de {qtd_tentativas} tentativas para vencer o(a) {nome_do_mandachuva}!')

                if experiencia_do_jogador == 'Iniciante':
                    if qtd_tentativas <= 5:
                        print('Esse iniciante teve muita sorte, no próximo boss ele vai conhecer a verdadeira DOR!!!')
                    elif 5 <= qtd_tentativas <= 10:
                        print('Até que não foi tão ruim assim, continue assim novato!')
                    else:
                        print('Bem vindo a Dark Souls.')
                elif experiencia_do_jogador == 'Veterano':
                    if qtd_tentativas <= 5:
                        print('Você já andou por Lordran antes, não é? Impressionante.')
                    elif 5 <= qtd_tentativas <= 10:
                        print('Nada mal, guerreiro. Mas os próximos desafios não terão piedade.')
                    else:
                        print('Mesmo os veteranos sangram em Dark Souls...')
                else:
                    if qtd_tentativas == 1:
                        print('Inacreditável. Um verdadeiro Mestre do Souls. Está destinado a se tornar o Dark Lord!')
                    elif 1 <= qtd_tentativas <= 10:
                        print('Seu conhecimento sobre o ciclo é profundo. Quase como se já tivesse vivido isso mil vezes...')
                    else:
                        print('Nem mesmo os Mestres escapam ilesos da chama...')

                print('A chama se apaga, e o silêncio reina em Lordran. Você derrotou o Senhor das Cinzas...')
                if qtd_tentativas == 1:
                    print('O ciclo foi quebrado... Você se tornou o verdadeiro Senhor das Cinzas. Um novo destino começa...')
                else:
                    print('Mas o ciclo... o ciclo continua.')
            return

        vida_atual_do_jogador -= dps_mandachuva

        # Próximo turno recursivamente, passando o estado atualizado
        simulando_as_batalhas(qtd_tentativas, experiencia_do_jogador, vida_inicial_jogador, dps_inicial_jogador,
                              nome_do_mandachuva, vida_do_mandachuva, dps_mandachuva,
                              vida_atual_do_jogador, vida_atual_do_mandachuva, sif_ferida)

    else:
        # Caso o jogador morreu, inicia nova tentativa com bônus
        qtd_tentativas += 1

        if experiencia_do_jogador == 'Iniciante':
            novo_dps_jogador = dps_inicial_jogador * 1.05
            novo_dps_mandachuva = dps_mandachuva * 0.90
        elif experiencia_do_jogador == 'Veterano':
            novo_dps_jogador = dps_inicial_jogador * 1.1
            novo_dps_mandachuva = dps_mandachuva * 0.80
        else:
            novo_dps_jogador = dps_inicial_jogador * 1.20
            novo_dps_mandachuva = dps_mandachuva * 0.67

        simulando_as_batalhas(qtd_tentativas, experiencia_do_jogador, vida_inicial_jogador, novo_dps_jogador,
                              nome_do_mandachuva, vida_do_mandachuva, novo_dps_mandachuva)



# ========== ÁREA DE CÓDIGO PRINCIPAL ==========

# Recebendo a experiência do jogador
experiencia_do_jogador = input()

# Recebendo as estatísticas do jogador
vitalidade_forca = input().split(' ')

# Recebendo o nome do chefe que será enfrentado
nome_do_mandachuva = input()

# Analisando a vida inicial do jogador
vida_inicial_jogador = int(vitalidade_forca[0]) * 20

# Analisando o DPS inicial do jogador
dps_inicial_jogador = int(vitalidade_forca[1]) * 5



# Mensagem inicial
if nome_do_mandachuva == 'Sif, a Grande Loba Cinzenta':
    print('Venha até mim guardiã do túmulo de Artorias... Vamos acabar logo com isso!')
    vida_do_mandachuva = 3432
    dps_mandachuva = 35
elif nome_do_mandachuva == 'Gwyn, Lorde das Cinzas':
    print('Enfim estou de frente ao Senhor das Cinzas! Nossa batalha será lendária e ecoará em todos os cantos de Lordran!!!')
    vida_do_mandachuva = 4185
    dps_mandachuva = 55



qtd_tentativas = 1  
simulando_as_batalhas(qtd_tentativas, experiencia_do_jogador, vida_inicial_jogador, dps_inicial_jogador,
                      nome_do_mandachuva, vida_do_mandachuva, dps_mandachuva)
