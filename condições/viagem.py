kms = int(input('Quanto Kms terá a viagem?: '))

if kms <= 200:
    converção = kms * 0.50
    print('A viagem de {}Kms custará R${:.2f}.'.format(kms, converção))
elif kms > 200:
    converção = kms * 0.45
    print("""Pela sua viagem ter mais de 200Km, daremos
um discontinho, assim ela custará R${:.2f}.""".format(kms, converção))
