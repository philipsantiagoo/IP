print('Bem amigos da Rede Globo, emoção no ar! Prepare o coração porque hoje é dia de decisão! É final de Copa do Mundo, mas não é futebol… é ping pong, meu amigo! A raquete vai cantar, a bolinha vai voar, e só um será campeão! Segura essa emoção porque vai começar!')

sacador_1 = input()  # Quem saca o primeiro set (e o primeiro ponto do 5º set)
sacador_atual = sacador_1

sets_hugo = 0
sets_lin = 0
set_n = 1

while sets_hugo < 3 and sets_lin < 3:
    print(f'Set {set_n}:')

    pontos_hugo = 0
    pontos_lin = 0
    vantangem_de_set = False

    limite_pontos_set = 5
    limite_para_vantangem_de_set = 4

    if set_n == 5:
        limite_pontos_set = 7
        limite_para_vantangem_de_set = 6

        print('Agora é hora da decisão! Vamos para o tie-break, quem errar, perde tudo! É emoção até o fim!')

    set_acabou = False
    while not set_acabou:
        quem_saca_o_ponto = ""

        if set_n == 5:
            pontos_jogados_no_set_atual = pontos_hugo + pontos_lin
            if pontos_jogados_no_set_atual == 0:
                quem_saca_o_ponto = sacador_1
            else:
                primeiro_sacador = sacador_1
                oponente = 'lin' if primeiro_sacador == 'hugo' else 'hugo'
                numero_de_trocas = (pontos_jogados_no_set_atual - 1) // 2
                if numero_de_trocas % 2 == 0:
                    quem_saca_o_ponto = oponente
                else:
                    quem_saca_o_ponto = primeiro_sacador

        else:
            quem_saca_o_ponto = sacador_atual

        sacador_do_ponto = quem_saca_o_ponto

        if not vantangem_de_set:
            if pontos_hugo == limite_para_vantangem_de_set and pontos_lin == limite_para_vantangem_de_set:
                if set_n == 5:

                    print('O tie-break está pegando fogo e agora vai a 2! Quem fizer dois pontos seguidos leva, é a reta final da disputa! Quem será o grande campeão?')
                else:

                    print('O set está pegando fogo e agora vai a 2! Quem fizer dois pontos seguidos leva — é decisão na mesa!')
                vantangem_de_set = True

        jogada_str = input()

        acao_atual_str = ''
        jogador_da_acao = quem_saca_o_ponto
        acao_anterior_do_oponente = 'inicio_ponto'
        ponto_foi_definido = False

        for char_atual in jogada_str:

            if ponto_foi_definido:
                acao_atual_str = ''
            elif char_atual != '-':
                acao_atual_str += char_atual
            else:
                acao_finalizada = acao_atual_str
                acao_atual_str = ''
                oponente_do_jogador_da_acao = 'lin' if jogador_da_acao == 'hugo' else 'hugo'
                vencedor_ponto = ''

                if acao_anterior_do_oponente == 'saque':
                    if acao_finalizada == 'erro' or acao_finalizada == 'ataque':
                        print(f'Uau, um ace! {sacador_do_ponto.capitalize()} solta o braço e deixa o adversário parado!')
                        vencedor_ponto = sacador_do_ponto
                        ponto_foi_definido = True

                elif acao_finalizada == 'erro':
                    print(f'{jogador_da_acao.capitalize()} se estica, tenta a defesa, mas não alcança — ponto para o adversário.')
                    vencedor_ponto = oponente_do_jogador_da_acao
                    ponto_foi_definido = True

                elif acao_anterior_do_oponente == 'ataque':
                    if acao_finalizada != 'defesa':
                        print(f'{oponente_do_jogador_da_acao.capitalize()} acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!')
                        vencedor_ponto = oponente_do_jogador_da_acao
                        ponto_foi_definido = True
                        
                elif acao_anterior_do_oponente == 'defesa':
                    if acao_finalizada == 'defesa':
                        print(f'{jogador_da_acao.capitalize()} tentou devolver uma bola de defesa, o que não é permitido — ponto para o adversário.')
                        vencedor_ponto = oponente_do_jogador_da_acao
                        ponto_foi_definido = True

                if not ponto_foi_definido:
                    acao_anterior_do_oponente = acao_finalizada
                    jogador_da_acao = oponente_do_jogador_da_acao

        if not ponto_foi_definido and acao_atual_str != '':
            acao_finalizada = acao_atual_str
            oponente_do_jogador_da_acao = 'lin' if jogador_da_acao == 'hugo' else 'hugo'
            vencedor_ponto = ''

            if acao_anterior_do_oponente == 'saque':
                if acao_finalizada == 'erro' or acao_finalizada == 'ataque':
                    print(f'Uau, um ace! {sacador_do_ponto.capitalize()} solta o braço e deixa o adversário parado!')
                    vencedor_ponto = sacador_do_ponto
            elif acao_finalizada == 'erro':
                print(f'{jogador_da_acao.capitalize()} se estica, tenta a defesa, mas não alcança — ponto para o adversário.')
                vencedor_ponto = oponente_do_jogador_da_acao
            elif acao_anterior_do_oponente == 'ataque':
                if acao_finalizada != 'defesa':
                    print(f'{oponente_do_jogador_da_acao.capitalize()} acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!')
                    vencedor_ponto = oponente_do_jogador_da_acao
            elif acao_anterior_do_oponente == 'defesa':
                if acao_finalizada == 'defesa':
                    print(f'{jogador_da_acao.capitalize()} tentou devolver uma bola de defesa, o que não é permitido — ponto para o adversário.')
                    vencedor_ponto = oponente_do_jogador_da_acao

            if vencedor_ponto != '':
                ponto_foi_definido = True
            else:
                acao_anterior_do_oponente = acao_finalizada
                jogador_da_acao = oponente_do_jogador_da_acao

        if vencedor_ponto == 'hugo':
            pontos_hugo += 1
            print('Ponto para Hugo!')
        elif vencedor_ponto == 'lin':
            pontos_lin += 1
            print('Ponto para Lin!')

        print(f'Placar do {set_n} set : {pontos_hugo} x {pontos_lin}')

        ganhou_por_limite_normal = (pontos_hugo >= limite_pontos_set or pontos_lin >= limite_pontos_set)
        tem_diferenca_de_dois = abs(pontos_hugo - pontos_lin) >= 2

        if vantangem_de_set:
            if ganhou_por_limite_normal and tem_diferenca_de_dois:
                set_acabou = True
        else:
            if ganhou_por_limite_normal:
                set_acabou = True
                if not tem_diferenca_de_dois and (pontos_hugo == limite_pontos_set or pontos_lin == limite_pontos_set):
                    set_acabou = False
                    if pontos_hugo == limite_pontos_set and pontos_lin == limite_pontos_set:
                        set_acabou = False

    vencedor_do_set = ''
    if pontos_hugo > pontos_lin:
        vencedor_do_set = 'hugo'
        sets_hugo += 1
    else:
        vencedor_do_set = 'lin'
        sets_lin += 1

    if set_n == 5:
        if (pontos_hugo == limite_pontos_set and pontos_lin == 0) or \
           (pontos_lin == limite_pontos_set and pontos_hugo == 0):
            print(f'Fim de tie-break! {vencedor_do_set.capitalize()} arrasa com um {limite_pontos_set} a 0 impressionante, sem dar chances para o adversário! Vitória esmagadora!')
        else:
            print(f'E o set vai para {vencedor_do_set.capitalize()}!')
    else:
        if (pontos_hugo == limite_pontos_set and pontos_lin == 0) or \
           (pontos_lin == limite_pontos_set and pontos_hugo == 0):
            print(f'Fim de set! Domínio total: {limite_pontos_set} a 0, sem chance para o adversário — {vencedor_do_set.capitalize()} passeia na mesa')
        else:
            print(f'E o set vai para {vencedor_do_set.capitalize()}!')

    print(f'Placar do jogo: {sets_hugo} x {sets_lin}')

    set_n += 1
    if sets_hugo < 3 and sets_lin < 3:
        if set_n <= 4:
            sacador_atual = 'lin' if sacador_atual == 'hugo' else 'hugo'

if sets_hugo == 3:
    if set_n - 1 == 5:
        print('Hugo é o grande vencedor! Ele conquista o tie-break com uma performance impecável e leva a vitória!')
    else:
        print('Hugo garantiu a vitória sem precisar de tie-break! Uma performance sólida e sem erros, ele dominou o jogo do início ao fim e se sagrou campeão do mundo!')
elif sets_lin == 3:
    if set_n - 1 == 5:
        print('Hugo lutou até o fim, mas no tie-break, o adversário levou a melhor. Uma derrota apertada, mas ainda assim, uma grande batalha!')
    else:
        print('Hugo não conseguiu segurar a pressão e acabou perdendo sem precisar do tie-break. Foi uma grande final, mas hoje não foi o seu dia. Vitória do chinês!')