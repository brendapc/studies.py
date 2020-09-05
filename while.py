# s = ''
# while s != 'F' and s != 'M':
#     s = str(input('Digite o sexo com M ou F: '))

# num = 2
# chute = 0
# chutes = 0
# while chute != 2:
#     chute = int(input('digite o seu palpite: '))
#     chutes += 1
# print('foram necessários {} chutes'.format(chutes))


o = 0
while o != 5:
    n1 = int(input('digite o primeiro valor: '))
    n2 = int(input('digite o segundo valor: '))
    print('[1]somar', '[2]multiplicar', '[3]maior valor', '[4]novos numeros', '[5]sair do programa')
    o = int(input('digite o número da operação desejada: '))
    if o == 1:
        print(n1+n2)
        o = 0
    elif o == 2:
        print(n1*n2)
    elif o == 3:
        if n1>n2:
            print(n1)
        elif n2>n1:
            print(n2)
        else:
            print('eles são iguais')
            o = 0
    elif o == 4:

        o = 0
    elif 0 == 5:
        o = 5
    else:
        result = 'opção inválida'
