print(" ")
'''
o dealer sorteia duas carta do jogador
o jogador aposta uma quantia
o jogador ve se quer continuar
o dealer mostra 3 cartas
o jogador aposta ou desiste
o delaer mostra uma carta
o jogador aposta ou desiste
o deler mostra uma carta
'''
import random 
# apresentação
print(" bem vindo ao")
print("pokerface v1.1")
print(" ")
# baraio
carta = ["[A]","[2]","[3]","[4]","[5]","[6]","[7]","[8]","[9]","[10]","[J]","[Q]","[K]"]
revelada = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J","Q" ,"K"]
# movimentos do dealer
resultado1 = (random.choice(carta))
resultado2 = (resultado1+(random.choice(carta)))
resultado3 = (resultado1 + resultado2 + random.choice(carta))
resultado = []
# dar as cartas ao player
print("suas cartas:",(random.choice(carta)+(random.choice(carta))))
# mostrar a carta
while True:
    print("carta na mesa:",resultado)
    dealer = input("aceitar?")
    if dealer == "n":
        break
# pedaços
