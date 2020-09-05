nome = str(input('qual é seu nome? '))
if nome == 'Brenda':
    print('legal! o meu tambem')
elif nome == 'Pedro' or nome == 'João' or nome == 'Maicon':
    print('seu nome é um nome masculino')
elif nome in 'ana juliana marcela rebeca julia':
    print('seu nome é um nome feminino')
else:
    print('bom pra você')
print('tenha um bom dia {}'.format(nome))

