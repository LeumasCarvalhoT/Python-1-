lag = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))

print("Sua parede tem a dimensão de {}x{} e sua área é de {}m².".format(lag, alt, lag*alt ))
print("Para pintar a essa parede, você precisará de {}L de tinta.".format(lag*alt/2))