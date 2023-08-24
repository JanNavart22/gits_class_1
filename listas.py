import os
os.system("cls")

#-------------------------------------------------------------------------------------

        # listas 

"""
varLista = ['hector', True, 5.5, 9]

print(varLista[-1])
print(varLista[0])
print(varLista[1])
print(varLista[2])
print(varLista[3])

print('-----------------------------')

for z in varLista:
    print(z)
    
print('-----------------------------')

q = 0

while q < len(varLista):
    print(varLista[q])
    q+=1
    
print('-----------------------------')

del varLista[0]

for z in varLista:
    print(z)

print('-----------------------------') 

varLista.insert(1,'cual?')

for z in varLista:
    print(z)
    
print('-----------------------------') 

varLista.append('USCO')

for z in varLista:
    print(z)
    
print('-----------------------------') 

varLista.append(input('ingrese la ciudad: '))

for z in varLista:
    print(z)
 
print('-----------------------------') 

eliminar = input('ingrese el valor que desea eliminar: ')

contador = 0

for z in varLista:
    if eliminar == z:
        del varLista[contador]
    else:
        contador += 1
        
print(varLista)
   
os.system("pause") 
#"""

#-------------------------------------------------------------------------------------

            # lista dentro de otra lista

#"""

datos = [['hecto', 'sanchez', 36], ['maria', 'lugo', 28], ['juan', 'silva', 17]]

print(datos[1])
print(datos[1][2])

print('--------------------------')

for z in datos:
    print(z)

print('----------------------')
    
for z in datos:
    for u in z:
        print(u)
    print('------------')
 
 
os.system("pause") 
#"""


