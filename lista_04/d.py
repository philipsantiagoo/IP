# =============== ÁREA DAS FUNÇÕES ===============
def primeira_string(nome1, refazer1=0, refazer2=0):
    tamanho_string1 = len(nome1)

    # Verificando se a string 1 tem 4 ou menos caracteres
    if tamanho_string1 <= 4:
        # Se for refazer uma primeira vez, usa os dois primeiros caracteres
        if refazer1 == 1:
            return [nome1[:2]]
        else:
            return [nome1[0]]

    # Verificando se é maior que 4
    elif tamanho_string1 > 4:
        # Divide
        resultado_div = tamanho_string1 / 2

        # Se o resultado não for inteiro, arredonda pra cima
        if resultado_div != int(resultado_div):
            caracteres = int(resultado_div) + 1
        else:
            caracteres = int(resultado_div)

        # Se for refazer1 **e não for** refazer2 (última tentativa), adiciona +1
        if refazer1 == 1 and refazer2 == 0:
            caracteres += 1

        # Retorna os primeiros n caracteres da string
        return [nome1[:caracteres]]


def segunda_string(nome2, refazer2=0):
    tamanho_string2 = len(nome2)

    # Verificando se houve refazer2
    if refazer2 == 1:
        if tamanho_string2 <= 4:
            return [nome2[-3:]]
        else:
            resultado_div = tamanho_string2 / 2
            caracteres = int(resultado_div) if resultado_div == int(resultado_div) else int(resultado_div) + 1
            return [nome2[-caracteres:]]

    # Se não tem refazer2
    if tamanho_string2 == 3:
        return [nome2[-2:]]
    # Verificando se a string 2 tem 4 ou menos caracteres
    elif tamanho_string2 <= 4:
        return [nome2[-3:]]
    else:
        # Verifica se for maior que 4 caracteres
        resultado_div = tamanho_string2 / 2
        # Se o resultado não for inteiro, arredonda pra cima
        caracteres = int(resultado_div) if resultado_div == int(resultado_div) else int(resultado_div) + 1
        # Reduz 1 conforme a regra
        caracteres -= 1
        return [nome2[-caracteres:]]


def fusaoZ(nome1, nome2, refazer1=0, refazer2=0):
    # Observação: faça o favor a nós dois (eu e você) e leia com a entonação certa
    # Se precisa refazer uma vez
    if refazer1 == 1:
        parte_nome1 = primeira_string(nome1, refazer1=1, refazer2=refazer2)[0]
    else:
        parte_nome1 = primeira_string(nome1, refazer1=0)[0]

    parte_nome2 = segunda_string(nome2, refazer2=refazer2)[0]
    # Preparara... A hora é agora!! fuuuuSÃO
    fuuuuSAO = parte_nome1 + parte_nome2
    fuuuuSAO = fuuuuSAO.capitalize()
    return [parte_nome1, parte_nome2, fuuuuSAO]


def avaliando_fusaoZ(parte_nome1, parte_nome2, fusao):
    if len(fusao) <= 3:
        return 'Fusão imperfeita'

    ultima1 = parte_nome1[-1].lower()
    primeira2 = parte_nome2[0].lower()
    vogais = 'aeiou'

    if (ultima1 in vogais and primeira2 in vogais) or (ultima1 not in vogais and primeira2 not in vogais):
        return 'Fusão imperfeita'

    return 'Fusão perfeita'


def tipo_personagem(nome):
    if nome in herois:
        return 'heroi'
    else:
        return 'vilao'


def incremento_de_poder(nome_fusao):
    tamanho = len(nome_fusao)
    if tamanho == 4:
        return 2000
    elif tamanho == 5:
        return 2250
    elif tamanho == 6:
        return 2500
    elif tamanho == 7:
        return 2750
    else:
        return 3000


def registrar_fusao(tipo1, tipo2, nome1, nome2, fusao):
    # Bloquinho chato que se repetiu 3 vezes
    if tipo1 == 'heroi' and tipo2 == 'heroi':
        print(f'Fusão realizada com sucesso! {fusao} entra em combate para derrotar o exército de vilões!')
        herois_fundidos.append(nome1)
        herois_fundidos.append(nome2)
        return incremento_de_poder(fusao)
    elif tipo1 == 'vilao' and tipo2 == 'vilao':
        print(f'Fusão realizada com sucesso! {fusao} entra em combate com sede de destruir Satan City!')
        viloes_fundidos.append(nome1)
        viloes_fundidos.append(nome2)
        return incremento_de_poder(fusao)
    return 0


# =============== ÁREA DE CÓDIGO PRINCIPAL ===============
herois = [
    'Gohan',
    'Goku',
    'Goten',
    'Kuririn',
    'Piccolo',
    'Tenshinhan',
    'Trunks',
    'Uub',
    'Vegeta',
    'Yamcha'
]

viloes = [
    'Babidi',
    'Baby',
    'Broly',
    'Buu',
    'Cell',
    'Cooler',
    'Frieza',
    'Hit',
    'Janemba',
    'Zamasu'
]

herois_fundidos = []
viloes_fundidos = []

poder_herois = 0
poder_viloes = 0

# Flag de vencedor
vencedor = False

# Loop
while not vencedor:
    # Recebendo os nomes tlgd
    nome1 = input()
    print(f'{nome1} se elege para participar da fusão!')

    nome2 = input()
    print(f'{nome2} se elege para participar da fusão!')

    # ======= VERIFICAÇÕES DE REGRA =======
    # Vendo se alguém que já fez fusão tá tentando entrar em outra
    participou_nome1 = nome1 in herois_fundidos or nome1 in viloes_fundidos
    participou_nome2 = nome2 in herois_fundidos or nome2 in viloes_fundidos

    if participou_nome1 or participou_nome2:
        if participou_nome1:
            print(f'{nome1} já participou de uma fusão. Fusão inválida.')
        if participou_nome2:
            print(f'{nome2} já participou de uma fusão. Fusão inválida.')
    elif (nome1 in herois and nome2 in viloes) or (nome1 in viloes and nome2 in herois):
        print('Heróis e vilões não se misturam! As auras dos dois participantes são incompatíveis.')
    else:
        # ======= CASOS ESPECIAIS =======
        if (nome1 == 'Goku' and nome2 == 'Vegeta') or (nome1 == 'Vegeta' and nome2 == 'Goku'):
            print('Fusão realizada com sucesso! Vegito entra em combate para derrotar o exército de vilões!')
            herois_fundidos.extend([nome1, nome2])
            poder_herois += incremento_de_poder("Vegito")
        elif (nome1 == 'Goten' and nome2 == 'Trunks') or (nome1 == 'Trunks' and nome2 == 'Goten'):
            print('Fusão realizada com sucesso! Gotenks entra em combate para derrotar o exército de vilões!')
            herois_fundidos.extend([nome1, nome2])
            poder_herois += incremento_de_poder("Gotenks")
        else:
            # Verificando as fusões imperfeitas
            resultado_lista = fusaoZ(nome1, nome2, refazer1=0, refazer2=0)
            parte_nome1 = resultado_lista[0]
            parte_nome2 = resultado_lista[1]
            fusao_resultado = resultado_lista[2]
            avaliacao = avaliando_fusaoZ(parte_nome1, parte_nome2, fusao_resultado)

            if avaliacao == 'Fusão imperfeita':
                print(f'A sincronização foi um desastre... {fusao_resultado} é uma fusão imperfeita!')
                resultado_lista = fusaoZ(nome1, nome2, refazer1=1, refazer2=0)
                parte_nome1 = resultado_lista[0]
                parte_nome2 = resultado_lista[1]
                fusao_resultado = resultado_lista[2]
                avaliacao = avaliando_fusaoZ(parte_nome1, parte_nome2, fusao_resultado)

                if avaliacao == 'Fusão imperfeita':
                    print(f'A sincronização foi um desastre... {fusao_resultado} é uma fusão imperfeita!')
                    resultado_lista = fusaoZ(nome1, nome2, refazer1=1, refazer2=1)
                    parte_nome1 = resultado_lista[0]
                    parte_nome2 = resultado_lista[1]
                    fusao_resultado = resultado_lista[2]
                    avaliacao = avaliando_fusaoZ(parte_nome1, parte_nome2, fusao_resultado)

                    if avaliacao == 'Fusão imperfeita':
                        print(f'A sincronização foi um desastre... {fusao_resultado} é uma fusão imperfeita!')
                        print("Aparentemente essa combinação é incompatível...")
                    else:
                        tipo1 = tipo_personagem(nome1)
                        tipo2 = tipo_personagem(nome2)
                        ganho = registrar_fusao(tipo1, tipo2, nome1, nome2, fusao_resultado)
                        if tipo1 == 'heroi':
                            poder_herois += ganho
                        else:
                            poder_viloes += ganho
                else:
                    tipo1 = tipo_personagem(nome1)
                    tipo2 = tipo_personagem(nome2)
                    ganho = registrar_fusao(tipo1, tipo2, nome1, nome2, fusao_resultado)
                    if tipo1 == 'heroi':
                        poder_herois += ganho
                    else:
                        poder_viloes += ganho
            else:
                tipo1 = tipo_personagem(nome1)
                tipo2 = tipo_personagem(nome2)
                ganho = registrar_fusao(tipo1, tipo2, nome1, nome2, fusao_resultado)
                if tipo1 == 'heroi':
                    poder_herois += ganho
                else:
                    poder_viloes += ganho

    # ======= VERIFICANDO VENCEDOR =======
    if poder_herois > 8000:
        print("O poder dos heróis... É mais de 8000! Eles derrotam os vilões e conseguem selar o portal.")
        vencedor = True
    elif poder_viloes > 8000:
        print("Os vilões são fortes demais! Satan City está em apuros!")
        vencedor = True
