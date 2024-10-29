a = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]

sim = 0

for i in range(5):
    resposta = input(a[i])

    if resposta.lower() == "sim":
        sim += 1


if sim < 2:
    print(" VOCÊ FOI INOCENTADO! ")

elif sim == 2:
    print(" VOCÊ FOI CONSIDERADO SUSPEITO! ")

elif sim == 3 or sim == 4:
    print(" VOCÊ FOI CONSIDERADO CÚMPLICE! ")

else:
    print(" VOCÊ É O ASSASSINO! ")          
    
