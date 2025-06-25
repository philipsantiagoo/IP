# Entrada: quantidade de ondas
n = int(input())

# Listas para armazenar dados de cada onda
diferencas = []
participantes = []
vencedores = []

# Variáveis para pontuação
ponto_vilao = 0
ponto_heroi = 0

# Loop das ondas
for c in range(1, n + 1):
    entrada_de_personagens = input()
    personagem_na_disputa = entrada_de_personagens.split(', ')
    disputa = personagem_na_disputa[1:-1]  # tira o primeiro e último

    numero_de_herois = 0
    numero_de_viloes = 0

    for personagem in disputa:
        tipo = personagem[:2]
        if tipo == 'H-':
            numero_de_herois += 1
        elif tipo == 'V-':
            numero_de_viloes += 1

    diferenca = numero_de_herois - numero_de_viloes
    diferencas.append(diferenca)
    participantes.append(entrada_de_personagens)
    if diferenca > 0:
        ponto_heroi += 1
        vencedores.append("heroi")
    elif diferenca < 0:
        ponto_vilao += 1
        vencedores.append("vilao")
    else:
        vencedores.append("empate")

# Identifica a onda com maior diferença
maior_diferenca = 0
indice_melhor_onda = -1
for i, dif in enumerate(diferencas):
    if abs(dif) > maior_diferenca:
        maior_diferenca = abs(dif)
        indice_melhor_onda = i
    elif abs(dif) == maior_diferenca and maior_diferenca != 0:
        if i < indice_melhor_onda:
            indice_melhor_onda = i

# Imprime resultado da onda com maior diferença
if maior_diferenca == 0:
    print("🌀Nenhuma onda foi selecionada como a menos acirrada e a mais favorável para nenhum do dois lados!")
else:
    if vencedores[indice_melhor_onda] == "heroi":
        print(f"🌀Onda {indice_melhor_onda+1} foi a menos acirrada e a mais favorável para os heróis!")
    elif vencedores[indice_melhor_onda] == "vilao":
        print(f"🌀Onda {indice_melhor_onda+1} foi a menos acirrada e a mais favorável para os vilões!")
    print(f"Participantes analisados: {participantes[indice_melhor_onda]}")

# Resultado final
print("Agora vamos ao resultado geral das ondas...")
print(f"Heróis: {ponto_heroi} | Vilões: {ponto_vilao}")

if ponto_heroi > ponto_vilao:
    print("Ufa, os heróis dominaram! Central City está seguro outra vez")
elif ponto_vilao > ponto_heroi:
    print("Ah, não. Os vilões vão dominar Central City e mandar todos os heróis embora!")
else:
    print("Ninguém é mais forte que ninguém. Heróis e vilões vão ter que entrar em consenso para viverem no mesmo espaço")
