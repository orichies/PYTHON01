# CONSTRUA UM PROGRAMA ONDE O USUARIO DIGITARÁ SEIS NUMEROS EM UM VETOR E DEPOIS, ESSES NUMEROS DEVEM SER EXIBIDOS NA TELA NA ORDEM DIGITADA.

lista = []

for i in range(6):
    i = int(input(" digite um número: ")) 

    lista.append(i)
    lista.sort()

    print(lista)



    
