# ========== ÁREA DE FUNÇÕES ==========
def batalha_de_turnos(vitalidade_sekiro, postura_sekiro, postura_maxima_sekiro, cabacas_curativas_sekiro,
                      vitalidade_genichiro, postura_genichiro, postura_maxima_genichiro, i):

    if vitalidade_sekiro <= 0:
        print('Sekiro cai de joelhos, derrotado...')
        print('====================================')
        print('Vitória de Genichiro: Morte.')
        return
    elif postura_sekiro >= postura_maxima_sekiro:
        print('A postura do lobo foi quebrada! Ele não consegue se defender e é derrotado!')
        print('====================================')
        print('Vitória de Genichiro: Morte.')
        return

    print(f'--- Turno {i} ---') 
    if postura_genichiro >= postura_maxima_genichiro or vitalidade_genichiro <= 0:
        print('Genichiro está de joelhos e vulnerável! Acabe com isso, Lobo!')

        if postura_genichiro >= postura_maxima_genichiro:
            motivo_vulnerabilidade = 'postura'
        else:
            motivo_vulnerabilidade = 'vitalidade'

        acao_sekiro = input()
        while acao_sekiro not in ['ataque', 'hesitar']:
            print('O lobo não adquiriu esse movimento ainda.')
            acao_sekiro = input()

        if acao_sekiro == 'ataque':
            print('Sekiro executa um Golpe Mortal em Genichiro!')
            print('====================================')
            print('Vitória de Sekiro: Golpe Mortal!')
            return
        elif acao_sekiro == 'hesitar':
            print('O lobo hesitou no seu golpe final, Genichiro recupera sua postura! Cuidado, Lobo!')
            if motivo_vulnerabilidade == 'postura':
                postura_genichiro += 50
                if vitalidade_genichiro < 50:
                    vitalidade_genichiro = 50
            else:
                vitalidade_genichiro += 50
                postura_genichiro = 50
            return batalha_de_turnos(vitalidade_sekiro, postura_sekiro, postura_maxima_sekiro, cabacas_curativas_sekiro, vitalidade_genichiro, postura_genichiro, postura_maxima_genichiro, i + 1)

    acoes_Sekiro = ['ataque', 'defesa', 'defesa perfeita', 'usar cabaça', 'desviar', 'contra ataque mikiri']
    acoes_Genichiro = ['ataque', 'defesa', 'recuperação de postura', 'ataque kanji']

    acao_genichiro = input()
    while acao_genichiro not in acoes_Genichiro:
        print('Genichiro não tem esse movimento em seu arsenal.')
        acao_genichiro = input()

    acao_sekiro = input()
    while acao_sekiro not in acoes_Sekiro:
        print('O lobo não adquiriu esse movimento ainda.')
        acao_sekiro = input()


    if acao_genichiro == 'ataque':

        if acao_sekiro == 'ataque':
            print('Clima de tensão! Os dois atacam numa luta implacável!')
            vitalidade_sekiro -= 25
            vitalidade_genichiro -= 10
            postura_genichiro += 15

        elif acao_sekiro == 'defesa':
            print('Sekiro firma sua espada e se defende, absorvendo o impacto em sua postura!')
            vitalidade_sekiro -= 10
            postura_sekiro += 20

        elif acao_sekiro == 'defesa perfeita':
            print('Lâminas se encontram! Um desvio perfeito de Sekiro desequilibra Genichiro!')
            postura_genichiro += 25

        elif acao_sekiro == 'usar cabaça':
            if cabacas_curativas_sekiro > 0:
                print('Sekiro tenta curar, mas é punido pelo ataque impiedoso de Genichiro!')
                cabacas_curativas_sekiro -= 1
                vitalidade_sekiro -= 25
            else:
                print('Sekiro busca sua cabaça, mas ela está vazia!')
                print('Enquanto Sekiro se distrai, Genichiro avança com um ataque certeiro!')
                vitalidade_sekiro -= 25

        elif acao_sekiro == 'desviar':
            print('O lobo desvia agilmente do ataque comum de Genichiro!')

        else:
            print('O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro faz um movimento comum.')
            postura_genichiro += 10


    elif acao_genichiro == 'defesa':

        if acao_sekiro == 'ataque':
            print('Genichiro prevê o movimento e apara o golpe de Sekiro com sua lâmina!')
            postura_genichiro += 5

        elif acao_sekiro == 'defesa':
            print('Os guerreiros se encaram, medindo um ao outro. Nenhum avanço.')

        elif acao_sekiro == 'defesa perfeita':
            print('Sekiro se prepara para o desvio, mas Genichiro permanece na defensiva.')

        elif acao_sekiro == 'usar cabaça':
            if cabacas_curativas_sekiro > 0:
                print('Genichiro hesita! Sekiro aproveita a brecha para usar sua Cabaça Curativa.')
                vitalidade_sekiro += 25
                cabacas_curativas_sekiro -= 1
            else:
                print('Sekiro busca sua cabaça, mas ela está vazia!')
                print('Genichiro mantém a guarda, enquanto o lobo percebe seu erro.')

        elif acao_sekiro == 'desviar':
            print('O lobo tenta prever um possível ataque de Genichiro desviando antecipadamente, mas ele não faz nada.')

        else:
            print('O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro não realizou nenhum movimento de ataque.')


    elif acao_genichiro == 'recuperação de postura':

        if acao_sekiro == 'ataque':
            print('Genichiro ia recuperar sua postura mas o lobo foi mais rápido, um grande ataque por parte do lobo!')
            vitalidade_genichiro -= 10
            postura_genichiro += 15

        elif acao_sekiro == 'defesa':
            print('Os guerreiros se encaram, medindo um ao outro. Nenhum avanço.')
            print('Genichiro consegue recuperar sua postura, cuidado lobo!')
            postura_genichiro = 0

        elif acao_sekiro == 'defesa perfeita':
            print('Sekiro se prepara para o desvio, mas Genichiro permanece na defensiva.')
            print('Genichiro consegue recuperar sua postura, cuidado lobo!')
            postura_genichiro = 0

        elif acao_sekiro == 'usar cabaça':
            if cabacas_curativas_sekiro > 0:
                print('Genichiro hesita! Sekiro aproveita a brecha para usar sua Cabaça Curativa.')
                print('Genichiro consegue recuperar sua postura, cuidado lobo!')
                vitalidade_sekiro += 25
                cabacas_curativas_sekiro -= 1
                postura_genichiro = 0
            else:
                print('Sekiro busca sua cabaça, mas ela está vazia!')
                print('Genichiro aproveita a hesitação do lobo para recuperar sua postura.')
                print('Genichiro consegue recuperar sua postura, cuidado lobo!')
                postura_genichiro = 0

        elif acao_sekiro == 'desviar':
            print('O lobo tenta prever um possível ataque de Genichiro desviando antecipadamente, mas ele não faz nada.')
            print('Genichiro consegue recuperar sua postura, cuidado lobo!')
            postura_genichiro = 0

        else:
            print('O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro não realizou nenhum movimento de ataque.')
            print('Genichiro consegue recuperar sua postura, cuidado lobo!')
            postura_genichiro = 0


    else:
        
        if acao_sekiro == 'contra ataque mikiri':
            print('O lobo utiliza a técnica de contra ataque mikiri e pisa na arma de Genichiro!')
            postura_genichiro += 25

        elif acao_sekiro == 'desviar':
            print('O lobo desvia do ataque especial de Genichiro com muita agilidade!')

        elif acao_sekiro == 'usar cabaça':
            print('O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!')
            if cabacas_curativas_sekiro > 0:
                cabacas_curativas_sekiro -= 1
                vitalidade_sekiro -= 50
                postura_sekiro += 20
            else:
                print('Para piorar, Sekiro nem sequer tinha uma cabaça para usar!')
                vitalidade_sekiro -= 50
                postura_sekiro += 20

        else:
            print('O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!')
            vitalidade_sekiro -= 50
            postura_sekiro += 20

    batalha_de_turnos(vitalidade_sekiro, postura_sekiro, postura_maxima_sekiro, cabacas_curativas_sekiro,
                      vitalidade_genichiro, postura_genichiro, postura_maxima_genichiro, i + 1)


# ========== ÁREA DE CÓDIGO PRINCIPAL ==========
print('O duelo começa! Suas decisões determinarão o vencedor.')

vitalidade_sekiro = 100
postura_sekiro = 0
postura_maxima_sekiro = 100
cabacas_curativas_sekiro = 2

vitalidade_genichiro = 100
postura_genichiro = 0
postura_maxima_genichiro = 100

batalha_de_turnos(vitalidade_sekiro, postura_sekiro, postura_maxima_sekiro, cabacas_curativas_sekiro,
                  vitalidade_genichiro, postura_genichiro, postura_maxima_genichiro, 1)
