from random import shuffle
al1 = str(input("Nome do 1º aluno: "))
al2 = str(input("Nome do 2º aluno: "))
al3 = str(input("Nome do 3º aluno: "))
al4 = str(input("Nome do 4º aluno: "))
lista = [al1, al2, al3, al4]
shuffle(lista)

print("A apresentação está organizada: ")
print(lista)