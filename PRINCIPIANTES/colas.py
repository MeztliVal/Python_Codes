#importando libreria para interaccion con colas
from collections import deque
#creando una cola
cola = deque (['Hector','Juan','Miguel','Meztli'])
print(cola)
cola.append('Maria')
cola.append('Mario')
print(cola)
k = cola.popleft()
print(k)
print(cola)