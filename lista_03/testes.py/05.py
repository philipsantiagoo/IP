# Cria a lista
lista = [1, 4, 55, 6, 9, 10]
tamanho_lista = len(lista)
meio_lista = int(tamanho_lista/2)

lista_1 = lista[0:meio_lista]
lista_2 = lista[meio_lista:]

lista_soma = []

for indice in range(0, 3):
    lista_soma.append(lista_1[indice] + lista_2[indice])

print(lista)
print(tamanho_lista)
print(meio_lista)
print(lista_1)
print(lista_2)
print(lista_soma)