velocidade = float(input('Qual a velocidade?: '))
if velocidade > 80:
    print("\033[1;37;41mMulta!!\033[m Você ultrapassou a velocidade maxima de 80km/h! ")
    multa = (velocidade-80)*7
    print('-_-_'*10)
    print ("O valor da multa é {:.2f}".format(multa))
    print('-_-_'*10)
else:
    print("Você esta no limite de velocidade")
