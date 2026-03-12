import random

for chances in range(3):
    a = random.randint(1,10)
    chute = int(input('digite seu chute: '))
    print('você tem,', chances, 'chances')
    if a == chute:
        print('Ganhou!! acertou em cheio')
        break
    else:
        print('errou feio')
        if chances == 0:
       
          print('não acertou nenhum...')
