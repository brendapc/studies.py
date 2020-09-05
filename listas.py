# num = [2,5,9,1]
# print(num)
# num[2] = 4
# print(num)
# num.append(7)
# print(num)
# num.sort()
# print(num)
# print(f'esta lista tem {len(num)} elementos')
# num.pop()
# print(num)
# print(f'esta lista tem {len(num)} elementos')
#
# for n in num:
#     print(f'o numero é {n}')
#
# for c,v in enumerate(num):
#     print(f'chave:{c}, valor:{v}')
#

# valores = list()
# for con in range(0,5):
#     valores.append(int(input('digite um valor')))
# print(valores)

a = [2, 3, 4]
b = a #b = [2,3,4] e cria uma ligação entre as duas, o que for alterado em b será alterado em a

c = a[:] # copia, oq for alterado em c não será alterado em a