from random import choice, sample

print("Vamos a jugar al blackjack")

cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}
for carta, valor in cartas.items():
    print(carta, valor)
    lista_cartas = list(cartas.keys())
    print(lista_cartas)
cartan1 = choice(lista_cartas)
cartan2 = choice(lista_cartas)
print("Carta numero 1: ", cartan1)
print("Carta numero 2: ", cartan2)
cartas_jugador = [cartan1, cartan2]
print("Cartas del jugador: ", cartas_jugador)
valor_cartas_jugador = cartas[cartan1] + cartas[cartan2]
print("Valor de las cartas del jugador: ", valor_cartas_jugador)
while valor_cartas_jugador < 21:
    print("¿Quieres otra carta?")
    respuesta = input("Si o No: ")
    if respuesta == "Si":
        cartan = choice(lista_cartas)
        print("Carta numero: ", cartan)
        cartas_jugador.append(cartan)
        print("Cartas del jugador: ", cartas_jugador)
        valor_cartas_jugador += cartas[cartan]
        print("Valor de las cartas del jugador: ", valor_cartas_jugador)
    else:
        break
cartan1mesa = choice(lista_cartas)
cartan2mesa = choice(lista_cartas)
print("Carta numero 1: ", cartan1mesa)
print("Carta numero 2: ", cartan2mesa)
cartas_mesa = [cartan1mesa, cartan2mesa]
print("Cartas de la mesa: ", cartas_mesa)
valor_cartas_mesa = cartas[cartan1mesa] + cartas[cartan2mesa]
print("Valor de las cartas de la mesa: ", valor_cartas_mesa)
if valor_cartas_jugador>valor_cartas_mesa<21:
    print("Has ganado")
elif valor_cartas_jugador<valor_cartas_mesa<21:
    print("Has perdido")
elif valor_cartas_jugador==valor_cartas_mesa:
    print("Empate")


