#Há duas formas de fazer

vendas_funcionario_um = int(input('Entre com as vendas do funcionário 1: '))
vendas_funcionario_dois = int(input('Entre com as vendas do funcionário 2: '))
vendas_funcionario_tres = int(input('Entre com as vendas do funcionário 3: '))

if vendas_funcionario_um >= 1000:
    if vendas_funcionario_um >= 2000:
        bonus = 0.15 * vendas_funcionario_um
    else:
        bonus = 0.1 * vendas_funcionario_um
else:
    bonus = 0
print('O funcionário 1 ganhou {} de bonus'.format(bonus))

if vendas_funcionario_dois >= 1000:
    if vendas_funcionario_dois >= 2000:
        bonus = 0.15 * vendas_funcionario_dois
elif vendas_funcionario_dois >= 2000:
    bonus = 0.1 * vendas_funcionario_dois
else:
    bonus = 0
print('O funcionário 2 ganhou {} de bônus'.format(bonus))

if vendas_funcionario_tres >= 1000:
    if vendas_funcionario_tres >= 2000:
        bonus = 0.15 * vendas_funcionario_tres
    else:
        bonus = vendas_funcionario_tres * 0.1
else:
    bonus = 0
print('O funcionário 3 ganhou {} de bônus'.format(bonus))

