# Declarando a quantidade de golpes sofridos pelos vingadores e o total de golpes do thanos
num_golpes_sofridos_vingadores= 0
golpes_totais_do_thanos = 0

# Declarando a qtd de armas disponíveis
n = int(input())

# Declarando a lista de armas disponíveis
armas_disponiveis = []

# Flag
missao_ativa = True


# Declarando a solicitação de armas com base na quantidade máxima disponível
for i in range(1, n+1):
    armas = input()
    armas_disponiveis.append(armas)


# Solicitação de armas e loop
nome_arma = ''
quantidade_armas = [0] * n

while nome_arma != 'fim':
    nome_arma = input()

    if nome_arma != 'fim':
        if nome_arma in armas_disponiveis:
            indice = armas_disponiveis.index(nome_arma)
            quantidade_armas[indice] += 1

            if quantidade_armas[indice] == 1:
                print(f'{nome_arma} usado(a) com sucesso!')
            else:
                print(f'{nome_arma} já foi usado(a)!')
                num_golpes_sofridos_vingadores += 1
                golpes_totais_do_thanos += 1

        else:
            print(f'{nome_arma} não está disponível!')
            num_golpes_sofridos_vingadores += 1
            golpes_totais_do_thanos += 1


# Mensagem após inserir 'fim'
armas_utilizadas = sum(1 for qtd in quantidade_armas if qtd > 0)
print(f'Batalha encerrada! Os Vingadores utilizaram {armas_utilizadas} arma(s).')


if num_golpes_sofridos_vingadores == 0:
    print('Vitória! Os Vingadores salvaram o UNIVERSO!')
    print()

    print('Tony Stark:')
    print('Salvar o mundo de novo? Vou precisar de um aumento.')
    print()

    print('Thor:')
    print('Espero que tenha cerveja depois disso!')
    print()

    print('Homem-Aranha:')
    print('Posso dizer que ajudei, né? Tipo… oficialmente?')
    print('Dá pra postar isso no Insta dos Vingadores?')

elif num_golpes_sofridos_vingadores == 1:
    print('Os Vingadores sofreram um golpe do Thanos!')
    print('Vitória por pouco! Os Vingadores ganharam...')
    print()

    print('Tony Stark:')
    print('Quase que eu fico sem troco para o cafezinho.')
    print()

    print('Thor:')
    print('Esse quase foi o meu momento de “não consegui”. Mas consegui, então vale cerveja!')
    print()

    print('Peter Quill (Star-Lord):')
    print('Cara, quase perdi o ritmo do meu walkman!')

elif num_golpes_sofridos_vingadores >= 2:
    print(f'Os Vingadores sofreram {golpes_totais_do_thanos} golpes do Thanos!')
    print('Derrota... Os Vingadores não conseguiram todas as armas necessárias.')
    print()

    print('Tony Stark:')
    print('Essa não foi das melhores ideias...')
    print()

    print('Thor:')
    print('Culpa do humano. Eu sabia que devíamos ter chamado o Hulk.')