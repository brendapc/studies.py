numExtenso = ('um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
n = int(input('digite um numero'))-1
res = numExtenso[n]
if 1 <= n <= 20 :
    print(f' o numero é: {res}')
