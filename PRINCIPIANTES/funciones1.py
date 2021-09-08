#Funciones en Python
def saludo():        #Definición de la función
    print("Hola estas imprimiendo desde una funcion")
    
saludo()

#Funcion2
def dibuja_tabla5():
    print("==== Calculando Tabla del 5 ==== \n")
    for i in range(10):
        print("5 X ",i+1," = ",(i+1)*5)
        
dibuja_tabla5()
    
#Funcion3
def suma(a,b):
    return a+b

r = suma(5,2)
print("Imprimiendo el resultado de la suma")
print(r)
