jogador_1 = input()
jogador_2 = input()

if ((jogador_1 == "Luis" or jogador_1 == "Lavoisier" or jogador_1 == "Joab" or jogador_1 == "Renan") and (jogador_2 == "Luis" or jogador_2 == "Lavoisier" or jogador_2 == "Joab" or jogador_2 == "Renan")):
    print("Essa partida vai ser épica! O jogo vai ser emocionante!")

num_sets = int(input())

nivel_disputa = input()

rebatidas = 0

if (nivel_disputa == "aprendizes"):
    rebatidas = 1
elif (nivel_disputa == "básicos"):
    rebatidas = 2
else:
    rebatidas = 3

hit = rebatidas

reb_max = 0

pontos_jogador_1 = 0
pontos_jogador_2 = 0

total_pontos_jogador_1 = 0
total_pontos_jogador_2 = 0

jogador_atual = 1

for n in range(1, num_sets + 1):
    print(f"Iniciando o {n}º set")
    acabou = False
    pontos_jogador_1 = 0
    pontos_jogador_2 = 0
    hit = rebatidas
    reb_max = 0

    while not acabou:
        acao = input()

        if (acao == "saque"):

            entrada_1 = input()
            entrada_2 = input()

            if (jogador_atual%2 != 0):

                print(f"O saque é de {jogador_1}")

                if (entrada_1 == "SA" and entrada_2 == "AO"):
                    print("Um saque PERFEITO!!")
                    jogador_atual = 2

                elif (entrada_1 == "SA" and entrada_2 == "SA"):
                    print(f"{jogador_1}, a bola quicou duas vezes na sua própria área! Que saque feio foi esse??")
                    jogador_atual = 2
                    pontos_jogador_2 += 1
                
                elif (entrada_1 == "AO" and entrada_2 == "AO"):
                    print(f"Boa, {jogador_1}! Deu ponto de graça pro oponente!! Agora quem saca é {jogador_2}")
                    jogador_atual = 2
                    pontos_jogador_2 += 1

                else:
                    print("Vish, ainda bateu na rede")
                    pontos_jogador_2 += 1
                    jogador_atual = 2
            
            else:
                print(f"O saque é de {jogador_2}")

                if (entrada_1 == "SA" and entrada_2 == "AO"):
                    print("Um saque PERFEITO!!")
                    jogador_atual = 1

                elif (entrada_1 == "SA" and entrada_2 == "SA"):
                    print(f"{jogador_2}, a bola quicou duas vezes na sua própria área! Que saque feio foi esse??")
                    jogador_atual = 1 
                    pontos_jogador_1 += 1
                
                elif (entrada_1 == "AO" and entrada_2 == "AO"):
                    print(f"Boa, {jogador_2}! Deu ponto de graça pro oponente!! Agora quem saca é {jogador_1}")
                    jogador_atual = 1
                    pontos_jogador_1 += 1                
                else:
                    print("Vish, ainda bateu na rede")
                    pontos_jogador_1 += 1
                    jogador_atual = 1

        if (acao == "rebatida"):

            while (hit > 0):

                entrada_Acao = input()

                if (jogador_atual%2 != 0 or jogador_1 in entrada_Acao):

                    if (entrada_Acao == "oponente rebateu"):
                        jogador_atual = 2
                        reb_max += 1
                        hit -= 1
                    else:
                        jogador_atual = 2
                        pontos_jogador_2 += 1
                        hit = 0
                        
                elif (jogador_atual%2 == 0  or jogador_2 in entrada_Acao):
                    if (entrada_Acao == "oponente rebateu"):
                        jogador_atual = 1
                        reb_max += 1
                        hit -= 1
                    
                    else:
                        jogador_atual = 1
                        pontos_jogador_1 += 1
                        hit = 0

        if (rebatidas == reb_max):
            velocidade_jogador_1 = int(input())
            velocidade_jogador_2 = int(input())

           
            if (velocidade_jogador_1 < velocidade_jogador_2):
                pontos_jogador_1 += 1
                jogador_atual = 1
            else:
                pontos_jogador_2 += 1
                jogador_atual = 2

        
        diferenca = abs(pontos_jogador_1 - pontos_jogador_2)
        reb_max = 0
        hit = rebatidas


        if (diferenca >= 2 and pontos_jogador_1 >= 3 and pontos_jogador_1 > pontos_jogador_2):
            total_pontos_jogador_1 += 1
            jogador_atual = 1
            pontos_jogador_1 = 0
            pontos_jogador_2 = 0
            acabou = True

        elif (diferenca >= 2 and pontos_jogador_2 >= 3 and pontos_jogador_2 > pontos_jogador_1):
            total_pontos_jogador_2 += 1
            jogador_atual = 1
            pontos_jogador_1 = 0
            pontos_jogador_2 = 0
            acabou = True


if (total_pontos_jogador_1 > total_pontos_jogador_2):
    print(f"Depois de {num_sets} set(s) vibrante(s), o grande vencedor é {jogador_1}!!\nFim do jogo!")
else:
    print(f"Depois de {num_sets} set(s) vibrante(s), o grande vencedor é {jogador_2}!!\nFim do jogo!")