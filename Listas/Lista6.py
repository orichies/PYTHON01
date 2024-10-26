# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

listaC = []
listaV = ['a', 'e', 'i', 'o', 'u']
for i in range(6):
    resposta = (input("Digite a letra: "))
    if resposta.lower() != listaV[0] and resposta.lower() != listaV[1] and resposta.lower() != listaV[2] and resposta.lower() != listaV[3] and resposta.lower() != listaV[4]:
        listaC.append(resposta)
print(listaC)        