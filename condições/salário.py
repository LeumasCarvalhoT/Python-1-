sal = float(input('Informe seu salário: '))
if sal <= 1250.00:
    novo = sal + sal * 15/100
elif sal > 1250.00:
    novo = sal + sal * 10/100 
print('O salário que era {}, agora passará a ser {}'.format(sal, novo))