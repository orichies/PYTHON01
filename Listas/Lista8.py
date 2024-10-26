numeros = []
contador = 0

for i in range(10):
    numeros.append(int(input(" digite um numero: ")))
    if numeros[i] > 10:
        contador += 1
        print(numeros[i])
print(contador)        