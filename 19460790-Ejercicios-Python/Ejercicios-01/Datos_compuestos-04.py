"""
mano = (1, 2, 1, 4, 1)


def poker(mano):
    contador = 0
    for i in mano:
        if i == mano[i]:
            contador += 1
        
    print(contador)


poker(mano)
"""

mano = ('4h', '5s', 'Ad', '4p', '4s')
def poker(mano):
    #tupla = mano
    counter = 0
    counter2 = 0
    
    for i in range(5):
        carta = mano[i][0]
        for j in range(counter2, 5):
            if carta == mano[j][0]:
                counter += 1
        if counter == 4:
            return "Tienes un Poker"
        else:
            return "No tienes poker"

        counter = 0
        counter2 += 1

print(poker(mano))