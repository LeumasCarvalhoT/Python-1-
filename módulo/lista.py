from random import choice
al1 = str(input("Qual o nome do 1º aluno? "))
al2 = str(input("Qual o nome do 2º aluno? "))
al3 = str(input("Qual o nome do 3º aluno? "))
al4 = str(input("Qual o nome do 4º aluno? "))
lista = [al1, al2, al3, al4]
escolhido = choice(lista)
print("O aluno escolhido foi {}".format(escolhido))