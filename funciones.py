import os

def sumar_2_num():
    num1 = float(input("Ingrese primer número: "))
    num2 = float(input("Ingrese segundo número: "))
    total = num1 + num2
    print("FUNCION: El total es: ",total)


os.system("cls")

print("MENÚ")
print("1. Sumar 2 numeros")
print("2. Restar 2 numeros")
print("3. Multiplicar 2 numeros")
print("4. Dividir 2 numeros")

opc = int(input("Ingrese opción: "))
if opc ==1:
    os.system("cls")
    sumar_2_num()
elif opc==2:
    pass
elif opc ==3:
    pass
else:
    pass
