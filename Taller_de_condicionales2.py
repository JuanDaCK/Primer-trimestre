"""Taller condicionales"""

# # # Ejercicios con Condicionales y Operaciones Matemáticas

"""Positivo, negativo o cero."""
# print("Ejercicio 1:")
# numero=int(input("Ingrese un número: "))
# if numero > 0:
#     print("El número ",numero," es positivo.")
# elif numero < 0:
#     print("El número ",numero," es negativo.")
# else:
#     print("El número es 0.")

"""Mayor de dos números ingresados."""
# print("Ejercicio 2:")
# n1=int(input("Ingrese un número: "))
# n2=int(input("Ingrese otro número: "))
# if n1 > n2:
#     print("El número",n1,"es mayor que",n2)
# else:
#     print("El número",n2,"es mayor que ",n1)

"""Par o impar."""
# print("Ejercicio 3:")
# num=int(input("Ingrese un número para determinar sí es par o impar: "))
# if num % 2 == 0:
#     print("El número",num,"es par.")
# else:
#     print("El número",num,"es impar.")    

"""Entre 10 y 20."""
# print("Ejercicio 4:")
# numer=int(input("Ingrese un número: "))
# if numer >= 10 and numer <= 20:
#     print("El número",numer,"está entre el 10 y el 20.")
# else:
#     print("El número",numer,"no está entre el 10 y el 20.")

"""El mayor de 3 números."""
# print("Ejercicio 5:")
# a=int(input("Ingrese su primer número: "))
# b=int(input("Ingrese su segundo número: "))
# c=int(input("Ingrese su tercer número: "))
# if a > b and a > c:
#     print("El núnmero",a,"es el mayor de los tres números.")
# elif b > a and b > c:
#     print("El número",b,"es el mayor de los tres números.")
# elif c > a and c > b:
#     print("El número",c,"es el mayor de los tres números.")

"""Precio final con 10% de descuento."""
# print("Ejercicio 6:")
# prd=input("Ingrese el producto que desea comprar: ")  
# prec=(int(input("Ingrese el precio del producto. Sí es mayor a $100, tiene un 10% de descuento: ")))
# if prec > 100:
#     z=prec*10/100
#     y=prec-z
#     print(f"Su producto tiene un costo de",prec,"y con el descuento, su costo final es de",y)
# else:
#     print(f"Su producto no cuesta más de $100.")

"""Voto de las personas."""
# print("Ejercicio 7:")
# nome=input("Ingrese su nombre: ")
# i=int(input("Ingrese su edad: "))
# if i >= 18:
#     print("Hola",nome,", usted tiene derecho a votar.")
# else:
#     print("Usted no tiene permitido votar.")

"""Descuento a clientes vip."""
# print("Ejercicio 8:")
# print("Bienvenido querido cliente. Nuestro servicio ofrece un descuento del 20% a nuestros miembros vip. Ingrese sus datos a continuación para verificar sí usted tiene membresía")
# k=input("Ingrese su nombre: ")
# l=int(input("Ingrese su documento de identificación: "))
# vip=input("¿Es usted cliente vip?, ingrese Y para decir que si o N para decir que no: ")
# if vip.upper() == "Y":
#     print("¡Gracias por ser parte de nuestros miembros vip!, al ser usted parte de nuestros miebros, le otorgamos un 20% de descuento en nuestro servicio.")
# elif vip.upper() == "N":
#     print("Bienvenido.")
# else:
#     print("Usted ingresó un carácter no válido.")

"""Múltiplo de 5 y de 3."""
# print("Ejercicio 9:")
# ppp=int(input("Ingrese un número: "))
# if ppp % 5 == 0 and ppp % 3 == 0:
#     print("El número",ppp,"es múltiplo de 5 y 3.")
# else:
#     print("El número",ppp,"no es múltiplo de 5 y 3.")

"""Número divisible entre dos números dados."""
# print("Ejercicio 10:")
# numeroo=int(input("Ingrese un número que quiera verificar por cuáles dos números es divisible: "))
# divisor1=int(input("Ingrese el primer divisor: "))
# divisor2=int(input("Ingrese el segundo divisor:" ))
# if numeroo % divisor1 == 0 and numeroo % divisor2 == 0:
#     print("El número",numeroo,"es divisible entre",divisor1,"y",divisor2)
# else:
#     print("El número",numeroo,"no es divisible entre",divisor1,"y",divisor2)

# # # Ejercicios con Listas (con condicionales)

"""Tercer número mayor, menor o igual a 10."""
# print("Ejercicio 11:")
# lista=[2,5,10,9,5]
# print(lista)
# if lista[2] > 10:
#     print("El tercer número que es",lista[2],"es mayor que 10.")
# elif lista[2] < 10:
#     print("El tercer número que es",lista[2],"es menor que 10.")
# else:
#     print("El tercer número que es",lista[2],"es igual a 10.")

"""Número 7 en la lista."""
# print("Ejercicio 12:")
# list=[3,5,7,9]
# print(list)
# if 7 in list:
#     print("El número 7 está en la lista.",list)
# else:
#     print("El número 7 no está en la lista.",list)

"""Suma de los dos primeros elementos de la lista."""
# print("Ejercicio 13:")
# lst=[4,6,2,8]
# print(lst)
# if lst[0] + lst[1] > 10:
#     print("La suma de los dos primeros elementos de la lista es una suma alta")
# else:
#     print("La suma de los dos primeros elementos de la lista es una suma baja")

"""Último nombre de la lista."""
# print("Ejercicio 14:")
# ls=["Ana", "Luis", "Pedro", "Marta"]
# print("El último nombre de la lista es",ls[3])
# if ls[3] == "Marta":
#     print("El nombre es correcto.")
# else:
#     print("El nombre es diferente.")

"""Lista de colores."""
# print("Ejercicio 15:")
# colores=[]
# color1=input("Ingrese un color: ")
# colores.append(color1)
# color2=input("Ingrese un segundo color: ")
# colores.append(color2) 
# color3=input("Ingrese un tercer color: ")
# colores.append(color3)
# print(colores)
# if colores[1] == "azul":
#     color4=input("Ingrese un nuevo color para reemplazar al segundo color en la lista: ")
#     colores2=[color1,color4,color3]
#     print(colores2)
# else:
#     print(colores)

# # # Ejercicios con Tuplas (con condicionales)

"""Primer valor de una tupla dada."""
# print("Ejercicio 16:")
# tpl=(5,8,12,20)
# print(tpl)
# if tpl[0] < tpl[3]:
#     print("El orden de la tupla",tpl,"es ascendente.")
# else:
#     print("El orden de la tupla",tpl,"es descendente.")

"""Segundo valor de una tupla dada."""
# print("Ejercicio 17:")
# tplt=(25,32,28)
# print(tplt)
# if tplt[1] > 30:
#     print("La segunda edad es mayor a 30.")
# else:
#     print("La segunda edad es menor o igual a 30")

"""Tupla convertida a lista."""
# print("Ejercicio 18:")
# tuplaa=(1,2,3)
# print(tuplaa)
# listaa=list(tuplaa)
# print("La tupla",tuplaa,"convertida a lista es:",listaa)
# if listaa[1] == 2:
#     listaa2=[1,10,3]
#     print("La nueva lista viene siendo:",listaa2)
#     tuplaa2=tuple(listaa2)
#     print("La lista 2 convertida a tupla es:"tuplaa2)
# else:
#     print(tuplaa)
    
"""Acceso al segundo valor de una tupla."""
# print("Ejercicio 19:")
# tlk=(4,9)
# print(tlk)
# if tlk[1] > 5:
#     print("La segunda coordenada de",tlk,"es alta.")
# else:
#     print("La segunda coordenada de",tlk,"es baja.")  

"""Comparación de tuplas."""
# print("Ejercicio 20:")
# tupla1=(3,4)
# tupla2=(3,5)
# print("las tuplas son:",tupla1,tupla2)
# if tupla1 == tupla2:
#     print("Las tupla",tupla1,"y la tupla",tupla2,"son diferentes.")
# else:
#     print("Las tuplas son diferentes")

# # # Ejercicios con Diccionarios (con condicionales)

""""""