print("hola ya se imprimir")
numero=273
print(numero)
numero_decimal=3,5
print(numero_decimal)
suma= 1234+532
print(suma)
resta=1234-532
print(resta)
multiplicacion=1234*532
print(multiplicacion)
division=1234/532
print(division)
numero_1=1
#numeros del 1 a 3
while numero_1<=3:
    print(numero_1)
    numero_1=numero_1+1
#numeros del 1 al 9
numero_2=1
while numero_2<=9:
    print(numero_2)
    numero_2=numero_2+1
#numeros del 1 al 10k
for x in range(1,10001):
    print(x)
#numeros del 5 al 10
for y in range(5,11):
    print(y)
#numeros del 5 al 15
for z in range(5,16):
    print(z)
#numeros del 5 al 15k
for q in range(5,15001):
    print(q)
#hola 200 veces
a=0
while a<= 200:
    print("hola")
    a=a+1
for m in range(1,31):
   cuadrado= m ** 2
   print(f"{m}={ cuadrado}")
#multiplicacion de los primerpos 20 numeros
resultado=1
for g in range (1,21):
    resultado *= g
    print(resultado)
#sumar los cuadrados de los primeros 100 numeros
suma_decuadrados=0
for sm in range(1,101):
    suma_decuadrados += sm**2
    print(f"{sm} = {suma_decuadrados}")
#cambair de euros a dolares
dinero_en_euros = 5.5
cambio_a_dolares = dinero_en_euros * 1.10
print(cambio_a_dolares)

# hasta aqui ta la tarea
#ya llevo 2 horas y mas errrores que programas xd (ayuda)
#hallar el area de un rectangulo
altura_de_rectamgulo=6.6
ancho_del_rectangulo=5.6
area=altura_de_rectamgulo * ancho_del_rectangulo
print(area)
#decir cual es mayor 
num1=12
num2=15
if num1<num2:
     print(f"El número mayor es {num2} y el número menor es {num1}.")

#.. imprimir un numero entero y los numeros impares menores que el
numero_entero=17
print(numero_entero)
for i in range(numero_entero):
    if i % 2 !=0:
        print(i)