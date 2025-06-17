contador_de_rodadas = 1
baralho_coup = 0
pontos_luvusier = 0
pontos_jaob = 0

numero_rodadas = int(input())
print("Vamos dar início à disputa!!! TOMADA!!!")
vencedor_tomada = input()

if vencedor_tomada == "Jaob":
    print("Jaob veio de Catende e está pronto para vencer!!!")
elif vencedor_tomada == "Luvusier":
    print("Nada se cria, tudo se transforma, então Luvusier irá se transformar em um vencedor!!!")
    
nome_monitor = vencedor_tomada


rodadas_contadas = 1


while contador_de_rodadas <= numero_rodadas and baralho_coup == 0:

    if rodadas_contadas == 1:
        print(f"COMEÇA A {contador_de_rodadas}ª RODADA!")
        objeto_que_foi_acertado = input()

        while objeto_que_foi_acertado != "mesa":
            objeto_que_foi_acertado = input()

    rodadas_contadas = 0

    if objeto_que_foi_acertado == "mesa":
        while objeto_que_foi_acertado == "mesa":
            print(f"{nome_monitor} jogou a bolinha no(a) {objeto_que_foi_acertado}!")
            if nome_monitor == "Luvusier":
                nome_monitor = "Jaob"
            else:
                nome_monitor = "Luvusier"
            objeto_que_foi_acertado = input()

    else:
        if nome_monitor == "Jaob":
            if objeto_que_foi_acertado == "Baralho de UNO":
                pontos_jaob += 2
                print(f"{nome_monitor} jogou a bolinha no(a) {objeto_que_foi_acertado}!")
                print(f"{nome_monitor} teve uma grande pontaria e acertou {objeto_que_foi_acertado}! Agora está com {pontos_jaob} pontos.")

            elif objeto_que_foi_acertado == "Armário de Homero e Elena":
                pontos_jaob += 3
                print(f"{nome_monitor} jogou a bolinha no(a) {objeto_que_foi_acertado}!")
                print(f"{nome_monitor} teve uma grande pontaria e acertou {objeto_que_foi_acertado}! Agora está com {pontos_jaob} pontos.")

            elif objeto_que_foi_acertado == "Peça de Dominó":
                pontos_jaob += 3
                print(f"{nome_monitor} jogou a bolinha no(a) {objeto_que_foi_acertado}!")
                print(f"{nome_monitor} teve uma grande pontaria e acertou {objeto_que_foi_acertado}! Agora está com {pontos_jaob} pontos.")

            elif objeto_que_foi_acertado == "Baralho de Coup Desaparecido":
                pontos_jaob += 100
                print(f"{nome_monitor} jogou a bolinha no(a) {objeto_que_foi_acertado}!")
                print(f"{nome_monitor} teve uma grande pontaria e acertou {objeto_que_foi_acertado}! Agora está com {pontos_jaob} pontos.")
                print(f"{nome_monitor} achou o Coup!!! Ele merece a vitória sem dúvidas!")
                baralho_coup = 1
                
            elif objeto_que_foi_acertado == "Nada":
                pontos_jaob -= 1
                if pontos_jaob < 0:
                    pontos_jaob = 0
                print(f"{nome_monitor} jogou a bolinha no(a) {objeto_que_foi_acertado}!")
                print(f"{nome_monitor} teve mãos de alface e acertou o(a) {objeto_que_foi_acertado}. Agora está com {pontos_jaob} pontos.")
                nome_monitor = "Luvusier"

            elif objeto_que_foi_acertado == "Projetor":
                pontos_jaob -= 2
                if pontos_jaob < 0:
                    pontos_jaob = 0
                print(f"{nome_monitor} jogou a bolinha no(a) {objeto_que_foi_acertado}!")
                print(f"{nome_monitor} teve mãos de alface e acertou o(a) {objeto_que_foi_acertado}. Agora está com {pontos_jaob} pontos.")
                nome_monitor = "Luvusier"

            elif objeto_que_foi_acertado == "Computador":
                pontos_jaob -= 3
                if pontos_jaob < 0:
                    pontos_jaob = 0
                print(f"{nome_monitor} jogou a bolinha no(a) {objeto_que_foi_acertado}!")
                print(f"{nome_monitor} teve mãos de alface e acertou o(a) {objeto_que_foi_acertado}. Agora está com {pontos_jaob} pontos.")
                nome_monitor = "Luvusier"

            elif objeto_que_foi_acertado == "Cabeça do Amiguinho":
                pontos_jaob -= 5
                if pontos_jaob < 0:
                    pontos_jaob = 0
                print(f"{nome_monitor} jogou a bolinha no(a) {objeto_que_foi_acertado}!")
                print(f"{nome_monitor} teve mãos de alface e acertou o(a) {objeto_que_foi_acertado}. Agora está com {pontos_jaob} pontos.")
                nome_monitor = "Luvusier"
                
        else:
            if objeto_que_foi_acertado == "Baralho de UNO":
                pontos_luvusier += 2
                print(f"{nome_monitor} jogou a bolinha no(a) {objeto_que_foi_acertado}!")
                print(f"{nome_monitor} teve uma grande pontaria e acertou {objeto_que_foi_acertado}! Agora está com {pontos_luvusier} pontos.")

            elif objeto_que_foi_acertado == "Armário de Homero e Elena":
                pontos_luvusier += 3
                print(f"{nome_monitor} jogou a bolinha no(a) {objeto_que_foi_acertado}!")
                print(f"{nome_monitor} teve uma grande pontaria e acertou {objeto_que_foi_acertado}! Agora está com {pontos_luvusier} pontos.")

            elif objeto_que_foi_acertado == "Peça de Dominó":
                pontos_luvusier += 3
                print(f"{nome_monitor} jogou a bolinha no(a) {objeto_que_foi_acertado}!")
                print(f"{nome_monitor} teve uma grande pontaria e acertou {objeto_que_foi_acertado}! Agora está com {pontos_luvusier} pontos.")

            elif objeto_que_foi_acertado == "Baralho de Coup Desaparecido":
                pontos_luvusier += 100
                print(f"{nome_monitor} jogou a bolinha no(a) {objeto_que_foi_acertado}!")
                print(f"{nome_monitor} teve uma grande pontaria e acertou {objeto_que_foi_acertado}! Agora está com {pontos_luvusier} pontos.")
                print(f"{nome_monitor} achou o Coup!!! Ele merece a vitória sem dúvidas!")
                baralho_coup = 1
                
            elif objeto_que_foi_acertado == "Nada":
                pontos_luvusier -= 1
                if pontos_luvusier < 0:
                    pontos_luvusier = 0
                print(f"{nome_monitor} jogou a bolinha no(a) {objeto_que_foi_acertado}!")
                print(f"{nome_monitor} teve mãos de alface e acertou o(a) {objeto_que_foi_acertado}. Agora está com {pontos_luvusier} pontos.")
                nome_monitor = "Jaob"

            elif objeto_que_foi_acertado == "Projetor":
                pontos_luvusier -= 2
                if pontos_luvusier < 0:
                    pontos_luvusier = 0
                print(f"{nome_monitor} jogou a bolinha no(a) {objeto_que_foi_acertado}!")
                print(f"{nome_monitor} teve mãos de alface e acertou o(a) {objeto_que_foi_acertado}. Agora está com {pontos_luvusier} pontos.")
                nome_monitor = "Jaob"

            elif objeto_que_foi_acertado == "Computador":
                pontos_luvusier -= 3
                if pontos_luvusier < 0:
                    pontos_luvusier = 0
                print(f"{nome_monitor} jogou a bolinha no(a) {objeto_que_foi_acertado}!")
                print(f"{nome_monitor} teve mãos de alface e acertou o(a) {objeto_que_foi_acertado}. Agora está com {pontos_luvusier} pontos.")
                nome_monitor = "Jaob"

            elif objeto_que_foi_acertado == "Cabeça do Amiguinho":
                pontos_luvusier -= 5
                if pontos_luvusier < 0:
                    pontos_luvusier = 0
                print(f"{nome_monitor} jogou a bolinha no(a) {objeto_que_foi_acertado}!")
                print(f"{nome_monitor} teve mãos de alface e acertou o(a) {objeto_que_foi_acertado}. Agora está com {pontos_luvusier} pontos.")
                nome_monitor = "Jaob"

        if baralho_coup == 0:
            contador_de_rodadas += 1
            rodadas_contadas = 1
            

print("\nTEMOS O RESULTADO DA PARTIDA!")
if pontos_jaob > pontos_luvusier:
    print(f"Jaob deu orgulho à Catende e ganhou a disputa com {pontos_jaob} pontos!")
elif pontos_luvusier > pontos_jaob:
    print(f"A química está em festa, Luvusier ganha a disputa com {pontos_luvusier} pontos!")
else:
    print("Jaob usou a sua autoridade como monitor-chefe e ganhou a disputa mesmo com o empate!")