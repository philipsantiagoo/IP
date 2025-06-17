valor_mensal_dolar = int(input())
cotacao_dolar = float(input())
gasto_mensal_reais_racao = int(input())
gasto_mensal_reais_aluguel = int(input())
gasto_mensal_reais_onibus = int(input())


conversao_dolar_real = valor_mensal_dolar * cotacao_dolar
gastos_totais = gasto_mensal_reais_racao + \
    gasto_mensal_reais_aluguel + gasto_mensal_reais_onibus


if conversao_dolar_real > gastos_totais:
    print('Me chama pra sua casa um dia pra gente comer Pedigree! Com essa grana dá pra alugar uma ManCão!')
elif conversao_dolar_real == gastos_totais:
    print('Vai dar pra alugar sua casa, mas sugiro que você vá trabalhar se quiser gastar com outra coisa!')
else:
    print('Eu acho melhor você ir morar comigo no Cin! O RU é só 4 reais e lá no DA tem saco de dormir!')


if gasto_mensal_reais_racao > gasto_mensal_reais_aluguel and gasto_mensal_reais_racao > gasto_mensal_reais_onibus:
    maior = 'Ração'
    print('A inflaCão deu pros cachorros, viu! Sugiro que você vá no Coffee Break dos calouros e leve toda a comida!')
elif gasto_mensal_reais_aluguel > gasto_mensal_reais_racao and gasto_mensal_reais_aluguel > gasto_mensal_reais_racao:
    maior = 'Aluguel'
    print('Não está fácil pra ninguém... Tenta dividir o aluguel com algum estudante aí!')
else:
    maior = 'Ônibus'
    print('Você consegue voar, por que quer orçamento de ônibus? Vai ser feliz!')


print(f'MESADA (dólares): {valor_mensal_dolar:.2f} dólares\n'
      f'MESADA (reais): {conversao_dolar_real:.2f} reais\n'
      f'MAIOR GASTO: {maior}')
