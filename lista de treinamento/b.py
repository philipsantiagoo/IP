x1 = int(input())
z1 = int(input())


hogsmeade_x2 = 34
hogsmeade_z2 = 220

kakariko_x2 = 0
kakariko_z2 = 0

loneliness_x2 = 140
loneliness_z2 = 456


d_tantan_hogsmeade = ((x1 - hogsmeade_x2)**2 + (z1 - hogsmeade_z2)**2)**0.5
print(f'Distancia para Hogsmeade: {d_tantan_hogsmeade:.2f}')

d_tantan_kakariko = ((x1 - kakariko_x2)**2 + (z1 - kakariko_z2)**2)**0.5
print(f'Distancia para Kakariko: {d_tantan_kakariko:.2f}')

d_tantan_loneliness = ((x1 - loneliness_x2)**2 + (z1 - loneliness_z2)**2)**0.5
print(f'Distancia para Solitude: {d_tantan_loneliness:.2f}')
