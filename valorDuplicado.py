numeros = list()
while True:
    n = int(input('digite um numero'))
    if n not in numeros:
        numeros.append(n)
    else:
        print('valor duplicado')
    r = str(input('quer continuar?'))
    if r in 'Nn':
        print(sorted(numeros))
        break
