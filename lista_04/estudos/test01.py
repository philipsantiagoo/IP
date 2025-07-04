def print_max(a, b):
    if a > b:
        print(f'{a} é maior que {b}')
    elif a < b:
        print(f'{a} é menor que {b}')
    else:
        print(f'{a} é igual a {b}')


# chama print_max
x = int(input())
y = int(input())

print_max(x, y)