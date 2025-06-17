qtd_pessoas = int(input())
contador = 0

voto_classica = 0
voto_caneta = 0
voto_classineta = 0

while contador < qtd_pessoas:
    voto = str(input())

    if voto == 'Clássica':
        voto_classica += 1
    elif voto == 'Caneta':
        voto_caneta += 1
    else:
        voto_classineta += 1

    contador += 1


print('Estamos calculando... tão rápido quanto dar Run no Dikastis...')


if voto_classica > voto_caneta and voto_classica > voto_classineta:
    primeiro_lugar = 'Clássica'
    pts_primeiro = voto_classica
    print(f'1º lugar: {primeiro_lugar} ({pts_primeiro} votos)')

    if voto_caneta > voto_classineta:
        segundo_lugar = 'Caneta'
        pts_segundo = voto_caneta
        print(f'2º lugar: {segundo_lugar} ({pts_segundo} votos)')

        terceiro_lugar = 'Classineta'
        pts_terceiro = voto_classineta
        print(f'3º lugar: {terceiro_lugar} ({pts_terceiro} votos)')
    
    elif voto_classineta > voto_caneta:
        segundo_lugar = 'Classineta'
        pts_segundo = voto_classineta
        print(f'2º lugar: {segundo_lugar} ({pts_segundo} votos)')

        terceiro_lugar = 'Caneta'
        pts_terceiro = voto_caneta
        print(f'3º lugar: {terceiro_lugar} ({pts_terceiro} votos)')


elif voto_caneta > voto_classica and voto_caneta > voto_classineta:
    primeiro_lugar = 'Caneta'
    pts_primeiro = voto_caneta
    print(f'1º lugar: {primeiro_lugar} ({pts_primeiro} votos)')

    if voto_classica > voto_classineta:
        segundo_lugar = 'Clássica'
        pts_segundo = voto_classica
        print(f'2º lugar: {segundo_lugar} ({pts_segundo} votos)')

        terceiro_lugar = 'Classineta'
        pts_terceiro = voto_classineta
        print(f'3º lugar: {terceiro_lugar} ({pts_terceiro} votos)')
    
    elif voto_classineta > voto_classica:
        segundo_lugar = 'Classineta'
        pts_segundo = voto_classineta
        print(f'2º lugar: {segundo_lugar} ({pts_segundo} votos)')

        terceiro_lugar = 'Clássica'
        pts_terceiro = voto_classica
        print(f'3º lugar: {terceiro_lugar} ({pts_terceiro} votos)')


else:
    primeiro_lugar = 'Classineta'
    pts_primeiro = voto_classineta
    print(f'1º lugar: {primeiro_lugar} ({pts_primeiro} votos)')

    if voto_classica > voto_caneta:
        segundo_lugar = 'Clássica'
        pts_segundo = voto_classica
        print(f'2º lugar: {segundo_lugar} ({pts_segundo} votos)')

        terceiro_lugar = 'Caneta'
        pts_terceiro = voto_caneta 
        print(f'3º lugar: {terceiro_lugar} ({pts_terceiro} votos)')
    
    elif voto_caneta > voto_classica:
        segundo_lugar = 'Caneta'
        pts_segundo = voto_caneta
        print(f'2º lugar: {segundo_lugar} ({pts_segundo} votos)')

        terceiro_lugar = 'Clássica'
        pts_terceiro = voto_classineta
        print(f'3º lugar: {terceiro_lugar} ({pts_terceiro} votos)')


if primeiro_lugar == 'Clássica' and (pts_primeiro - pts_segundo >= 5):
    print('Podemos ver que a influência do grande Hugo Calderano foi disseminada pelos corredores do CIn!')
