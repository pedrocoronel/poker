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
jogos_feitos = "DZ,JJ,QQ,KK,AA", "AA,AA,AA,AA,OO", "QO,OO,SS,SE,DS", "KK,KK,KK,CO,OO", "NE,DZ,SS,SS,DS", "QO,CO,SS,SE,OO", "QO,CO,SS,SE,OO", "QQ,QQ,QQ,SS,SS", "TS,QO,CO,SS,SE", "TS,NE,NE,CO,CO", "QO,SS,KK,OO,TS"
# o que é usado
baralho = ("AA" "DS" "TS" "QO" "CO" "SS" "SE" "OO" "NE" "DZ" "JJ" "QQ" "KK")
mesa = []
suas_cartas = (random.choice(baralho), (random.choice(baralho)))
dealer_cartas = (random.choice(baralho))
# dealer sorteia duas carta do jogador: 1
print("suas cartas:",suas_cartas)
# jogador aposta ou recusa: 0 ou 1
print(mesa)
while True:
    for letra in dealer_cartas:
        if  letra in mesa:
            print(letra, end= " ")
    dealer = input("apostar?(s/n) ")
    if dealer == "n":
        break
    else:
        print(random.choice(baralho))
    mesa.append(dealer)
    if dealer in dealer_cartas:
        print(random.choice(baralho))
        break
    if mesa == jogos_feitos:
        print("game over")
        break
    elif set(dealer_cartas).issubset(set(mesa)):
        print("gg,iz")
        
