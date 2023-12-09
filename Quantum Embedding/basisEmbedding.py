#Data set
# ds=[[1,0,1,1,1,0],
#     [1,0,0,0,0,1]]
ds=[[3,2],[5,90000],[9,192],[2,4]]

ds2=[]
mb=[]
nc=len(ds)**(1/2)

#máximo de bits por posicion
for i,x in enumerate(ds):
    for j,y in enumerate(x):
        if(i==0):
            mb.append(len(bin(y))-2)
        elif(len(bin(y))-2 >mb[j]):
            mb[j]= len(bin(y))-2
print("\n Maximo bites",mb)

aux1=0
for i,x in enumerate(mb):
    aux1=aux1+mb[i]
print("\n Número de Qubits necesarios", aux1)

#Convertir a binario cada valor
for i,x in enumerate(ds):
    for j,y in enumerate(x):
        aux= bin(y)
        h = aux[2:]
        #validacion de max bits por posicion
        if(len(h)<mb[j]):
            for k in range(mb[j]):
                h= "0"+h
                if(len(h)==mb[j]):break
        ds[i][j]=h
    #Concatenar todos los valores por posicion
    ds2.append("".join(x))

#pasar a int
#for i,x in enumerate(ds2):
    #ds2[i]=int(x)

print('\n', ds2)
import numpy as np
#ds2.shape()


#(ds3=[]
#for i,x in enumerate(ds2):
#    for j,y in enumerate(x):

def binary_string_to_list(binary_string):
    return [int(bit) for bit in binary_string]

Binary_lists = [binary_string_to_list(i) for i in ds2]

print(Binary_lists)
#print(type(Binary_lists))

for i,h in enumerate(Binary_lists):
    0
    #print(i, h)

# Ket vectors in matrix form
ket_0 = np.array([1 + 0j, 0 + 0j])
ket_1 = np.array([0 + 0j, 1 + 0j])

# Input into Matrix form
def transform_input(input_list):
    return [ket_0 if val == 0 else ket_1 for val in input_list]

# Iterate through each binary list and apply the transformation
transformed_results = []
for ket in Binary_lists:
    transformed_vectors = transform_input(ket)
    kronecker_product_result = transformed_vectors[0]
    
    for vector in transformed_vectors[1:]:
        kronecker_product_result = np.kron(kronecker_product_result, vector)
    
    transformed_results.append(kronecker_product_result)

# Print or use the results
#print(len(transformed_results))
suma=0
for i,h in enumerate(transformed_results):
    suma= suma + h

print('\n',suma,"/",nc)

    