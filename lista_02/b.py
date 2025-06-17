entrada = ''

contador_uniforme = 0
contador_isotonico = 0
contador_raquete = 0
contador_toalha = 0

houve_sabotagem = False

while entrada != 'FIM':
    entrada = str(input())

    if entrada == 'Uniforme':
        contador_uniforme += 1
        print(f'Tava faltando camisa! Agora temos {contador_uniforme} uniforme(s)')
    elif entrada == 'Isotônico':
        contador_isotonico += 1
        print(f'Bora garantir a hidratação! Agora temos {contador_isotonico} isotônico(s)')
    elif entrada == 'Raquete':
        contador_raquete += 1
        print(f'Mais uma raquete saindo! Agora temos {contador_raquete} raquete(s)')
    elif entrada == 'Toalha':
        contador_toalha += 1
        print(f'Mais uma toalha saindo! Agora temos {contador_toalha} toalha(s)')
    elif entrada != 'FIM':
        material_sabotado = str(input())
        if material_sabotado == 'Uniforme' and contador_uniforme >= 1:
            contador_uniforme -= 1
            houve_sabotagem = True
            print('O sueco está roubando as camisas de Hugo!')
        elif material_sabotado == 'Isotônico' and contador_isotonico >= 1:
            contador_isotonico -= 1
            houve_sabotagem = True
            print('O sueco está sabotando a hidratação de Hugo!')
        elif material_sabotado == 'Raquete' and contador_raquete >= 1:
            contador_raquete -= 1
            houve_sabotagem = True
            print('O sueco está roubando as raquetes de Hugo!')
        elif material_sabotado == 'Toalha' and contador_toalha >= 1:
            contador_toalha -= 1
            houve_sabotagem = True
            print('O sueco está roubando as toalhas de Hugo!')


print('Bora ver o relatório final dos materiais!')
print(f'Uniforme: {contador_uniforme} unidade(s).')
print(f'Isotônico: {contador_isotonico} unidade(s).')
print(f'Raquete: {contador_raquete} unidade(s).')
print(f'Toalha: {contador_toalha} unidade(s).')

total_materiais = contador_uniforme + contador_isotonico + contador_raquete + contador_toalha

if total_materiais == 0 and houve_sabotagem:
    print('Droga... Truls Möregårdh conseguiu sabotar os materiais completamente!')
elif total_materiais == 0 and houve_sabotagem == False:
    print('Vish... Parece que vão faltar materiais para garantir a vitória do nosso atleta.')
elif total_materiais > 0 and (
    contador_uniforme == 0 or 
    contador_isotonico == 0 or 
    contador_raquete == 0 or 
    contador_toalha == 0):
    print('Ta faltando algumas coisas, mas para Hugo Calderano tudo é possível!!!')
else:
    print('Tudo pronto! Não vai faltar nada para mais um título de Hugo Calderano!')
    