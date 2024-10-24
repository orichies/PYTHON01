Peso = float(input( "Digite Seu Peso: "))

Altura = float(input( "Digite Sua Altura: "))

Imc = Peso / (Altura*Altura)

if Imc > 25:
    print(f" Acima do Peso Ideal! ")

else:
    print(f" Peso OK! ")

