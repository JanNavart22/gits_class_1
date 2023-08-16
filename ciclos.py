import os
os.system("cls")

#-----------------------------------------------

# ciclo while
"""
control = 1

while control <= 10 :
    print(control)
    control += 1
    
os.system("pause") 
#"""
    
#-------------------------------------------   
 
# arreglos
"""
listado = ["juan", "pedro", "maria", "sofia"]

b=0

while b < len(listado): # "len" el tamaño del vector
    print(listado[b])
    b+=1
    
os.system("pause") 
#"""

#-------------------------------------------------------------------------------------
# ciclo for

"""   
frutas = ["limon", "fresa", "manzana", "pera"]
   
for i in frutas:
    print(i)    

print("----------------------------------")

for a in range(10):
    print(a)    

print("----------------------------------")

for a in range(2, 20, 2):
    print(a)    

print("----------------------------------")

os.system("pause") 
#"""

#-------------------------------------------------------------------------------------
            # taller en clase

#"""
#1. Escriba un programa que almacene la cadena de caracteres contraseña en una 
# variable, para luego preguntarle al usuario por la contraseña. 
#Luego, imprima en la consola si la contraseña que el usuario ingreso coincide con 
# la guardada en variable.   
         
contraseña = 12345

password = int(input("Por favor escriba su contraseña :"))

if contraseña == password:
    print("contraseña CORRECTA!!!!!")

else :
    print("contraseña INCORRECTA")

    
os.system("pause") 
print()
print("--------------------------------------------")
print()

#2. Realice un programa que le pida al usuario dos números por teclado y muestre por 
# consola su división. Si el divisor es cero el programa debe mostrar un error y solicitar
#nuevamente el numero.

x = float((input("Ingrese un numero cualquiera: ")))   
y = float((input("ingrese el numero por el que desea dividirlo: ")))
       
while y == 0: 
    print("el divisor no puede ser 0... ")
    y = float((input("por favor ingrese nuevamente el numero por el que desea dividirlo: ")))
    
print(x,"/",y ," es igual a : ",x/y)


os.system("pause") 
print()
print("--------------------------------------------")
print()

#3. Escriba un programa que le pida al usuario por teclado un numero entero y 
# muestre en consola si es par o impar.   

z = int(input(" ingrese un numero entero cualquiera: "))

if z%2 == 0:
    print(z," es par!!!")
else:
    print(z," es impar!!!")

os.system("pause") 
print()
print("--------------------------------------------")
print()

#4. Escriba que mediante un vector  de 5 item, lea cada item y evalué el ingreso a menores de 
# edad, si la persona tiene menos de 19 años el programa le debe mostrar 
#en pantalla que ¡No puede ingresar!, de caso contrario que le diga ¡Bienvenido!

edades= [13, 15, 21, 14, 19]

for e in edades:
    if e > 19:
        print ("Bienvenido!!!!")
    else:
        print("No puede ingresar...")

os.system("pause") 
#"""
