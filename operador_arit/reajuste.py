sal = float(input("Qual era o seu salário? R$"))
reajuste = int(input("Digite agora quanto foi o aumento: "))
print("Seu salário de {}, com o reajuste de {}%, será agora de R${:.2f}".format(sal, reajuste, (sal + sal * reajuste/100)))