#Aprendiendo Ciclos While en Python
print("Aprendiendo Ciclos While con Python")
c=int(input('Teclea el numero de vueltas del ciclo:'))
while c>0:
    print("C es igual a ",c)
    c-=1      # c = c-1
print("Fin del primer ciclo while")

#Segunda prueba con ciclo While
print("\n\n Mezclando Ciclos con Listas")
lista_num=[1,2,3,4,5,6,7,8,9,10,11]
indice = 0
while indice < len(lista_num):
    print(lista_num[indice])
    indice+=2