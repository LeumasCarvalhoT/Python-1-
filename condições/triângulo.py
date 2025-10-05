l1 = int(input('Primeiro lado: '))
l2 = int(input('Segundo lado: '))
l3 = int(input('Terceiro lado: '))
if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l2 + l1):
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')
