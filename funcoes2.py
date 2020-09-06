#escopo
def teste():
    global n #diz que oq for feito com o n aqui dentro deve acontecer com o n global
    n += 2
    x = 8
    print(x)
    print(n)

n = 1

teste()#teste() marca o fim do escopo

n = 2 #fora do escopo

#print(x) #só funciona dentro do corpo da função
print(n)

