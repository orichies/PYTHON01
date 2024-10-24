Nota1 = float(input( " Digite O Primeiro Número: "))

Nota2 = float(input( " Digite O Segundo Número: "))

media = Nota1 + Nota2 / 2


if media < 4:
    print(f" Sua Média é de: {media} , Você Está Reprovado! ")

elif media > 7:
    print(f" Sua Média é de: {media} , Você Foi Aprovado! ")

else:
    print(f" Sua Média é de: {media} , Você Está Na Recuperação! ")

    recuperacao = float(input(" Digite Sua Nota De Recuperação: "))

    if recuperacao < 5:
        print(" Você Foi Reprovado Na Recuperação! ")

    else:
        print(" Você Passou Na Recuperação! ")    
 

