import os
os.system("cls")

#---------------------------------------
edad = int(input(" ingrese su edad: "))

if edad >= 18:
    print("es mayor de edad")
else: 
    print("es menor de edad")
    
#---------------------------------------

edad = int(input(" ingrese su edad: "))

if edad >0:
    print("su edad no puede ser negativa")
elif edad < 18 and edad >0:
    print("niños")
elif edad >= 18 and edad <=35: 
    print("pos adolecente")
elif edad >35 and edad <=60:
    print("adulto")
else:
    print("adulto mayor")
    
os.system("pause")

