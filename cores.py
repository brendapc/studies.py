print('\033[4;31;43mOlá mundo\033[m')
a = 3
b = 5
print('os valores são \033[1;33m{}\033[m e \033[1;31m{}'.format(a, b))

cores = { 'limpa': '\033[m', 'amarelo': '\033[1;33m', 'vermelho': '\033[1;31m'}

print('{}parabéns'.format(cores['vermelho']))