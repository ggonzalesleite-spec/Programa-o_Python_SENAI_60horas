print('sistema de verificação de média')

nome = input('digite o nome do aluno:')

print('digite as notas do aluno', nome)

n1 = float(input('digite sua nota'))
n2 = float(input('digite sua nota'))
n3 = float(input('digite sua nota'))

print(n1 + n2 + n3)
print('***' * 15)
print('media do aluno(a)', nome)
media = (n1 + n2 + n3) / 3
print('media do aluno(a)', nome)
print(media)

aprovado = media >= 7
reculperação = media >=5 and media <7
reprovado = media < 5

print(f'''

situação do aluno(A) {nome}
aprovado?{aprovado}
reculperação?{reculperação}
reprovado?{reprovado}


''')