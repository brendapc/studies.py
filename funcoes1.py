def linha(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


linha('ola')

def contador(* num): #o asterisco fala que não tem quantidade de parametros definida
    print(num)


contador(2,3,4,5)
contador(3,4)
contador(1)

def dobra(list):
    pos = 0
    while pos< len(list):
        list[pos] *= 2
        pos += 1


valores = [2, 4, 5, 6, 7]
valores2 = valores[:]
dobra(valores2)
print(valores)
print(valores2)


def soma(* val):
    s = 0
    for n in val:
        s += n
    print(f'a soma dos valores é: {s}')

soma(3,3,5)