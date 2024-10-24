sim = 0

a = input(" TELEFONOU PARA A VÍTIMA? (S / N) : ")
if a == "S" :
    sim += 1

b = input(" ESTEVE NO LOCAL DO CRIME? (S / N) : ")
if b == "S":
    sim += 1


c = input(" MORA PERTO DA VÍTIMA? (S / N) : ")
if c == "S":
    sim += 1


d = input(" DEVIA PARA A VÍTIMA? (S / N) : ")
if d == "S":
    sim += 1


e = input(" JÁ TRABALHOU COM A VÍTIMA? (S / N) : ")
if e == "S":
    sim += 1

if sim < 2:
    print(" VOCÊ FOI INOCENTADO! ")

elif sim == 2:
    print(" VOCÊ FOI CONSIDERADO SUSPEITO! ")

elif sim == 3 or sim == 4:
    print(" VOCÊ FOI CONSIDERADO CÚMPLICE! ")

else:
    print(" VOCÊ É O ASSASSINO! ")    




    
    


