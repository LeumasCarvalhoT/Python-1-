from time import sleep

vel = int(input('Qual a velocidade atual do carro?: '))
print('Sendo 80Km/h o limite de velocidade...')
sleep(1)

if vel <= 80:
    print('\033[32mSem ultrapassagem de velocidade.' \
    ' Tenha um bom dia.\033[m')
elif (vel > 80) and (vel <= 96):
    print('\033[4;31mMULTADO!\033[m, \033[31mcom a passagem de velocidade média, você receberá' \
    ' uma multa R$130,16\033[m')
elif (vel > 96) and (vel <= 120):
    print('\033[4;31mMULTADO!\033[m, \033[31mcom a passagem de velocidade grave, você receberá' \
    ' uma multa R$195,23\033[m')
elif vel > 120:
    print('\033[4;31m MULTADO!\033[m, \033[31mcom a passagem de velocidade gravíssima, você receberá' \
    ' uma multa R$880,41\033[m')


