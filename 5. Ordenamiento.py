if ((a - b) == 2 and (b == 5)):
    print("Gano el jugador A")
elif((b - a) == 2 and ( a == 5)):
    print("Gano el jugador B")
elif((b - a) <= 1 and ((a < 7) and (b < 7))):
    print("Aun no termina")
elif(a == 7 and b >= 5):
    print("Gano el jugador A")
elif(b == 7 and a>=5):
    print("Gamno el jugador B")
else:
    print("Invalido")
    