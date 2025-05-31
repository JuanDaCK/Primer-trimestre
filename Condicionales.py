"""Edad del usuario"""
# edad=int(input("Ingrese su edad:"))
# if edad>=18:
#     print("Usted es un adulto")
# else:
#     print("Usted es un menor de edad")
"""Múltiples If"""
# x=int(input("Ingrese un número: "))
# if x > 10:
#     print("su número está por encima del 10")
#     if x > 20:
#         print("su número también está por encima del 20!")
#     else:
#         print("pero su número no está por encima del 20")
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