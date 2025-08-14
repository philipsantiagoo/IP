# Função
def shift_ascii_chars(caractere, deslocamento_shift, conjunto_caracteres_permitidos):
    # nosso objetivo é deslocar o 'caractere' dento do 'conjunto_caracteres_permitidos', dentro do limite de tamnho permito

    # verifico se caractere tá no conjunto 
    if caractere in conjunto_caracteres_permitidos:
        # obetendo o índice do danado
        posicao_atual_caractere = conjunto_caracteres_permitidos.index(caractere)

        # calculando a nova posição após o deslocamento shift
        nova_posicao_atual_caractere = (posicao_atual_caractere + deslocamento_shift) % len(conjunto_caracteres_permitidos)

        # retorna o novo caractere
        return conjunto_caracteres_permitidos[nova_posicao_atual_caractere]

    else:
        # caractere não tava nos permitidos
        return caractere


def descripitografando(nome_criptogafado, conjunto_caracteres_permitidos):
    # vendo onde tá o meio do nome
    meio_nome = len(nome_criptogafado) // 2

    # aquelas regras lá, tu sabe, tu ta ligado já que eu sei
    if len(nome_criptogafado) % 2 == 0:
        primeira_metade_nome_criptografado = nome_criptogafado[:meio_nome]
        segunda_metade_nome_criptografado = nome_criptogafado[meio_nome:]
    else:
        primeira_metade_nome_criptografado = nome_criptogafado[:meio_nome]
        segunda_metade_nome_criptografado = nome_criptogafado[meio_nome:]
    
    segunda_metade_nome_criptografado = [
        shift_ascii_chars(caractere, 1, conjunto_caracteres_permitidos)
        for caractere in segunda_metade_nome_criptografado
    ]

    combinado = list(primeira_metade_nome_criptografado) + segunda_metade_nome_criptografado

    combinado_revertido = combinado[::-1]
    
    resultado = [
        shift_ascii_chars(caractere, -3, conjunto_caracteres_permitidos) 
        for caractere in combinado_revertido
        ]

    return ''.join(resultado)


# dados fornecidos
ascii_chars = [
    ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?',
    '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_',
    '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'
]




# código principal
# inteiro 1 <= N <= 25
qtd_nomes_criptografados = int(input())


nomes_criptografados = {}
nomes_descriptografados = {}


for c in range(1, qtd_nomes_criptografados + 1):
    nome_criptografado = input()

    # adicionando no dicionário
    nomes_criptografados[f'nome_{c}'] = nome_criptografado


# chamando a danada, a periculosa, a função da descriptografia (diabo de nome difícil de escrever vei)
for chave, nome_criptografado in nomes_criptografados.items():
    nome_descriptografado = descripitografando(nome_criptografado, ascii_chars)
    nomes_descriptografados[chave] = nome_descriptografado


# outputs FASE 1
for chave in nomes_criptografados:
    criptografado = nomes_criptografados[chave]
    descriptografado = nomes_descriptografados[chave]

    print(f'Criptografada: {criptografado}')
    print(f'Descriptografada: {descriptografado}')
    print('--------------------------------------------------')

# outputs FASE 2
for chave in nomes_descriptografados:
    # não é uma crítica, mas quem fez a questão sabe que Rivaldo foi um dos melhores em campo né? 
    descriptografado = nomes_descriptografados[chave]

    if descriptografado == 'Ronaldo':
        print('Ronaldo Fenômeno detectado! Autor dos gols na final!')
    
    if descriptografado == 'Ronaldinho':
        print('Ronaldinho Gaúcho chegou! Chamem o inglês que ele vai chutar do meio-campo...')
    
    if descriptografado == 'Cafu':
        print('Capitão Cafu presente! O único a jogar 3 finais de Copa seguidas!')
    
    if descriptografado == 'Marcos':
        print('Marcos está na área! O paredão do Brasil em 2002!')
    
    if descriptografado == 'Luiz Felipe Scolari':
        print('Técnico reconhecido: Luiz Felipe Scolari — o comandante do penta!')
    
    else:
        if descriptografado != 'Ronaldo' and descriptografado != 'Ronaldinho' and descriptografado != 'Cafu' and descriptografado != 'Marcos' and descriptografado != 'Luiz Felipe Scolari':
            print(f'{descriptografado} está confirmado na escalação!')

print()

# outputs FASE 3
jogadores = [nome for nome in nomes_descriptografados.values() if nome != 'Luiz Felipe Scolari']
quantidade_jogadores = len(jogadores)
tecnico_presente = 'Luiz Felipe Scolari' in nomes_descriptografados.values()


if quantidade_jogadores < 11:
    print('!!!!!!!!!! Escalação incompleta! !!!!!!!!!!')
    print(f'Só foram encontrados {quantidade_jogadores} jogadores. Faltam jogadores para completar o time.')
else:
    print('++++++++++ Escalação Confirmada ++++++++++')
    print('Escalação Oficial da Seleção Brasileira — Copa do Mundo 2002')
    print('==================================================')
    for nome in jogadores:
        print(f'->{nome}')
    print('==================================================')


if not tecnico_presente:
    print('!!!!!!!!!! Técnico não encontrado! !!!!!!!!!!')
    print('Como vamos jogar sem treinar? Como vamos ganhar o penta?')
else:
    print('========== Técnico ==========')
    print('Luiz Felipe Scolari (Felipão)')


if tecnico_presente and quantidade_jogadores >= 11:
    print('===== Tudo pronto! Rumo ao Penta! =====')
    print('Escalação completa com técnico confirmado.')
    print('Que comece o espetáculo, Brasil rumo ao penta!')
