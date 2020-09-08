temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('digite o nome: ')))
    temp.append(float(input('digite o peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    resp = str(input('voce quer continuar? [S/N]'))
    temp.clear()
    if resp in 'nN':
        break