prod = float(input("Qual o valor do produto? R$"))
desc = float(input("Agora o valor do desconto: "))

print("O produto com valor R${} com desconto de {}% vai custar R${:.2f}.".format(prod, desc, (prod - prod * desc/100)))