import os
os.system("cls")

        # Conjuntos
        
'''los conjuntos son  grupos de elementos desordenado donde no puede haber duplicados'''
#'''
conjunto = {}  #esto es un diccionario
conjunto = set(conjunto) # este si es un conjunto

conjunto = {1,2,3, 'hola mundo', 5.24} # los conjuntos pueden contener todo tipo de variables

#conjunto = {1,2,3, 'hola mundo', 5.24, [1, 2, 3]} # sin embargo no pueden contener objetos mutables

print(conjunto)

os.system('pause')

print('------------------------')

conjunto.add(5) # con esto puedo agregar un elemento al conjunto (diferente)

conjunto.discard(2) # con este puedo remorer un elemento (existente) no error

#conjunto.remove(2)

print(conjunto)

#print(5 in conjunto) # comprobar elementos del conjunto


#conjunto.clear() # limpar el conjunto
#print(conjunto) 


print('------------------')

print(conjunto.pop()) # regresa un elemento al azar (no estan ordenados)

os.system('pause')

print('--------------------------')
#'''

        # ejemplo
'''
print('vamos a enlistar todos lo apodos de la banda!!!!')
print()

nombre = set({'ique'})      
desicion = input('desea agregar o eliminar apodos (si-no): ')

if desicion == 'si':        
        apodo = input('ingrese apodos, para termina escriba la letra x: '  )
        while apodo != 'x':
                nombre.add(apodo)
                print(nombre)
                apodo = input('apodo: ')
        eliminar = input('desea eliminar apodos (si-no): ')
        if eliminar == 'si':
                apodo = input('ingrese el apodo qe desea eliminar, para termina escriba x: '  )
        while apodo != 'x':
                nombre.discard(apodo)
                print(nombre)
                apodo = input('apodoa a eliminar: ')
        else:
                print(nombre)
else:
        print(nombre)
#'''