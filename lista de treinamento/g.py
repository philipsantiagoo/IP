D = int(input())

if D < 1:
    print('ERROR')
elif D <= 10:
    print('Arthur')
elif 10 < D <= 30:
    print('Luiz')
elif 30 < D <= 100:
    print('Pedro')
else:
    print('Nenhum')
