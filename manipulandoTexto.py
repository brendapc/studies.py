frase = 'curso em video python' #como se fosse um array de 0:20
print(len(frase)) #length
recorte = frase[9:13] # de nove à treze, inclui o nove e exclui o treze
print(recorte)
print(frase.find(('python'))) #frase[15]
print('video' in frase) # true

frase2 = frase.replace('python', 'javascript')
print(frase2)

frase3 = frase2.split() #split: cada palavra vira um array
print(frase3[0])
print(frase3[0][2])
print(len(frase3))
