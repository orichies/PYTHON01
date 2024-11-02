#CONSTRUA UMA PÁGINA ONDE O USUÁRIO DIGITARÁ O NOME E A MÉDIA DE 5 ALUNOS E O PROGRAMA SÓ ACEITARÁ A MÉDIA DO ALUNO CASO ELA ESTEJA ENTRE 0 E 10

notas = []

def media():
    for i in range(2):
        nome = input('digite o nome do aluno: ')
        media = float(input("digite a média do aluno: "))

        while media < 0 or media > 10:
            media = float(input(" Digite uma média válida: ")) 
            
            
        notas.append({'nome':nome,'media':media})

       
media()
print(notas)