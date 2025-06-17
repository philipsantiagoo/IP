nome_do_aluno = str(input())
acertos_lista_1 = int(input())
acertos_lista_2 = int(input())
acertos_lista_3 = int(input())
acertos_lista_4 = int(input())
acertos_lista_5 = int(input())
acertos_lista_6 = int(input())

a1 = acertos_lista_1 * 1
a2 = acertos_lista_2 * 1
a3 = acertos_lista_3 * 1
a4 = acertos_lista_4 * (10/6)
a5 = acertos_lista_5 * (10/6)
a6 = acertos_lista_6 * (10/6)

media_geral = (a1 + a2 + a3 + a4 + a5 + a6) / 6
print(f'A média de {nome_do_aluno} é {media_geral:.1f}')

if a1 <= a2 <= a3 and a4 <= a5 <= a6:
    print('Progresso constante! Parabéns pelo esforço!')
else:
    print('Alerta! Queda no rendimento.')

listas_nao_feitas = 0
if acertos_lista_1 == 0:
    listas_nao_feitas += 1
if acertos_lista_2 == 0:
    listas_nao_feitas += 1
if acertos_lista_3 == 0:
    listas_nao_feitas += 1
if acertos_lista_4 == 0:
    listas_nao_feitas += 1
if acertos_lista_5 == 0:
    listas_nao_feitas += 1
if acertos_lista_6 == 0:
    listas_nao_feitas += 1

if listas_nao_feitas >= 2:
    print('Alerta! Múltiplas listas não respondidas.')

if media_geral >= 8:
    print('Parabéns pelo excelente desempenho! Continue "au" sim.')
elif media_geral >= 7:
    print('Parabéns pelo bom desempenho!')
else:
    print('Alerta! Desempenho abaixo do esperado.')
