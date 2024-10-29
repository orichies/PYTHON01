def ProgramasInfantis():
    lista1 = ["PEIXONAUTA, DINOTREM, TOM E JERRY"]
    print(lista1)
    return    

def Carros():
    carro =[
            {
            "MODELO":"JEEP RENEGADE",
             "PREÇO":120000
            },

            {
             "MODELO":"AMAROK",
             "PREÇO":350000
            },
             
            {
             "MODELO":"PORSCHE CAYENNE", 
             "PREÇO":700000
            }, 

            {
            "MODELO":"LAMBORGHINI",
             "PREÇO":1000000
            }
        ] 
    
    for c in carro:
        print(f'{c["MODELO"]} - R${c["PREÇO"]}')
    
    return

idade = int(input("DIGITE SUA IDADE: "))

if idade >= 18:
    print("MAIOR DE IDADE")
    Carros()
else:
    ProgramasInfantis()
 