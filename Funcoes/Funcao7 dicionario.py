pessoa = []

for i in range(5):
    nome = input('digite seu nome: ')
    idade = int(input('digite sua idade: '))
    pessoa.append({'nome':nome,'idade':idade})

def buscar():
    i = 0
    menor = 0

    while(i < 4):
        if(pessoa[1]['idade'] < pessoa[menor]['idade']):
          menor = 1

        else:
          menor = menor

        i += 1
    return menor
print(f'{pessoa[buscar()]}')                   


    


