Salario = int(input(" Digite O Valor Do Seu Salário: "))

Desc_Vale = Salario * 0.06
Desc_Saude = Salario * 0.03

print(f" O Valor Do Desconto Do Vale-Transporte é de: R$ {Desc_Vale} \n "
      f" O Valor Do Desconto Do Plano de Saúde é de: R$ {Desc_Saude} \n "
      f" O Seu Novo Salário é de: R$ {Salario - Desc_Vale - Desc_Saude} \n ")

