palavras = ('amanda','juliana', 'maria', 'julia', 'ana', 'rebeca')

for p in palavras:
    print(f'\nna palavra {p} temos:', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')