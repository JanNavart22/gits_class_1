import os
os.system("cls")

#"""                   Calculadora

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