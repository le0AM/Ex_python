salario = float(input('Qual o seu salário? R$: '))
if salario >= 1250:
    novo = salario + (salario * 10 / 100)
    print("O seu salario era R${}, e aumentou para R${}".format(salario, novo))
else:
    novo = salario + (salario * 15 / 100)
    print("Seu salario era R${}, aumentou para R$ {}".format(salario, novo))
