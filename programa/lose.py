#17
suma_decuadrados=0
for sm in range(1,101):
    suma_decuadrados += sm**2
    print(f"{sm} = {suma_decuadrados}")
#18
n=float(input("dame un numero que te lo sumo:"))
suma = sum(n + i for i in range(1, 101))
print("La suma de los 100 números siguientes es:", suma)
#19
euros = float(input("Ingrese cantidad en euros: "))
tipo_cambio = 1.12
dolares=euros*tipo_cambio
print(f"{euros} euros equivalen a {dolares} dólares.")
#20
base_del_rectangulo=float(input("dame el base del rectangulo:"))
altura_del_rectangulo=float(input("dame la altura del rectangulo:"))
area_del_rectangulo= base_del_rectangulo * altura_del_rectangulo
print("el area del rectangulo es", area_del_rectangulo)
#21
numero1=float(input("dame un numero:"))
numero2=float(input("dame otro numero:"))

if numero1 > numero2:
    print("el numero",numero1, "es mayor que el numero",numero2)
if numero1 == numero2:
    print("son iguales")
else:
    print("el numero", numero2,"es mayor que el numero", numero1)



#22
numero = float(input("dame otro numero papi:"))

print("Números impares menores que", numero, ":")
for i in range(int(numero) - 1, -1, -1):
    if i % 2 != 0:
        print(i)

#23
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
print("El MCD es:", mcd(a, b))

#24
import math


a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor b: "))
c = float(input("Ingrese el valor c: "))


discriminante = b**2 - 4*a*c
if a == 0:
    print("No es una ecuación de segundo grado.")
elif discriminante < 0:
    print("La ecuación no tiene soluciones reales.")
elif discriminante == 0:
    x = -b / (2*a)
    print("La ecuación tiene una solución real:", x)
else:
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    print("La ecuación tiene dos soluciones reales:", x1, "y", x2)









