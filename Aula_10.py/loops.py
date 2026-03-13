
# for numero in range(0, 1001):
#     print(numero)

#---------------------------------------------#

# nomes = []
# contador = 0

# while contador < 10:
#     nome = input("Digite o nome da pessoa: ")
#     nomes.append(nome)
#     contador += 1

# print("\nLista de pessoas:")

# for nome in nomes:
#     print(nome)

#---------------------------------------------#

usuario_correto = "aluno"
senha_correta = "1234"

tentativas = 0
acesso = False

# Sistema de login (3 tentativas)
while tentativas < 3:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Acesso permitido ao sistema!")
        acesso = True
        break
    else:
        tentativas += 1
        print("Usuário ou senha incorretos.")

if acesso == False:
    print("Conta bloqueada! Senha incorreta 3 vezes.")

else:
    notas = []

    quantidade = int(input("Quantas notas deseja inserir? "))

    for i in range(quantidade):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)

    soma = 0
    for nota in notas:
        soma += nota

    media = soma / len(notas)

    print("Notas do aluno:", notas)
    print("Média do aluno:", media)

input('Digite enter para sair')


#---------------------------------------------#

