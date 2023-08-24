import os
os.system("cls")
#---------------------------------------------------------------------------------------------------

''' 1. Escriba un programa que almacene (Input) en una Lista las materias que has cursado con sus respectivas 
notas. Luego muestre la lista por consola mediante un ciclo.'''

'''
print('Vamos a enlistar las materias y sus respectivas notas que usted ha tomado...')
print()

materias = []    
print('ingrese el nombre de la materia y su respectiva nota, al terminar escriba(fin)')
print()
nombre = 0
notas=0

if nombre != 'fin':
    while nombre != 'fin':
        nombre = input('ingrese el nombre de la materia: ')
        if nombre == 'fin':
            break
        else:
            notas = float(input('cuanto saco: '))
            if notas < 0:
                print('la nota no puede ser negativa')
            else:
                materias.append(nombre)
                materias.append(notas)
                print(materias)
else:
     pass
     
print('el listado final de materias es ',materias)    

os.system('pause')
#'''


#---------------------------------------------------------------------------------------------------

'''2. Escriba un programa que almacene personas (input), luego que le muestre 
por pantalla el mensaje de ‘Su nombre es ‘nombre’'''

'''
print('Vamos a enlistar nombres de personas')
print()
print('ingrese el nombre de las personas, al terminar escriba(fin)')

person = []    
nomb_person = 0

while nomb_person != 'fin':
    nomb_person = input('ingrese el nombre: ')
    if nomb_person == 'fin':
            break
    else:
        person.append(nomb_person)
        print(person)
    
for x in person:
    print('su nombre es',[x])    

os.system('pause')
#'''
#---------------------------------------------------------------------------------------------------

'''3. Escribir un programa que guarde en una variable un diccionario con los siguientes valores 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'} Luego pregunte al usuario por una divisa y el valor en pesos a convertir. Luego muestre en consola el 
símbolo con el valor que corresponde a la divisa o un mensaje de advertencia si esa divisa no se encuentra en 
el diccionario.'''
#---------------------------------------------------------------------------------------------------

'''4. En una tupla coloque o ingrese (input) los siguientes valores: números enteros, 
decimales, String, colecciones. Luego muestre en consola que tipo de datos o variable son los valores 
digitados.'''
print('ingrese elementos al azar, al termianr escriba(fin)')
print()

tupla = ()
elemento = 0

while elemento != 'fin':
    tipo = input('que tipo de dato desea ingresar, int, float, str: ')
    if elemento == 'fin' or tipo == 'fin':
            break
    else:
        if tipo == 'int' and tipo != 'fin':
            elemento = int(input('ingrese el elemento: '))
            lista = list(tupla)
            lista.append(int(elemento))
            tupla = tuple(lista)
            print(tupla)
            
        elif tipo == 'float' and tipo != 'fin' :
            elemento = float(input('ingrese el elemento: '))
            lista = list(tupla)
            lista.append(float(elemento))
            tupla = tuple(lista)
            print(tupla)
            
        elif tipo == 'str' and tipo != 'fin':
            elemento = input('ingrese el elemento: ')
            lista = list(tupla)
            lista.append(elemento)
            tupla = tuple(lista)
            print(tupla)
    
print(' estos son sus elementos',tupla)
print('ahora vamos a ver de que tipo son...')

lista = list(tupla)

for z in lista:
    print('---------------')
    print(z,'es un',type(z))
    

os.system('pause')

