r = 'A'
pMaisCaro = total = 0
while r != 'N':

    c = str(input('digite seu produto: '))
    p = int(input('digite o preço do seu produto: '))
    if r == 'A':
        pMaisBarato = p
    r = str(input('quer continuar comprando? [S/N]')).strip().upper()[0]
    total += p

    if p > pMaisCaro:
        pMaisCaro = p
    elif p < pMaisBarato:
        pMaisBarato = p
    if r == 'N':
        print(f'o produto mais caro foi {pMaisCaro}')
        print(f'o produto mais barato foi {pMaisBarato}')
        print(f'total de: {total}')
        break
