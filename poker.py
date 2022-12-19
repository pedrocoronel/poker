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
print("pokerface v1.0")
print(" ")
# baraio
carta1 = ["[A]","[2]","[3]","[4]","[5]","[6]","[7]","[8]","[9]","[10]","[J]","[Q]","[K]"]
carta2 = ["[A]","[2]","[3]","[4]","[5]","[6]","[7]","[8]","[9]","[10]","[J]","[Q]","[K]"]
carta3 = ["[A]","[2]","[3]","[4]","[5]","[6]","[7]","[8]","[9]","[10]","[J]","[Q]","[K]"]
# movimentos do dealer
resultado = carta1, carta2, carta3
# dar as cartas ao player
print("suas cartas")
print(random.choice(carta1)+(random.choice(carta2)))
# mostrar primeira carta
dealer = input("aceitar?")
if dealer == "n":
    print("reinicie o programa!")
else:
    print(random.choice(carta1))
# mostrar segunda carta
dealer = input("aceitar?")
if dealer == "n":
    print("perdeu na segunda rodada!")
else:
    print(random.choice(carta2)+(random.choice(carta1)))
# mostrar terceira carta
dealer = input("aceitar?")
if dealer == "n":
    print("perdeu na terceira rodada rodada!")
else:
    print((random.choice(carta3))+(random.choice(carta2))+(random.choice(carta1)))
print("end game!")