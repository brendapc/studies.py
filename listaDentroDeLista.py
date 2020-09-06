num = [ [], []]
for n in range(0,6):
    valor = int(input('digite um valor'))
    if valor%2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'pares em: {num[0]}')
print(f'impares em: {num[1]}')