# filme = {
#     'titulo': 'star wars',
#     'ano': 1977,
#     'diretor': 'George Lucas'
# }
# print(filme.values()) #star wars
# print(filme.keys()) # titulo
# print(filme.items()) #  titulo, star wars
#
# for k, v in filme.items():
#     print(f'o {k} é {v}')
#
# eu = {'nome': 'brenda', 'idade': 17}
# print(f'eu me chamo {eu["nome"]} e tenho {eu["idade"]} anos')

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('unidade federetiva: '))
    estado['sigla'] = str(input('sigla do estado: '))
    brasil.append(estado.copy()) # não tem como fazer estado[:]
print(brasil)