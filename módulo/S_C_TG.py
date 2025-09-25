import math
ang = int(input("Digite o ângulo: "))
seno = math.sin(math.radians(ang))
print("O valor do SENO com o ângulo de {}° será de {:.2f}".format(ang, seno))

cosseno = math.cos(math.radians(ang))
print("O valor do COSSENO com o ângulo de {}° será de {:.2f} ".format(ang, cosseno))

tangente = math.tan(math.radians(ang))
print("Por último, o valor da TANGENTE com o ângulo de {}° será de {:.2f}".format(ang, tangente))