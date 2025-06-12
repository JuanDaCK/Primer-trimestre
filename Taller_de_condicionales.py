"""Ejercicio 1"""
# print("Crédito bancario:")
# Nombre=input("Ingrese su nombre: ")
# Edad=int(input("Ingrese su edad: "))
# if Edad>=18:
#     Msg1=('Bienvenido ',Nombre,' Ingrese los datos de su cuenta para acceder a su crédito bancario.')
#     print(Msg1)
#     Msg2=(int(input('Ingrese su cédula de ciudadanía: ')))
#     Msg3=(int(input('Ingrese el código con el que accede a su cuenta: ')))
#     Msg4=(int(input('Ingrese el monto que desea retirar: ')))
#     Msg5=('¡Todo listo ',Nombre,'!',' Ya puede retirar el monto de ',Msg4,', gracias por usar nuestro servicio y vuelva pronto.')
#     print(Msg5)
# else:
#     print('Usted no tiene permiso para usar nuestro servicio.')
"""Ejercicio 2"""
# print("Zona de juegos:")
# Nombre=input("Ingrese su nombre: ")
# Msg=("Hola ",Nombre," gracias por usar nuestro servicio para su entretenimiento.")
# print(Msg)
# Edad=int(input("Porfavor, ingrese su edad para continuar: "))
# if Edad < 4:
#     print("Usted puede entrar gratis.")
# elif Edad <= 18:
#     print("Usted debe pagar 5 Euros para poder ingresar.")
# else:
#     print("Usted debe pagar 18 Euros para poder ingresar.")
"""Ejercicio 3"""
print("Calculadora:")
print("Menú:")
print("Suma = S")
print("Resta = R")
print("Multiplicación = M")
print("División = D")
Operacion=input("Ingrese el tipo de operación que quiere realizar: ")
if Operacion.upper() == "S":
    Nm1=int(input("lngrese el primer número: "))
    Nm2=int(input("Ingrese el segundo número:"))
    op=Nm1+Nm2
    print(f"El resultado de la suma es: ",op)
elif Operacion.upper() == "R":
    Num1=int(input("lngrese el primer número: "))
    Num2=int(input("Ingrese el segundo número:"))
    ope=Num1-Num2
    print(f"El resultado de la resta es: ",ope)
elif Operacion.upper() == "M":
    Numero1=int(input("lngrese el primer número: "))
    Numero2=int(input("Ingrese el segundo número:"))
    oper=Numero1*Numero2
    print(f"El resultado de la multiplicación es: ",oper)
elif Operacion.upper() == "D":
    Number1=int(input("lngrese el primer número: "))
    Number2=int(input("Ingrese el segundo número:"))
    opera=Number1/Number2
    print(f"El resultado de la división es: ",opera)
else:
    print("Usted ingresó un carácter no válido.")