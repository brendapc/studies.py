num = (int(input('digite o primeiro num: ')), int(input('digite o segundo num: ')), int(input('digite o terceiro num: ')), int(input('digite o ultimo num: ')))
print(f'voce digitou os numeros {num}')
count9 = 0
pares = ''
pos3 = 0
for n in num:
    if n % 2 == 0:
        pares += f'{n}, '
print(f'ha {num.count(9)} numeros 9')
print(f'o numero tres aparece na posição {num.index(3)}')
print(f'os numeros pares são: {pares}')