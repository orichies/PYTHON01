#construa um programa onde o usuario digitará 7 numeros e o programa escreverá na tela quantos são pares e quantos são impares

numeros = []
par = 0
impar = 0

for i in range(7):
    numeros.append(int(input(" digite um numero: ")))
    if numeros[i] % 2 == 0:
       par += 1

    else:
       impar += 1

print(f"números pares: {par}\n"
      f"números ímpares: {impar} \n ")

