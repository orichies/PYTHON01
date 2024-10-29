# construa um programa onde o usuario digitara o nome e a media de 10 alunos
# e o programa escreverá na tela o nome de todos com a media > ou = a 6

nome = []
media = []

for i in range(2):
    nome.append(input("DIGITE O NOME DO ALUNO: "))
    media.append(int(input("DIGITE A MÉDIA DO ALUNO: ")))

    if media >= 6:
        print(media[i])



