n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

soma_dos_numeros = n1 + n2 + n3 + n4 + n5

resto_da_div = soma_dos_numeros % 5

monitor = ''

if resto_da_div == 0:
    monitor = 'Arthur'
if resto_da_div == 1:
    monitor = 'Bruna'
if resto_da_div == 2:
    monitor = 'César'
if resto_da_div == 3:
    monitor = 'Daniel'
if resto_da_div == 4:
    monitor = 'Eduarda'

print(f'{monitor} vai ter a honra de passear com Byte hoje!')