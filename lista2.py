# teste = list()
# teste.append('Brenda')
# teste.append(10)
# print(teste)
#
# galera = list()
# galera.append(teste) #teste[:] faria uma cópia
# print(galera)
#
# teste[0] = 'Maria'
# teste[1] = 20
# galera.append(teste) #para fazer cópia teste[:]
#
# print(galera) #mudou os dois

galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear()

print(galera)
print(dado)

