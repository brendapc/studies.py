#() -> tuplas, [] -> listas, {} -> dicionários
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')  #parenteses não-obrigatórios mas coloquei para fins de clareza
print(lanche)
print(lanche[1:3]) #inclui o 1 mas não inclui o 3

#lanche[4] = 'agua' #error: tupla não podem ser alteradas
print(lanche)

# for comida in lanche:
#     print(f'eu vou comer {comida}') #modo alternativo para .format()

# for cont in range(0, len(lanche)):
#     print(f'eu vou comer {lanche[cont]}')
#
# print(sorted(lanche))

# a = (2, 3, 4)
# b = (5, 6, 7)
# c = a + b
# print(c)
# print(c.index(4))

tabela = ('gremio','palmeiras','flamengo','botafogo','bahia','juventude','cruzeiro','atlético MG','atletico PR','aimoré','as guria fc','os guri fc','tudo nosso fc','goias','corinthias','são paulo','fluminense','vasco','santos','internacional',)
print(tabela[0:5])
print(len(tabela))
print(tabela[15:20])

print(tabela.index('gremio'))
print(sorted(tabela))