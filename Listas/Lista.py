frutas = ["maçã", "banana", "cereja"]
frutas.append("melão")
frutas.append("abacaxi")
frutas.sort()
frutas.reverse()

for i in range(len(frutas)):
    if(frutas[i] == "cereja"):
        frutas.pop(i)
        break
print(frutas)        