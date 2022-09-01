from random import randint
computador = randint(0,5)
print("-_-_"*15)
print("Vou pensar em um numero entre 0 e 5, tente acertar")
print("-_-_"*15)
jogador = int(input("Que numero eu pensei?: "))
print("pensei em um numero... {}".format(computador))
if jogador == computador:
    print("\033[1;37;42mVocê acertou!!\033[m")
else:
    print("\033[1;37;41mVocê errou, tente novamente!\033[m")

