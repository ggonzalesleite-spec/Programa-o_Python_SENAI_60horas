def calculadora():
    n1 = float(input('nº >>'))
    op = input('>>')
    if op == '+': 
       n2 = float(input('>>')) 
       s  = soma(n1,n2)
       print(s)
    elif op == '-': 
       n2 = float(input('>>')) 
       s  = subtracao(n1,n2)
       print(s)
    elif op == '*': 
       n2 = float(input('>>')) 
       s = mult(n1,n2)
       print(s)
    elif op == '/': 
       n2 = float(input('>>')) 
       s = div(n1,n2)
       print('=', s)       

