#frase = str(input('digite uma frase: ')).strip()
# count = 0
# for letra in frase:
#     if letra in 'aA':
#         count += 1
# print(count)
# outro modo:
frase = str(input('digite uma frase: ')).lower().strip()
print('a letra a aparece {} vezes'.format(frase.count('a')))
print('a primeira vez que a letra a apareceu foi na posição: {}'.format(frase.find('a'))) # dá a posição do primeiro 'a' que achar
print('a primeira vez que a letra a apareceu foi na posição: {}'.format(frase.rfind('a'))) # dá a posição do primeiro 'a' que achar começando pelo lado Direito (Right
