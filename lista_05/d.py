# ========== ÁREA DE FUNÇÕES ==========
def gerar_tribonacci(limite, a=0, b=0, c=1, lista=None):
    if lista == None:
        lista = [a, b, c]

    proximo = a + b + c
    
    if proximo > limite:
        return lista
    lista.append(proximo)
    
    return gerar_tribonacci(limite, b, c, proximo, lista)


def verificando_tribonacci(numero):
    tribonacci = gerar_tribonacci(numero)
    return numero in tribonacci

# ---------------------------------------------------------------------------------------- #

def verificando_fatoriais(numero, atual = 1, n = 1):
    if atual == numero:
        return True
    
    elif atual > numero:
        return False
    
    else:
        return verificando_fatoriais(numero, atual * (n + 1), n + 1)
    
# ---------------------------------------------------------------------------------------- #

def somando_catalan(n, i = 0):
    # Construindo Catalan a partir da soma
    if i == n:
        return 0
    
    return catalan(i) * catalan(n - 1 - i) + somando_catalan(n, i + 1)


def catalan(n):
    # Catalan de fato
    if n == 0:
        return 1
    
    return somando_catalan(n)


def buscar_indice(valor, lista, inicio):
    if inicio >= len(lista):
        return -1
    if lista[inicio] == valor:
        return inicio
    return buscar_indice(valor, lista, inicio + 1)


def verificando_catalan(a, b, c, catalan_seq, i = 0):
    if i > len(catalan_seq) - 3:
        return False
    if catalan_seq[i] == a and catalan_seq[i + 1] == b and catalan_seq[i + 2] == c:
        return True
    return verificando_catalan(a, b, c, catalan_seq, i + 1)


def gerando_catalan(limite, i = 0, lista = None):
    # Gerando os números de Catalan
    if lista == None:
        lista = []
    
    valor = catalan(i)

    if valor > limite:
        return lista
    
    lista.append(valor)

    return gerando_catalan(limite, i + 1, lista)


def verificando_tentativa_para_catalan(entrada, valores_Runa, i = 0):
    # Percorre todos os trios consecutivos da entrada
    if i > 7:
        return False
    
    a = entrada[i]
    b = entrada[i + 1]
    c = entrada[i + 2]

    if verificando_catalan(a, b, c, valores_Runa):
        return True
    
    return verificando_tentativa_para_catalan(entrada, valores_Runa, i + 1)

# ---------------------------------------------------------------------------------------- #

def printando_numeros_utilizados(lista, valores_Runa, i = 0):
    if i > 7:
        return
    a = lista[i]
    b = lista[i + 1]
    c = lista[i + 2]
    if verificando_catalan(a, b, c, valores_Runa):
        print(f'Acabei precisando apenas dos números: {a} - {b} - {c}.')
        return
    return printando_numeros_utilizados(lista, valores_Runa, i + 1)


# ========== ÁREA DE CÓDIGO PRINCIPAL ==========

# Status
nome_maculado, vida_maculado = input().split(' - ')
vida_maculado = int(vida_maculado)
vida_maxima = vida_maculado  
runa_malenia_ativada = False
runa_godrick_ativada = False

# Total de ações = quantidade de armas que deseja aprimorar + número de tentativas de ativar runas
qtd_total_acoes = int(input())

# Loop de entradas + listas
nome_arma = []
dano_arma = []
tipo_arma = []
tentativas_armas = []

nome_runa = ''
valores_Runa = []

nivel_da_arma = []

for contador in range(qtd_total_acoes):
    entrada = input()

    # Meliante armado, repito, meliante armado
    if ' - ' in entrada:
        nome_da_arma, dano_da_arma, tipo_de_arma = entrada.split(' - ')

        nome_arma.append(nome_da_arma)

        print(f'Vou levar a/o {nome_da_arma} ela/e vai ser de grande ajuda.')

        dano_arma.append(dano_da_arma)
        tipo_arma.append(tipo_de_arma)

        nivel_da_arma.append(0)

        # Loop das tentativas/números de aprimoramento
        print('Hora de Aprimorar!!!')
        numero = ''
        dano = float(dano_arma[-1])
        while numero != 'fim':
            numero = input()
            if numero != 'fim':
                # Convertendo de str para int
                tentativa = int(numero)
                # Mechendo na arma mais recentemente adicionada
                if tipo_arma[-1] == 'basica':
                    # Indo pra função
                    if verificando_tribonacci(tentativa):
                        # Retornei True e agora avalio seu dano até o limite de 20 níveis
                        if nivel_da_arma[-1] < 20:
                            nivel_da_arma[-1] += 1
                            dano *= 1.10
                            print(f'Pronto, consegui mais um nível agora a/o {nome_da_arma} está no nível {nivel_da_arma[-1]}!')

                else:
                    # Sigo a mesma lógica anterior, só que essas são premiadas tlgd
                    if verificando_fatoriais(tentativa):
                        if nivel_da_arma[-1] < 10:
                            dano *= 1.20
                            nivel_da_arma[-1] += 1
                            print(f'Pronto, consegui mais um nível agora a/o {nome_da_arma} está no nível {nivel_da_arma[-1]}!')

        
        # Arma bufada
        dano_arma[-1] = int(dano)

        if nivel_da_arma[-1] > 0:
            print(f'Agora sim! Acho que a/o {nome_da_arma} está forte o suficiente, consegui colocar ele/a para o nível {nivel_da_arma[-1]}')
        else:
            print(f'Droga não consegui aumentar o nível da/o {nome_da_arma}')
        
        print()
    
    
    # Vamos runar (piadas a parte, você precisa ler os comentários como se estivesse vendo He-man, pq na minha cabeça isso faz total sentido)
    else:
        print('A batalha vai ser difícil melhor tentar ativar uma runa!')
        nome_runa = entrada

        print(f'Me decidi vou tentar ativar a {nome_runa}, ', end='')
        if nome_runa == 'Grande Runa de Radahn':
            print('mais vida vai ajudar muito.')

        elif nome_runa == 'Grande Runa de Morgott':
            print('quanto mais vida melhor.')
            
        elif nome_runa == 'Grande Runa de Godrick':
            print('acho que um pouco de tudo não é nada mal.')

        elif nome_runa == 'Grande Runa de Malenia':
            print('ela foi tão difícil de conseguir, tenho que testar ela pelo menos uma vez.')
        

        # Numbers (bilíngue) de tentativas
        lista_tentativas_runa = []
        for c in range(10):
            upandoRuna = int(input())
            lista_tentativas_runa.append(upandoRuna)
        
        valores_Runa = gerando_catalan(max(lista_tentativas_runa))
        
        if verificando_tentativa_para_catalan(lista_tentativas_runa, valores_Runa):
            if nome_runa == 'Grande Runa de Radahn':
                print('Isso consegui ativar a Grande Runa.')
                printando_numeros_utilizados(lista_tentativas_runa, valores_Runa)
                vida_maculado = round(vida_maculado * 1.15)
                vida_maxima = vida_maculado
            
            elif nome_runa == 'Grande Runa de Morgott':
                print('Isso consegui ativar a Grande Runa.')
                printando_numeros_utilizados(lista_tentativas_runa, valores_Runa)
                vida_maculado = round(vida_maculado * 1.25)
                vida_maxima = vida_maculado
            
            elif nome_runa == 'Grande Runa de Godrick':
                print('Isso consegui ativar a Grande Runa.')
                printando_numeros_utilizados(lista_tentativas_runa, valores_Runa)
                runa_godrick_ativada = True

            elif nome_runa == 'Grande Runa de Malenia':
                print('Isso consegui ativar a Grande Runa.')
                printando_numeros_utilizados(lista_tentativas_runa, valores_Runa)
                runa_malenia_ativada = True
        
        else:
            print('Caramba não consegui ativar a Grande Runa, infelizmente vou ter que me contentar com as armas que vou levar.')
        
        print()

# Buff de Godrick
if runa_godrick_ativada:
    for i in range(len(dano_arma)):
        dano_arma[i] = int(float(dano_arma[i] * 1.10))
    vida_maculado = round(vida_maculado * 1.10)
    vida_maxima = vida_maculado   

# Inimigo a vistaa! (Jack Sparow)
nome_inimigo, vida_inimigo, dano_inimigo = input().split(' - ')
vida_inimigo = int(vida_inimigo)
dano_inimigo = int(dano_inimigo)

batalha_ativa = True
vitoria_maculado = False

numero_turno = 1

# Fase de batalha
while batalha_ativa:

    if len(dano_arma) == 0:
        batalha_ativa = False
    else:
        print(f'{numero_turno}° TURNO')

        # Pegando os dados da arma usada no turno
        arma_utilizada = nome_arma[0]
        dano_causado = dano_arma[0]

        # Mostrar status antes do ataque
        print(f'Melhor conferir meus status antes de lutar -> vida: ({vida_maculado}/{vida_maxima})')
        print(f'E o {nome_inimigo} ainda está com {vida_inimigo} pontos de vida')

        # Ataque do maculado
        print(f'Atacando com {arma_utilizada}.')
        print(f'Consegui causar {dano_causado} de dano no/a {nome_inimigo}!!!')

        # Aplicar dano e remover arma usada
        vida_inimigo -= dano_causado
        dano_arma.pop(0)
        nome_arma.pop(0)
        tipo_arma.pop(0)
        nivel_da_arma.pop(0)

        print(f'Acabei consumindo a/o {arma_utilizada}, hora de pegar outra arma do arsenal.')

        # Efeito da runa Malenia ativada (cura 5% vida máxima por turno)
        if runa_malenia_ativada and vida_inimigo > 0 and vida_maculado < vida_maxima:
            cura_basica = round(vida_maxima * 0.05)
            cura_real = min(cura_basica, vida_maxima - vida_maculado)
            vida_maculado += cura_real
            print(f'Ainda bem que eu ativei a Grande Runa da Malenia, consegui recuperar {cura_real}')

        # Verifica se inimigo morreu
        if vida_inimigo <= 0:
            vitoria_maculado = True
            batalha_ativa = False
        else:
            # Inimigo ataca de volta
            vida_maculado -= dano_inimigo
            print(f'Droga {nome_inimigo} ainda não morreu, acabei recebendo {dano_inimigo} de dano.')
        
        # Verifica se maculado morreu
        if vida_maculado <= 0:
            batalha_ativa = False
        
        print()

    numero_turno += 1


# Fim da treta
if vitoria_maculado == True:
    print('Great Enemy Felled')

    if len(nome_arma) == 0:
        print(f'Acabei usando tudo que eu trouxe, mas finalmente consegui derrotar a/o {nome_inimigo}.')
    
    elif len(nome_arma) > 0:
        print(f'Finalmente depois de tanto me preparar consegui derrotar a/o {nome_inimigo}.')

        # Imprime arsenal restante
        num_armas_restantes = len(nome_arma)
        armas_restantes = ', '.join(nome_arma)
        print(f'Acho que me preparei bem eu ainda tenho {num_armas_restantes} arma/as sobrando são ela/as: {armas_restantes}.')

# Cenário de Derrota
if vitoria_maculado == False:
    # Se Maculado morreu (vida_maculado <= 0) - essa mensagem tem prioridade
    if vida_maculado <= 0:
        print('You Died')
        print(f'Droga acabei morrendo para a/o {nome_inimigo} e ele ainda tem {vida_inimigo} pontos de vida, vou ter que trazer armas mais fortes da próxima vez.')
    else:
        # Se as armas acabaram, mas o inimigo ainda está vivo
        if len(nome_arma) == 0 and vida_inimigo > 0:
            print(f'Parece que eu não me preparei o suficiente, acabei usando tudo que tinha e a/o {nome_inimigo} ainda tem {vida_inimigo} pontos de vida, vou ter que me preparar mais da próxima vez.')   
