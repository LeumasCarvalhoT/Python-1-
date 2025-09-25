
from math import pow, sqrt
CA = float(input("Qual o valor do cateto adjacente?: "))
CO = float(input("Qual o valor do cateto oposto?: "))
Hip = pow(CA, 2) + pow(CO, 2)
Hip = sqrt(Hip)
print("A hipotenusa tem valor de {:.2f}".format(Hip))