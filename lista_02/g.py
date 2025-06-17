print('🎾🏆 Bem-vindo ao Torneio Fatorial Ping Pong Championship! 🧮🏓\n'
      'Hoje, o jovem Lavoi enfrentará seu maior desafio: CÁLCULOS!')
print()


print('Qual será o número que marcará o INÍCIO dessa tabuada fatorial?')
numero_inicial_estagio = int(input())
if numero_inicial_estagio >= 0:
    print(f'O número {numero_inicial_estagio} é ótimo como número inicial!')
else:
    while numero_inicial_estagio < 0:
        print(f'O número {numero_inicial_estagio} é inválido! O INÍCIO NÃO pode ser NEGATIVO.')
        numero_inicial_estagio = int(input())
    print(f'O número {numero_inicial_estagio} é ótimo como número inicial!')
print()


print('Qual será o número que marcará o FIM dessa tabuada fatorial?')
numero_final = int(input())
if numero_final >= numero_inicial_estagio:
    print(f'O número {numero_final} é ótimo como número final!')
else:
    while numero_final < numero_inicial_estagio or (numero_final < numero_inicial_estagio and numero_final < 0):
        print(f'O número {numero_final} é inválido! O FIM NÃO pode ser MENOR que o número inicial {numero_inicial_estagio}.')    
        numero_final = int(input())
    print(f'O número {numero_final} é ótimo como número final!')
print()


print('Qual será o número cujo FATORIAL será calculado?')
numero_sagrado = int(input())
if numero_sagrado >= 0:
    print(f'O número {numero_sagrado} é ótimo para o cálculo do fatorial!')
else:
    while numero_sagrado < 0:
        print(f'O número {numero_sagrado} é inválido! Números válidos são maiores ou iguais a zero.')
        numero_sagrado = int(input())
    print(f'O número {numero_sagrado} é ótimo para o cálculo do fatorial!')
print()


for estagio in range(numero_inicial_estagio, numero_final + 1):
    valor = estagio * numero_sagrado
    fatorial = 1
    for i in range(1, valor + 1):
        fatorial *= i
    print(f'({estagio} * {numero_sagrado})! = {fatorial}')
print()


print('🏁 Jornada Finalizada! Lavoi completou todos os estágios do desafio!')
print('🏓 Que sua energia vital continue brilhando nas próximas batalhas!')
