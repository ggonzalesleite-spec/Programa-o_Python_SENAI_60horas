
def cumprimento(nome):
    return 'olá', nome

def produto(lista_prod, prod, carrinho, meus_v, lista_valores, paga):

    carrinho.append(lista_prod[prod])
    meus_v.append(lista_valores[paga])
    return carrinho,'- R$', sum(meus_v)


def pagamento(lista_tip_pags, escolha_pag):
    return lista_tip_pags[escolha_pag]




def restaurante():
   
    menu = ['','SALADA', 'MACARRONADA', 'SANDUICHE', 'SORVETE']
    valores  = [0,100,60,150,250]
    carrinho = []
    meus_valores = []
    nome = input('Nome: ')
    print(cumprimento(nome))
    # for v in valores:
    #    for p in menu, valores:
    #      print(p, v)      
    e  =  int(input('Escolha seu produto: 1 ,2 ,3, 4'))
    produto()


restaurante()
    # escolha = input('''
       


    # ''')
