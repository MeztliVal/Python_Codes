#Primer ciclo while
print('Aprendiendo Ciclos en Python')
c=int(input('Teclea el numero de vueltas del ciclo:'))

while c>0:
    print("C vale:",c)
    c-=1
print('Fin del primer ciclo while')

#Segundo ciclo while
print('\n\n Mezclando lista con Ciclos While')
lista_num=[1,2,3,4,5,6,7,8,9,10]
indice = 0
while indice<len(lista_num):
    print(lista_num[indice])
    indice+=1
print('Fin del Segundo Ciclo While')