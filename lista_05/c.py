# ========== ÁREA DE FUNÇÕES ==========
def percorre_lista_aprimoramentos(lista_aprimoramentos, lista_atributos_arma, valor_forca_atual, tipo_afinidade_atual, tipo_arma, nome_da_arma, indice_aprimoramento=0, valor_forca_inicial=None, tipo_afinidade_inicial=None, bonus_total_arma=0):
    # Inicializa os valores iniciais da arma (usado para desfazer se necessário)
    if valor_forca_inicial == None:
        valor_forca_inicial = valor_forca_atual
    if tipo_afinidade_inicial == None:
        tipo_afinidade_inicial = tipo_afinidade_atual

    # Caso base da recursão: se acabou a lista, devolve o resultado final
    if indice_aprimoramento >= len(lista_aprimoramentos):
        return valor_forca_atual, tipo_afinidade_atual

    # Pega o aprimoramento atual da lista
    aprimoramento_atual = lista_aprimoramentos[indice_aprimoramento]

    # Se o aprimoramento for uma sublista, prepara o mergulho recursivo (lá vamos nós!)
    if isinstance(aprimoramento_atual, list):
        forca_antes_sublista = valor_forca_atual
        afinidade_antes_sublista = tipo_afinidade_atual

        # Executa a sublista com a próxima afinidade (e esperança renovada)
        nova_forca, nova_afinidade = percorre_lista_aprimoramentos(aprimoramento_atual, lista_atributos_arma[:], valor_forca_atual, proxima_afinidade(tipo_afinidade_atual), tipo_arma, nome_da_arma, 0, valor_forca_atual, tipo_afinidade_atual, bonus_total_arma)

        # Se encontrou um "R", significa que não deu bom — volta tudo como era antes
        if "R" in aprimoramento_atual:
            print("Hmm, não acho que isso vai funcionar...")
            print(f"{nome_da_arma}: {nova_forca} -> {forca_antes_sublista}")
            print(f"Afinidade revertida para {afinidade_antes_sublista}")
            return percorre_lista_aprimoramentos(lista_aprimoramentos, lista_atributos_arma, forca_antes_sublista, afinidade_antes_sublista, tipo_arma, nome_da_arma, indice_aprimoramento + 1, valor_forca_inicial, tipo_afinidade_inicial, bonus_total_arma)
        
        else:
            # Se tudo deu certo, continua a saga com os novos valores
            return percorre_lista_aprimoramentos(lista_aprimoramentos, lista_atributos_arma, nova_forca, nova_afinidade, tipo_arma, nome_da_arma, indice_aprimoramento + 1, valor_forca_inicial, tipo_afinidade_inicial, bonus_total_arma)

    else:
        # Decodifica o tipo de atributo do aprimoramento atual (estilo RPG clássico)
        nome_atributo_aprimoramento = ""
        if aprimoramento_atual == "S": nome_atributo_aprimoramento = "força"
        elif aprimoramento_atual == "D": nome_atributo_aprimoramento = "destreza"
        elif aprimoramento_atual == "I": nome_atributo_aprimoramento = "inteligência"
        elif aprimoramento_atual == "F": nome_atributo_aprimoramento = "fé"
        elif aprimoramento_atual == "A": nome_atributo_aprimoramento = "arcano"

        # Aplica o bônus com base nos atributos e na afinidade — força bruta ou sabedoria arcana?
        if nome_atributo_aprimoramento:
            if nome_atributo_aprimoramento in lista_atributos_arma and nome_atributo_aprimoramento == atributo_extra(tipo_afinidade_atual):
                valor_forca_atual += 2
            elif nome_atributo_aprimoramento in lista_atributos_arma or nome_atributo_aprimoramento == atributo_extra(tipo_afinidade_atual):
                valor_forca_atual += 1
        # Bônus direto para armas normais (reforço no martelo +3)
        elif aprimoramento_atual == "+" and tipo_arma == "normal":
            valor_forca_atual += 3
            bonus_total_arma += 3
        # Bônus direto para armas especiais (porque são... especiais)
        elif aprimoramento_atual == "-" and tipo_arma == "especial":
            valor_forca_atual += 5
            bonus_total_arma += 5

    # Chama a função novamente para o próximo aprimoramento.
    return percorre_lista_aprimoramentos(lista_aprimoramentos, lista_atributos_arma, valor_forca_atual, tipo_afinidade_atual, tipo_arma, nome_da_arma, indice_aprimoramento + 1, valor_forca_inicial, tipo_afinidade_inicial, bonus_total_arma)


def atributo_extra(tipo_afinidade):
    if tipo_afinidade == "fogo":
        return "força"
    elif tipo_afinidade == "físico":
        return "destreza"
    elif tipo_afinidade == "mágico":
        return "inteligência"
    elif tipo_afinidade == "dourado":
        return "fé"
    elif tipo_afinidade == "oculto":
        return "arcano"

# Gira a roleta das afinidades e retorna a próxima 
def proxima_afinidade(tipo_afinidade):
    ordem_afinidades = ["físico", "mágico", "fogo", "dourado", "oculto"]
    indice_afinidade = ordem_afinidades.index(tipo_afinidade)
    return ordem_afinidades[(indice_afinidade + 1) % len(ordem_afinidades)]


# ========== ÁREA DE CÓDIGO PRINCIPAL ==========
# Um pequeno desabafo...
print("Não aguento mais morrer para a Malenia, Blade of Miquella...")
print("Vou refazer minha build!\n")

# Lista para armazenar todas as armas que o jogador vai aprimorar
lista_armas = []
entrada_usuario = input()
while entrada_usuario != "finalizar":
    partes_entrada = entrada_usuario.split(" - ")
    nome_arma_usuario = partes_entrada[0]
    tipo_arma_usuario = partes_entrada[1]
    valor_forca_usuario = int(partes_entrada[2])
    tipo_afinidade_usuario = partes_entrada[3]
    lista_atributos_usuario = partes_entrada[4:]
    lista_armas.append([nome_arma_usuario, tipo_arma_usuario, valor_forca_usuario, tipo_afinidade_usuario, lista_atributos_usuario])
    entrada_usuario = input()

# Listas para armazenar resultados após os aprimoramentos
lista_nome_e_poder = []
lista_afinidades_finais = []

# Para cada arma, aplica os aprimoramentos recursivamente
for indice_arma in range(len(lista_armas)):
    nome_arma_atual = lista_armas[indice_arma][0]
    tipo_arma_atual = lista_armas[indice_arma][1]
    valor_forca_atual = lista_armas[indice_arma][2]
    tipo_afinidade_atual = lista_armas[indice_arma][3]
    lista_atributos_arma_atual = lista_armas[indice_arma][4]

    lista_aprimoramentos_arma = eval(input())
    valor_forca_final, tipo_afinidade_final = percorre_lista_aprimoramentos(
        lista_aprimoramentos_arma,
        lista_atributos_arma_atual,
        valor_forca_atual,
        tipo_afinidade_atual,
        tipo_arma_atual,
        nome_arma_atual
    )
    lista_nome_e_poder.append(f"{nome_arma_atual}: {valor_forca_final}")
    lista_afinidades_finais.append(tipo_afinidade_final)
    print(f"{nome_arma_atual} aprimorado!")

# Exibe o inventário final do jogador
print("Inventário:")
for indice_arma in range(len(lista_nome_e_poder)):
    print(f"- {lista_nome_e_poder[indice_arma]}")
    print(f"- afinidade: {lista_afinidades_finais[indice_arma]}")
    if lista_afinidades_finais[indice_arma] == "fogo":
        print("Fogo... é uma das fraquezas da Malenia!!!")
    elif lista_afinidades_finais[indice_arma] == "dourado":
        print("É, não acho que uma arma de fé vá me ajudar muito...")

# Contagem das afinidades finais 
quantidade_armas_fogo = lista_afinidades_finais.count("fogo")
quantidade_armas_fisico = lista_afinidades_finais.count("físico")
quantidade_armas_magico = lista_afinidades_finais.count("mágico")
quantidade_armas_dourado = lista_afinidades_finais.count("dourado")
quantidade_armas_oculto = lista_afinidades_finais.count("oculto")

# Hora de julgar se vale a pena encarar a Malenia ou voltar farmar Runa
print()
if quantidade_armas_fogo > max(quantidade_armas_fisico, quantidade_armas_magico, quantidade_armas_dourado, quantidade_armas_oculto):
    print("Muitas armas de fogo, ela não vai ter chance!")
elif quantidade_armas_dourado > max(quantidade_armas_fogo, quantidade_armas_fisico, quantidade_armas_magico, quantidade_armas_oculto):
    print("Acho que vou ter que refazer meus aprimoramentos...")
else:
    print("Analisando meu inventário agora, acho que consigo vencer, pode vir, Malenia, Blade of Miquella!!")
