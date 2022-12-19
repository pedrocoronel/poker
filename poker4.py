print(" ")
'''
o jogo se inicia: 1

o dealer sorteia duas carta do jogador: 1
o dealer mostra as cartas do jogador: 1
o jogador aposta ou recusa: 0 ou 1
o dealer mostra 3 cartas: 1
o jogador aposta ou recusa: 0 ou 1
o dealer mostra 3 cartas: 1
o jogador aposta ou recusa: 0 ou 1
o dealer mostra 3 cartas: 1
'''
import random 
# apresentação
print(" bem vindo ao")
print("pokerface v1.2")
print(" ")
# jogos para ganhar o game
jogos_feitos = ["DZ JJ QQ KK AA", "AA AA AA AA OO", "QO OO SS SE DS", "KK KK KK CO OO", "NE DZ SS SS DS", "QO CO SS SE OO", "QO CO SS SE OO", "QQ QQ QQ SS SS", "TS QO CO SS SE", "TS NE NE CO CO", "QO SS KK OO TS"]
# o que é usado
baralho = ("AA", "DS", "TS", "QO", "CO", "SS", "SE", "OO", "NE", "DZ", "JJ", "QQ", "KK")
mesa = []
suas_cartas = (random.choice(baralho)), (random.choice(baralho))
oponente_cartas = (random.choice(baralho)), (random.choice(baralho))
# jogador aposta ou recusa: 0 ou 1
while True:
    print("suas cartas:",suas_cartas)
    print("oponente:",oponente_cartas)
    print("cartas na mesa:",mesa)
    dealer = input("apostar?")
    if dealer == "n":
        break
    elif dealer: 
        print(random.choice(baralho) in mesa)