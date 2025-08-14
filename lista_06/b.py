# QUERO VER TIRAR PONTO POR USAR TUPLAAAAAAAA (Revolta, perdão.)
# Acho que nem usei aqui '-'
# Eu vou ficar muito estressado se for obrigatório usar tupla aqui. Na questão dizia que era obrigação usar dicionário!

jogadores = []
qtd_jogadores = 0
qtd_atletas_prontos = 0
qtd_mei_def_prontos = 0

# Loop
continuar = True
while continuar:
    # Nome do jogador
    nome_jogador = input()

    if nome_jogador == 'FIM':
        continuar = False
    else:
        # Disposição do jogador
        disposicao_jogador = int(input())
        # Posição do jogador
        posicao_jogador = input()
        

        jogador = {
            "nome": nome_jogador,
            "disposição do jogador": disposicao_jogador,
            "posição": posicao_jogador
        }

        # Bicho tá disposto, mas tbm, recebeno milhões ou não...
        if disposicao_jogador >= 85:
            chutes_ou_passes = int(input())
            # É passe ou é gol?
            if posicao_jogador == 'atacante':
                jogador['chutes a gol'] = chutes_ou_passes
            else:
                jogador['passes realizados'] = chutes_ou_passes
        
        elif 50 <= disposicao_jogador <= 84:
            desempenho_ultimo_jogo = int(input())
            jogador['desempenho no último jogo'] = desempenho_ultimo_jogo
        
        else:
            desempenho_ultimo_treino = int(input())
            jogador['desempenho no último treino'] = desempenho_ultimo_treino
        
        jogadores.append(jogador)
        qtd_jogadores += 1


# Outputs
for jogador in jogadores:
    # Vamos iterar
    if jogador['disposição do jogador'] >= 85:
        if jogador['posição'] == 'atacante':
            if jogador['chutes a gol'] > 10:
                print(f"{jogador['nome']} está com um bom desempenho ofensivo.")
                qtd_atletas_prontos += 1
            else:
                print(f"{jogador['nome']} pode melhorar, Ancelotti pode usá-lo no segundo tempo.")
        else:
            if jogador['passes realizados'] >= 20:
                print(f"{jogador['nome']} está com um bom desempenho de passes.")
                qtd_mei_def_prontos += 1
            else:
                print(f"{jogador['nome']} pode melhorar, Ancelotti pode não colocá-lo no primeiro tempo.")

    elif 50 <= jogador['disposição do jogador'] <= 84:
        if jogador['desempenho no último jogo'] > 80:
            print(f"O jogador {jogador['nome']} pode ser escalado para a próxima partida.")
            if jogador['posição'] == 'atacante':
                qtd_atletas_prontos += 1
            else:
                qtd_mei_def_prontos += 1
        else:
            print(f"Ancelotti precisa analisar o desempenho do {jogador['nome']} na partida.")

    else:
        if jogador['desempenho no último treino'] > 70:
            print(f"Ancelotti deve colocar {jogador['nome']} para treinar mais.")
        else:
            print(f"{jogador['nome']} não deveria estar na próxima convocação.")


# relatório
print()
print('Relatório dos jogadores:')
print(f'Total de jogadores analisados: {qtd_jogadores}')
print(f'Atacantes prontos para começar: {qtd_atletas_prontos}')
print(f'Meio-campistas e Defensores prontos para começar: {qtd_mei_def_prontos}')