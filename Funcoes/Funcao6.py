def nome(local):

    if local == 'Rio de Janeiro':
        return f' seja bem-vindo a cidade maravilhosa'
 
    else:
        return f' seja bem-vindo a {local}'


cidade = input('digite a sua cidade: ')
usuario = input('digite o seu nome: ')

print(f'{usuario}, {nome(cidade)} ')

    
        
