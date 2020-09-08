people = []
person = {}
while True:
    person['name'] = str(input('nome: '))
    person['age'] = int(input('idade: '))
    person['gender'] = str(input('sexo: [M/F]'))
    if person['gender'] not in 'FfMm':
        print('ERRO! digite apenas F ou M')
        person['gender'] = str(input('sexo: [M/F]'))
    c = str(input('quer continuar? '))
    if c not in 'SsNn':
        print('ERRO! digite apenas S ou N')
    people.append(person.copy())
    if c in 'Nn':
        break
print(people)
print(f'ao todo temos {len(people)} pessoas cadastradas')
