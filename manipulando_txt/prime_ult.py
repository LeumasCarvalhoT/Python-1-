oraçao = str(input('Digite um frase: ')).lower().strip()
print("A letra 'A' aparece {} vezes na frase.".format(oraçao.count('a')))
print("A primeira letra 'A' apareceu na posição {}.".format(oraçao.find('a')+ 1))
print("A última letra 'A' apareceu na posição {}.".format(oraçao.rfind('a')+ 1))