for a in range(1,5): #funciona como um a<5 e não <=
    print('oi') #imprime 4 vezes

for b in range(6 , 0, -1): # de 6 à 1 decrescendo
    print(b)
print('------')

for d in range(0, 10 , 2): #de zero a dez de dois em dois d<10
    print(d)
print('fim')

inicio = 0
fim = 10
passo = 2
for c in range(inicio, fim+1, passo):
    print(c)

s = 0
for e in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print(s)

for c in range(1,50):
    if(c%2 == 0):
        print(c)

for a in range(1, 500):
    if(a%2 != 0):
        if(a%3 == 0):
            print(a)
soma = 0
for b in range(0, 6):
    num = int(input('digite um número'))
    if num%2 == 0:
        soma += num
print(soma)

num = int(input('Digite um numero'))
primo = 0
count = 0
for d in range(1, num+1):
    if num % d == 0:
        if d == 1 or d == num:
            primo += 1
            count += 1
        else:
            count += 1
if primo >= count:
    print('numero é primo')
else:
    print('não é primo, ele é divisivel por {} numeros'.format(count))