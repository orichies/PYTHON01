Lista = []

def bairros(): 
    for i in range(2):
        nome = input('digite seu nome: ')
        bairro = (input('digite o nome do seu bairro: '))
        Lista.append({'nome':nome,'bairro':bairro})

    ListaOrdenada = sorted(Lista, key = lambda d: d ['nome'])
    print(ListaOrdenada) 

bairros()      