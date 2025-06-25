# Declarando uma flag para o loop
lista_compras_finalizada = False

# Declarando a lista de compras
lista_compras = []

# Declarando o loop
while not lista_compras_finalizada:
        # Definindo entrada padrão
        entrada = input()

        # Condição de Anotar ingrediente
        if entrada == 'Anotar ingrediente':
                anotar_ingrediente = input()
                lista_compras.append(anotar_ingrediente)
        
        # Condição de ingrediente Urgente!
        elif entrada == 'Ingrediente Urgente!':
                ingrediente_urgente = input()
                lista_compras.insert(0, ingrediente_urgente)
        
        # Condição de Saci disse que já tem
        elif entrada == 'Saci disse que já tem':
                saci_disse_que_tem = input()
                if saci_disse_que_tem in lista_compras:
                    lista_compras.remove(saci_disse_que_tem)
        
        # Condição de Saci trocou a ordem
        elif entrada == 'Saci trocou a ordem':
               idx_atual = int(input())
               idx_novo = int(input())

                # Lógica para mudar a ordem
               if 0 <= idx_atual < len(lista_compras) and 0 <= idx_novo < len(lista_compras):
                      auxiliar = lista_compras[idx_atual]
                      lista_compras[idx_atual] = lista_compras[idx_novo]
                      lista_compras[idx_novo] = auxiliar
        
        # Condição de Organizar a lista
        elif entrada == 'Organizar a lista':
               novo_ingrediente_1 = input()
               novo_ingrediente_2 = input()
               
               # Lógica para troca de posições
               if novo_ingrediente_1 in lista_compras and novo_ingrediente_2 in lista_compras:
                      i1 = lista_compras.index(novo_ingrediente_1)
                      i2 = lista_compras.index(novo_ingrediente_2)

                      # Trocando de lugar
                      lista_compras[i1], lista_compras[i2] = lista_compras[i2], lista_compras[i1]

        # Definindo a condição de Deixar para depois
        elif entrada == 'Deixar para depois':
                ingrende_nao_especial = input()

                # Condição de: se o ingrediente já existe, removemo ele e logo depois o adicionamos no final da lista
                if ingrende_nao_especial in lista_compras:
                      lista_compras.remove(ingrende_nao_especial) 
                      lista_compras.append(ingrende_nao_especial)  
        
        # Definindo a condição de Ler a lista para a vovó
        elif entrada == 'Ler a lista para a vovó':
               
               # Interando a lista usando um for para remover as chaves 
               print(', '.join(lista_compras))

        elif entrada == 'E por hoje é só, pessoal!':
            lista_compras_finalizada = True

print(f'Pronto, vovó! A lista de compras para o bolo de Narizinho está pronta. Podemos ir ao mercado. A lista final é: {", ".join(lista_compras)}')
