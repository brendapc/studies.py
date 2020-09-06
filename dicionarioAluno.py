aluno = dict()
aluno['nome'] = str(input('digite um nome: '))
aluno['media'] = int(input('digite a media: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
else:
    aluno['situacao'] = 'reprovado'
print(aluno)