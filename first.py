#Se utilizaron las siguientes bibliotecas.
import numpy as np  

#Se pide la dimension de la matriz y se valida que sea mayor o igual a 3
m = int(input("Dimension de la matriz: "))
while m < 3:
    print("Dimension debe ser m>=3")
    m = int(input("Dimensión de la matriz: "))
# Se crea una matriz se llena con ceros al inicio y
# despues se escribe con número primos
matrix = np.zeros((m, m),dtype=int)
num = 2
for i in range(m):
    for j in range(m):
        p=1
        while p:
            prime = True
            for k in range(2, num):
                if num % k == 0:
                    prime = False
            if prime:
                matrix[i][j] = num
                num += 1
                p=0
            else:
                num += 1
               
print("La matriz de primos es:")
ms = str(matrix).replace('[','').replace(']','')
print(ms)

sum = 0
for i in range(m):
    for j in range(i, m):
        sum += matrix[i][j]

print("La suma de la diagonal superior es:", sum)

