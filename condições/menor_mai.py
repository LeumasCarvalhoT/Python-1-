n1 = int(input('Primeiro: '))
n2 = int(input('Segundo: '))
n3 = int(input('Terceiro: '))
menor = n1
maior = n1

#MENOR
if n2<n1 and n2<n3:
    menor = n2
if n3<n2 and n3<n1:
    menor = n3
#MAIOR
if n2>n1 and n2>n3:
    maior = n2
if n3>n2 and n3>n1:
    maior = n3

print('O número menor foi {}'.format(menor))
print('O número maior foi {}'.format(maior))
#numeros = [n1, n2, n3]
#print('O menor número foi {}'.format(min(numeros)))
#print('O maior número foi {}'.format(max(numeros)))