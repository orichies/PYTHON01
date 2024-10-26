lista = []

soma = 0

for i in range(10):
   lista.append(int(input(" digite um número: ")))
   soma += lista[i] 

print(f" soma = {soma}, média = {soma /len(lista)} ")