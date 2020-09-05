#entrada "ana maria de souza" saída: primeiro nome: 'ana' ultimo 'souza'
nome = str(input('digite seu nome: ')).strip().split()
print('primeiro nome: {}'.format(nome[0]))
print('ultimo nome: {}'.format(nome[len(nome)-1]))