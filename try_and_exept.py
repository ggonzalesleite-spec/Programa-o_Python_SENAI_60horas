

# try:
#     numero = int(input("Digite um número inteiro: "))
#     print(f"Você digitou o número {numero}")
# except ValueError:
#     print("Erro: você não digitou um número inteiro válido.")

#-------------------------------------------------------------------#

# a = int(input())
# b = int(input())

# try:
#       print(a/b)

# except ZeroDivisionError as error:
#       print('como você errou? , burro')

# else:
#       print( ' Sem erros , ta otimo')

# finally:
#       print('divisão completa')

#-------------------------------------------------------------------#

lista = [10, 20, 30, 40, 50]

try:
    indice = int(input("Digite um índice: "))
    print(f"O valor no índice {indice} é {lista[indice]}")
except ValueError:
    print("Erro: você não digitou um número inteiro.")
except IndexError:
    print("Erro: índice fora do intervalo da lista.")
