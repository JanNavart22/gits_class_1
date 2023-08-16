import os
os.system("cls")

#-----------------------------------------------------------------------

#"""                   Calculadora
print()
print("Programa de suma, resta, multiplicacion, division y exponente    ") 
print()

x = float((input("Ingrese un numero cualquiera: ")))   
y = float((input("ingrese otro numero cualquiera: ")))

print(x,"+",y ," es igual a : ",x+y)
print(x,"-",y ," es igual a : ",x-y)
print(x,"*",y ," es igual a : ",x*y)
print(x,"/",y ," es igual a : ",x/y)
print(x,"modulo",y ," es igual a : ",x%y)
print(x,"expo",y ," es igual a : ",x**y)

os.system("pause")

#"""

#"""                   Calculadora con decisiones

print()
print("Programa de suma, resta, multiplicacion y division   ") 
print()
print("ADVERTENCIA!!!!")
print("por favor en la parte de operacion","ingrese +  -  *  /   conforme lo que desea hacer")
print()

x = float((input("Ingrese un numero cualquiera: ")))   
y = input("operacion : ")
z = float((input("ingrese otro numero cualquiera: ")))

if y == "+":
    print(x,"+",z ," es igual a : ",x+z)
elif y == "-":
    print(x,"-",z ," es igual a : ",x-z)
elif y == "*":
    print(x,"*",z ," es igual a : ",x*z)
elif y == "/":
    if z>0 :
        print(x,"/",z ," es igual a : ",x/z)
        print("Y el modulo es: ",x%z)
    else:
        print(" no se puede dividir entre 0")
else:
    print("especificacion de operacion incorrecta, intentelo nuevamente.")      
          
          
os.system("pause")

#"""