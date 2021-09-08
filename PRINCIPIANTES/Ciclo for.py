#Primer ciclo for
for i in range(5):
    print(i)

#Segundo ciclo for
print('Segundo Ciclo For')
lista_numeros=[1,2,3,4,5,6,7,8,9,10]
contador = 0
for v1 in lista_numeros:
    lista_numeros[contador]*=10
    contador+=1
print(lista_numeros)
