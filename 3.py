vec=[] 
print("Ingrese número de elementos del vector")
tamaño=int( input())

if 1<=tamaño and tamaño<=200:
    for i in range(1,tamaño+1):
        numero=int( input("Ingrese Entero {0}: ".format(i)))
        vec.append(numero)
    i=0
    
    vector=[]
    for numero in vec:

        if numero not in vector:
                vector.append(numero) 

    vector.sort()

print(vector)