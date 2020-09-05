
for a in range(1, 6):
    peso = float(input('Peso da {}a pessoa'.format(a)))
    if a==1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('o maior peso foi {}'.format(maior))
print('o menor peso foi {}'.format(menor))