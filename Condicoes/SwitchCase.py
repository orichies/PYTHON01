# value = 3

# match value:

#     case 1:
#         result = " ONE "

#     case 2:
#         result = " TWO "

#     case 3:
#         result = " THREE "

#     case _:
#         result = " DEFAULT "

# print(result) 


total = 0

escolha = 0

pizza = 0


while escolha != 5:

    print(" C-A-R-D-Á-P-I-O: ")
    print(f" 1 - CALABRESA COM CEBOLA R$30,00 \n "
      f" 2 - FRANGO COM REQUEIJÃO R$35,00 \n "
      f" 3 - CAMARÃO COM CATUPIRY R$40,00 \n "
      f" 4 - BANANA COM CHOCOLATE R$45,00 \n ")  

    escolha = int(input(" ESCOLHA O SABOR DA SUA PIZZA: (DIGITE ENTRE 1 E 4). "))


    match escolha:

        case 1:
            print(" CALABRESA COM CEBOLA R$30,00 ")
            total += 30.00
            pizza += 1

        case 2:
            print(" FRANGO COM REQUEIJÃO R$35,00 ")
            total += 35.00
            pizza += 1

        case 3:
            print(" CAMARÃO COM CATUPIRY R$40,00 ")
            total += 40.00
            pizza += 1

        case 4:
            print(" BANANA COM CHOCOLATE R$45,00 ")
            total += 45.00
            pizza += 1

        case 5:
            print(f" SEU PEDIDO FOI FINALIZADO COM UM TOTAL DE {pizza} PIZZAS, NO VALOR DE R$ {total} Reais. ")
  

        case _:
            print(" ESCOLHA UMA OPÇÃO VÁLIDA! ")    















