def calculo():
    nomes = []
    idades = []

    for c in range(3):
        nomes.append(input('Digite o nome da pessoa: '))
        idades.append(int(input('Digite agora a idade da pessoa: ')))
     
        index = idades.index(min(idades)) 

    print(f'{nomes[index]} é a pessoa mais nova, com {min(idades)} anos')

calculo()    




    


