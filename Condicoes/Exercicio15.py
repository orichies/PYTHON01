Nota1 = float(input( " Digite a Primeira Nota: "))

Nota2 = float(input( " Digite a Segunda Nota: "))

Nota3 = float(input( " Digite a Terceira Nota: "))

Nota4 = float(input( " Digite a Quarta Nota: "))

media = Nota1 + Nota2 + Nota3 + Nota4 / 4

if(media < 6):
    print(f" Você Foi Reprovado! Com media: {media} ")

else:
    print(f" Você Está Aprovado! Com media: {media} ")    