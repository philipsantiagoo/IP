humor_byte = str(input()).capitalize()

qtd_vezes_senta = int(input())
qtd_vezes_patinha = int(input())
qtd_vezes_fica = int(input())
qtd_vezes_pega = int(input())

proximo_comando = str(input())


if proximo_comando == 'Senta':
  qtd_vezes_senta += 1
elif proximo_comando == 'Dá a patinha':
  qtd_vezes_patinha += 1
elif proximo_comando == 'Fica':
    qtd_vezes_fica += 1
elif proximo_comando == 'Pega':
  qtd_vezes_pega += 1


if proximo_comando == 'Senta' and qtd_vezes_senta >= 2 and humor_byte != 'Brincalhão':
  print('Byte é o melhor')
elif proximo_comando == 'Senta' and qtd_vezes_senta >= 2 and humor_byte == 'Brincalhão':
  print('Ele parece estar muito animado para isso!')

elif proximo_comando == 'Dá a patinha' and qtd_vezes_patinha >= 2:
  print('Ele é um bom garoto!')

elif proximo_comando == 'Fica' and qtd_vezes_fica >= 2 and humor_byte != 'Brincalhão':
  print('Ele está aprendendo')
elif proximo_comando == 'Fica' and qtd_vezes_fica >= 2 and humor_byte == 'Brincalhão':
  print('Ele não consegue ficar parado')

elif proximo_comando == 'Pega' and qtd_vezes_pega >= 2 and humor_byte != 'Preguiçoso':
  print('Ele é muito ágil!')
elif proximo_comando == 'Pega' and qtd_vezes_pega >= 2 and humor_byte == 'Preguiçoso':
  print('Quem não tem seu momento de preguiça?')

elif (proximo_comando == 'Pega' and qtd_vezes_pega < 2) or (proximo_comando == 'Senta' and qtd_vezes_senta < 2) or (proximo_comando == 'Dá a patinha' and qtd_vezes_patinha < 2) or (proximo_comando == 'Fica' and qtd_vezes_fica < 2):
  print('Parece que ele não aprendeu esse truque ainda')
 

truque1 = ''
truque2 = ''
truque3 = ''
truque4 = ''

if qtd_vezes_senta > 2:
  truque1 = 'Senta'
if qtd_vezes_patinha > 2:
  truque2 = 'Dá a patinha'
if qtd_vezes_fica > 2:
  truque3 = 'Fica'
if qtd_vezes_pega > 2:
  truque4 = 'Pega'


if qtd_vezes_senta > 2 or qtd_vezes_patinha > 2 or qtd_vezes_fica > 2 or qtd_vezes_pega > 2:
  print(f'O nosso novo mascote estava {humor_byte} e aprendeu o(s) seguinte(s) truque(s):')
if truque1 != '':
  print(truque1)
if truque2 != '':
  print(truque2)
if truque3 != '':
  print(truque3)
if truque4 != '':
  print(truque4)