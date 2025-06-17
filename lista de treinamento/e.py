D = int(input())
C = int(input())


total_ticks_por_hora = (24000 * 3) * 3
ticks_utilizaveis = total_ticks_por_hora / 2

if D == 0:
    print(0)
else:
    ticks_totais_disponiveis = ticks_utilizaveis * D
    ticks_por_casa = ticks_totais_disponiveis / C

    print(int(ticks_por_casa))
