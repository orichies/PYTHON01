def medias(n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4) / 4
    if media >= 7:
       return "APROVADO"
    
    elif media < 7 and media > 4:
       return "EM RECUPERAÇÃO"
    
    else:
       return "REPROVADO"
    
def definemedia(nome):    
    notas = []

    for i in range(4):
        notas.append(float(input(f"DIGITE A {i + 1}ª NOTA: ")))
    print(f"O ALUNO {nome} ESTÁ: {medias(notas[0], notas[1], notas[2], notas[3])}")    
    aprovados.append(f"{nome} {medias(notas[0], notas[1], notas[2], notas[3])}")

aprovados = []

for i in range(5):
    nomealuno = input("DIGITE O NOME DO ALUNO: ")
    definemedia(nomealuno)

print(aprovados)

