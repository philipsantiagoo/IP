A = int(input())
L = int(input())
P = int(input())
H = int(input())

diamantes_arthur = A * H
diamantes_luiz = L * H
diamantes_pedro = P * H

x_inicial = (diamantes_arthur + diamantes_luiz +
             abs(diamantes_arthur - diamantes_luiz)) // 2
x_final = (diamantes_pedro + x_inicial + abs(diamantes_pedro - x_inicial)) // 2

print(x_final)
