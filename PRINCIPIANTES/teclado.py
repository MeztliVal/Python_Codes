#Leyendo datos del teclado
saludo = input("Escribe tu saludo:")
print("Tu saludo fue:", saludo, " y fue almacenado en modo texto.")


#Leyendo datos segunda parte
decimal=float(input('Introduce un numero CON DECIMALES:'))
decimal *= 3
print(decimal)

#Leyendo datos tercera parte
numero=int(input('Introduce un numero ENTERO:'))
numero *= 3.4
print(numero)

#Leyendo multiples valores cuarta parte
valores=[]
print('\n\nIntroduce 3 valores')
for x in range(3):
    valores.append(input('Teclea un numero:'))
print(valores)

