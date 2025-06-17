cin_x = 500 
cin_y = 100

velocidade = 2
pausa = 15

concha_x = 400
concha_y = 500

laguinho_x = 300
laguinho_y = 1000

hospital_x = 1000
hospital_y = 1000

atletismo_x = 800
atletismo_y = 100

lugar = str(input())

if lugar == 'Concha Acústica da UFPE':
    distancia_entre_dois_pontos = ( (500 - 400)**2 + (100 - 500)**2 )**0.5
    distancia_total_percorrida = round(distancia_entre_dois_pontos * 2)
    tempo_total_gasto = round(((distancia_total_percorrida / 2) / 60) + 15)

if lugar == 'Laguinho da UFPE':
    distancia_entre_dois_pontos = ( (500 - 300)**2 + (100 - 1000)**2 )**0.5
    distancia_total_percorrida = round(distancia_entre_dois_pontos * 2)
    tempo_total_gasto = round(((distancia_entre_dois_pontos / 2) / 60) + 15)

if lugar == 'Hospital das Clínicas':
    distancia_entre_dois_pontos = ( (500 - 1000)**2 + (100 - 1000)**2 )**0.5
    distancia_total_percorrida = round(distancia_entre_dois_pontos * 2)
    tempo_total_gasto = round(((distancia_entre_dois_pontos / 2) / 60) + 15)

if lugar == 'Ginásio e Pista de Atletismo da UFPE':
    distancia_entre_dois_pontos = ( (500 - 800)**2 + (100 - 100)**2 )**0.5
    distancia_total_percorrida = round(distancia_entre_dois_pontos * 2)
    tempo_total_gasto = round(((distancia_entre_dois_pontos / 2) / 60) + 15)

print(f'Byte visitou {lugar}, caminhou {int(distancia_total_percorrida)} metros e gastou {int(tempo_total_gasto)} minutos passeando!')

if lugar == 'Concha Acústica da UFPE':
    print('Aqui é muito grande mesmo! Muitos eventos ocorrem por aqui!')
if lugar == 'Laguinho da UFPE':
    print('Nossa, mas esse lago é longe hein?!')
if lugar == 'Hospital das Clínicas':
    print('Um dos hospitais mais importantes do estado também fica na área do Campus da UFPE!')
if lugar == 'Ginásio e Pista de Atletismo da UFPE':
    print('Que legal! O Ginásio é bem perto do CIn!')