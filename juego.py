import random
res = int(input('En que numero estoy pensando?'))
print('Numero pensado', res, "\n\n")
cont = 0
while True:
    cont += 1
    ran = random.randint(1, 10)
    print('random', ran)
    if ran == res:
        break
    if cont == 3:
        print('Game Over...muchos intentos..')
        break
print("Felicitaciones..Ganaste...se ha adivinado el numero ", res)
