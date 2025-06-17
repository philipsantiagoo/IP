N = str(input())
S = str(input())


if len(N) + len(S) < 3 or len(N) + len(S) > 16:
    print('O número total de caracteres não está entre 3 e 16')

elif ' ' in N or ' ' in S:
    print('Não é permitido espaços')

elif '!@#$%¨&*()-=+' in N or '!@#$%¨&*()-=+' in S:
    print('Apenas caracteres alfanuméricos e underlines são permitidos')

else:
    print(N, end='')
    print(S)
