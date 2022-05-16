faixa_1 = 0000.00
faixa_2 = 1903.99
faixa_3 = 2826.66
faixa_4 = 3751.06
faixa_5 = 4664.69

while True:
    salario_bruto = float(input('Entre com o salário do funcionário: '))
    if faixa_1 <= salario_bruto < faixa_2:
        imposto = 0
        salario_liquido = salario_bruto - imposto
        print('O salário liquido (R$): {} e o imposto (R$): {}'.format(salario_liquido, imposto))
    elif faixa_2 <= salario_bruto < faixa_3:
        imposto = ((salario_bruto - faixa_2) * 0.075)
        salario_liquido = salario_bruto - imposto
        print('O salario liquido (R$): {:.2f} e o imposto (R$): {:.2f}'.format(salario_liquido, imposto))
    elif faixa_3 <= salario_bruto < faixa_4:
        imposto = ((faixa_3 - faixa_2) * 0.075) + ((salario_bruto - faixa_3) * 0.150)
        salario_liquido = salario_bruto - imposto
        print('O salario liquido1 (R$): {:.2f} e o imposto (R$): {:.2f}'.format(salario_liquido, imposto))
    elif faixa_4 <= salario_bruto < faixa_5:
        imposto = ((faixa_3 - faixa_2) * 0.075) + ((faixa_4 - faixa_3) * 0.150) + ((salario_bruto - faixa_4) * 0.225)
        salario_liquido = salario_bruto - imposto
        print('O salario liquido (R$): {:.2f} e o imposto (R$): {:.2f}'.format(salario_liquido, imposto))
    else:
        imposto = ((faixa_3 - faixa_2) * 0.075) + ((faixa_4 - faixa_3) * 0.150) + ((faixa_5 - faixa_4) * 0.225) + ((salario_bruto - faixa_5) * 0.275)
        salario_liquido = salario_bruto - imposto
        print('O salario liquido (R$): {:.2f} e o imposto (R$): {:.2f}'.format(salario_liquido, imposto))
    continuar = int(input('Deseja continuar?\n1 - Sim\n0 - Não\n>>'))
    if continuar == 0:
        break