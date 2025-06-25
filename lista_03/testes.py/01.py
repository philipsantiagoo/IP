# Bloco de testes sobre listas 

lista_alunos = ['João', 'Maria', 'Pedro', 'Ana', 'Lucas']
print(lista_alunos)

for aluno in lista_alunos:
    print(aluno, end=', ')
print('fim da chamada!')

"""
    Listas não são imutáveis

    len: retorna o tamanho da lista
    Listas são iteráveis, é possível percorrer ela usando for
"""

print(f'A truma possui {len(lista_alunos)} alunos no total')

