# Acho uma tremenda falta de empatia na lista de tupla ser proibido usar tupla. É tipo um vegetariano dizer que não pode comer vegetais?????

def ranking_dos_melhores(tecnicos, ranking):
    # flags
    contador = 1
    continuar = True

    # loop
    while continuar:
        # buscando a chave do dicionário maior: {'Tecnico_1': {...}, 'Tecnico_2': {...}, ...}
        chave = f'Tecnico_{contador}'
        if chave in tecnicos:
            # analisando os subdicionários e pegando as chaves deles
            tecnico = tecnicos[chave]

            nome = tecnico['nome']
            nacionalidade = tecnico['nacionalidade']

            # verificar 'tecnico_valido' e só continuar se for True ou não existir
            if 'tecnico_valido' not in tecnico or tecnico['tecnico_valido']:
                titulos_continentais = tecnico['titulos_continentais']
                titulos_nacionais = tecnico['titulos_nacionais']
                aproveitamento = tecnico['aproveitamento']
                interesse = tecnico['interesse']
                nome = tecnico['nome']

                # calculando a pontuação de acordo com a regrinha de vocês
                pontuacao_total = ((titulos_continentais * 100) + (titulos_nacionais * 50)) * aproveitamento

                # Blá, blá, blá...
                if titulos_continentais == 0:
                    pontuacao_total *= 0.5

                if nacionalidade == 'brasileiro':
                    pontuacao_total *= 1.10
                # Preconceito com Rivaldo, agora só tirar 10% de alemão? Mermão, cês sabem o que significa 7x1??
                elif nacionalidade == 'alemão':
                    pontuacao_total *= 0.90
                
                # armazenando no dicionário ranking
                ranking[nome] = {
                    'pontuacao': pontuacao_total,
                    'nacionalidade': nacionalidade,
                    'interesse': interesse,
                    'nome': nome
                }

            contador += 1

        else:
            continuar = False


# Código principal
qtd_tecnicos = int(input())

# loop
tecnicos = {}
contador = 1
ranking = {}

for dados in range(qtd_tecnicos):
    nome = input()
    nacionalidade = input()

    # hermanos uma ova, argentino bom é argentino chorando
    if nacionalidade == 'argentino':
        # Agora adiciona no dicionário para imprimir a mensagem depois, mesmo inválido
        dados_dos_tecnicos = {
            'nome': nome,
            'nacionalidade': nacionalidade,
            'tecnico_valido': False
        }
        tecnicos[f'Tecnico_{contador}'] = dados_dos_tecnicos
        contador += 1
    else:
        titulos_continentais = int(input())
        titulos_nacionais = int(input())
        aproveitamento = float(input())
        interesse = input()

        dados_dos_tecnicos = {
            'nome': nome,
            'nacionalidade': nacionalidade,
            'titulos_continentais': titulos_continentais,
            'titulos_nacionais': titulos_nacionais,
            'aproveitamento': aproveitamento,
            'interesse': interesse,
            'tecnico_valido': True
        }

        tecnicos[f'Tecnico_{contador}'] = dados_dos_tecnicos

        contador += 1


# outputs
for chave in tecnicos:
    tecnico = tecnicos[chave]
    nacionalidade = tecnicos[chave]

    nome_do_tecnico = tecnico['nome']
    nacionalidade_do_tecnico = tecnico['nacionalidade']
    
    if nome_do_tecnico == 'Ancelotti':
        print('Será que Carleto irá continuar no cargo?')
    
    if nome_do_tecnico == 'Jorge Jesus':
        print('O mister finalmente retornará ao Brasil?')
    
    if nacionalidade_do_tecnico == 'argentino' and 'tecnico_valido' in tecnico and not tecnico['tecnico_valido']:
        print('Um hermano comandando a seleção? Sai fora!')
    
    if nacionalidade_do_tecnico == 'alemão':
        print('Iremos mesmo perdoar o 7x1?')


ranking_dos_melhores(tecnicos, ranking)

# outputs PARTE 1
print('Lista de treinadores - CBF')

primeiro_colocado = ''
segundo_colocado = ''
terceiro_colocado = ''

maior_pontuacao = -1
segunda_maior_pontuacao = -1
terceira_maior_pontuacao = -1

for nome in ranking:
    pontos = float(ranking[nome]['pontuacao'])

    for nome in ranking:
        pontos = ranking[nome]['pontuacao']

        if pontos > maior_pontuacao:
            terceira_maior_pontuacao = segunda_maior_pontuacao
            terceiro_colocado = segundo_colocado

            segunda_maior_pontuacao = maior_pontuacao
            segundo_colocado = primeiro_colocado

            maior_pontuacao = pontos
            primeiro_colocado = nome

        elif pontos > segunda_maior_pontuacao and pontos != maior_pontuacao:
            terceira_maior_pontuacao = segunda_maior_pontuacao
            terceiro_colocado = segundo_colocado

            segunda_maior_pontuacao = pontos
            segundo_colocado = nome

        elif pontos > terceira_maior_pontuacao and pontos != maior_pontuacao and pontos != segunda_maior_pontuacao:
            terceira_maior_pontuacao = pontos
            terceiro_colocado = nome

print(f"1º {primeiro_colocado} - {ranking[primeiro_colocado]['nacionalidade']} - {ranking[primeiro_colocado]['pontuacao']:.2f} pontos")
print(f"2º {segundo_colocado} - {ranking[segundo_colocado]['nacionalidade']} - {ranking[segundo_colocado]['pontuacao']:.2f} pontos")
print(f"3º {terceiro_colocado} - {ranking[terceiro_colocado]['nacionalidade']} - {ranking[terceiro_colocado]['pontuacao']:.2f} pontos")

# outputs PARTE 2
tecnico_escolhido = False
posicao = 1
if 'Ancelotti' in ranking and ranking['Ancelotti']['interesse'] == 'sim':
    nacionalidade_ancelotti = ranking['Ancelotti']['nacionalidade']
    if nacionalidade_ancelotti != 'brasileiro':
        print(f'Ancelotti será o quarto estrangeiro a treinar o Brasil. Que honra para o {nacionalidade_ancelotti}!')
    print('Depois de uma longa novela, Carlo Ancelotti continuará como o treinador da Seleção Brasileira! Estamos bem servidos!')
else:
    tecnico_escolhido = False
    posicao = 1

    while posicao <= 3 and not tecnico_escolhido:
        if posicao == 1:
            tecnico_nome = primeiro_colocado
        elif posicao == 2:
            tecnico_nome = segundo_colocado
        else:  
            tecnico_nome = terceiro_colocado

        tem_interesse = ranking[tecnico_nome]['interesse']

        if tem_interesse == 'sim':
            tecnico_escolhido = True
            nacionalidade_n = ranking[tecnico_nome]['nacionalidade']

            if nacionalidade_n != 'brasileiro':
                print(f'{tecnico_nome} será o quarto estrangeiro a treinar o Brasil. Que honra para o {nacionalidade_n}!')

            if tecnico_nome == 'Jorge Jesus':
                print('JESUS VOLTOU!!! Será que ele conseguirá repetir na seleção o sucesso que obteve no Flamengo?')

            elif tecnico_nome == 'Felipão':
                print('FELIPÃO DE NOVO!? Vem mais um 7x1 por aí?')

            else:
                print(f'O técnico {nacionalidade_n} {tecnico_nome} irá treinar o Brasil. Não era o nome que esperávamos, mas torcemos para que faça um bom trabalho!')

        else:
            print(f'O {tecnico_nome} não aceitou a proposta da CBF e outros nomes serão analisados. Cuida, CBF!')

        posicao += 1

    if not tecnico_escolhido:
        print("Nenhum técnico aceitou a maior seleção do mundo!? Que humilhação, Sr. Samir Xaud!!!")
