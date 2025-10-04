#from colorama import init, Fore, Back, Style
#init()
import random
from time import sleep

Nrandom = random.randint(0, 5)
print('-+-' * 20 )
print(' Tente adivinhar um número entre 0 e 5 que estou pensando.')
print('-+-' * 20)

num = int(input('Em que número eu pensei?: '))
print('PROCESSANDO...')
sleep(2)
if num == Nrandom:
    print('PARABÉNS!!, acertastes miseravi, pensei mesmo em {}.'.format(num))
else:
    print('ERRASTIS, tente novamente na proxima, o número pensado foi {}.'.format(Nrandom))
