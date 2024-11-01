lista = []

def CampoGrande(): 
    for i in range(2):
        nome = input('digite seu nome: ')
        telefone = int(input('digite seu numero de telefone: '))
        cidade = input('digite sua cidade: ')
        lista.append({'nome':nome,'idade':telefone,'cidade':cidade})
    
def buscar():
    i = 0

    while ( i < len(lista)):

        if(lista[i]['cidade'] == 'CAMPO GRANDE'):
            print(lista[i])

        i += 1

CampoGrande()
buscar()                    

   

