distancia = float(input('Qual a distancia da viagem?: '))
print("Você vai fazer uma viagem de {:.2f}km".format(distancia))
if distancia > 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print("O preço da viagem vai ser R${:.2f}".format(preco))
