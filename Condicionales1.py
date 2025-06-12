"""Edad del usuario"""
edad=int(input("Ingrese su edad:"))
if edad>=18:
    print("Usted es un adulto")
else:
    print("Usted es un menor de edad")
"""Múltiples If"""
x=int(input("Ingrese un número: "))
if x > 10:
    print("su número está por encima del 10")
    if x > 20:
        print("su número también está por encima del 20!")
    else:
        print("pero su número no está por encima del 20")
"""Sentencia elif"""
a=int(input("Ingrese un número que quiera multiplicar: "))
b=int(input("Ingrese el número con el que quiere multiplicar el primer número: "))
op=a*b
print("El resultado de su operación es: ",op)
if op==100:
    print("El resultado de su operación es igual a 100")
elif op>100:
    print("El resultado de su operación es una cantidad mayor a 100")
else:
    print("El resultado de su operación es menor a 100")
"""Generaciones digitales"""
año=int(input("Ingrese el año en el que usted nació: "))
if año <= 1940:
    print("Usted pertenece a la generación silenciosa")
elif año <= 1964:
    print("Usted pertenece a la generación de los baby boomers")
elif año <= 1979:
    print("Usted pertenece a la generación X")
elif año <= 2000:
    print("Usted pertenece a la generación Y")
elif año <= 2010:
    print("usted pertenece a la generación Z")
else:
    print("Usted pertenece a la generación de cristal")