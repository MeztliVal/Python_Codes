#EJEMPLO DE LISTA EN PYTHON
autor = ["meztli", "valeriano", "orozco", 37, 2878751044, "c"]
contador = 0
for lugar in autor:
    print(autor[contador])
    contador+=1
    
#EJEMPLO DE DICCIONARIO
colores = {'amarillo':'yellow', 'azul':'blue', 'verde':'green', 'negro':'black'}
print(colores)
print(colores['azul'])

directorio = {'nombre':'meztli', 'paterno':'valeriano','edad':'37','tel':'2878751044'}
print(directorio)
print(directorio['nombre'])
print(directorio['tel'])

numeros = {10:'diez',20:'veinte',30:'treinta'}
print(numeros[20])
print(numeros)

edades={'meztli':37, 'ana':22,'marco':21,'bladimir':18, 'alejandro':19, 'jesus':21, 'karina':19, 'hector':19, 'javier':19, 'fortino':19, 'america':19,'crystal':23,'miguel':19,'angel':19}
print(edades['alejandro'])
edades['jesus']+=20
print(edades['jesus'])
print(edades['bladimir']+edades['meztli']+edades['crystal'])