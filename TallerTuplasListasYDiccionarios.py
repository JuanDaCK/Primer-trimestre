# """Registro simple de producto y cálculo de costos"""
# print("Taller 1:")
# pr=input("Ingrese el nombre del producto que desea comprar:")
# pru=float(input("Ingrese el precio unitario del producto:"))
# cc=int(input("INgrese la cantidad de producto que desea comprar:"))
# tpl=(pr,pru)
# lst=[tpl,cc]
# dicc={
#     "producto":lst
# }
# op=pru*cc
# print("La información sobre su compra es:",dicc)
# print("El costo total de su compra es:",op)
# """Factura de múltiples productos"""
# print("Taller 2:")
# pr1n=input("Ingrese el nombre del primer producto que desea comprar:")
# pr1p=float(input("Ingrese el precio unitario del producto:"))
# pr1c=int(input("Ingrese la cantidad de producto que desea comprar:"))
# pr2n=input("Ingrese el nombre del segundo producto que desea comprar:")
# pr2p=float(input("Ingrese el precio unitario del producto:"))
# pr2c=int(input("Ingrese la cantidad de producto que desea comprar:"))
# pr3n=input("Ingrese el nombre del tercer producto que desea comprar:")
# pr3p=float(input("Ingrese el precio unitario del producto:"))
# pr3c=int(input("Ingrese la cantidad de producto que desea comprar:"))
# tp1=(pr1n,pr1p)
# tp2=(pr2n,pr2p)
# tp3=(pr3n,pr3p)
# ls1=[tp1,pr1c]
# ls2=[tp2,pr2c]
# ls3=[tp3,pr3c]
# diccionario={
#     "producto 1":ls1,
#     "producto 2":ls2,
#     "producto 3":ls3
# }
# pr1t=pr1p*pr1c
# pr2t=pr2p*pr2c
# pr3t=pr3p*pr3c
# totalg=pr1t+pr2t+pr3t
# print("La información de los productos que desea comprar es:",diccionario)
# print("El precio total del producto 1 es:",pr1t)
# print("El precio total del producto 2 es:",pr2t)
# print("El precio total del producto 3 es:",pr3t)
# print("El costo general de su compra es:",totalg)
# print("Gracias por su compra :)")
"""Registro de notas de un estudiante"""
print("Taller 3:")
nombre=(input("Ingrese su nombre:"))
materia1=(input("Ingrese la primera asignatura que cursa:"))
materia2=(input("Ingrese la segunda asignatura que cursa:"))
materia3=(input("Ingrese la tercera asignatura que cursa:"))
nota1m1=(float(input("Ingrese la primera nota de "+materia1+" a continuación:")))
nota2m1=(float(input("Ingrese la segunda nota de "+materia1+" a continuación:")))
nota1m2=(float(input("Ingrese la primera nota de "+materia2+" a continuación:")))
nota2m2=(float(input("Ingrese la segunda nota de "+materia2+" a continuación:")))
nota1m3=(float(input("Ingrese la primera nota de "+materia3+" a continuación:")))
nota2m3=(float(input("Ingrese la segunda nota de "+materia3+" a continuación:")))
sm1=nota1m1+nota2m1
sm2=nota1m2+nota2m2
sm3=nota1m3+nota2m3
pr1=sm1/2
pr2=sm2/2
pr3=sm3/2
tpl1=(materia1,pr1)
tpl2=(materia2,pr2)
tpl3=(materia3,pr3)
lst1=[tpl1,nota1m1,nota2m1]
lst2=[tpl2,nota1m2,nota2m2]
lst3=[tpl3,nota1m3,nota2m3]
diccionario={
    "nombre":nombre,
    "materia":[lst1,lst2,lst3]
}
prtotal=pr1+pr2+pr3
print(nombre," las materias que usted cursó, sus promedios y notas son:",lst1,lst2,lst3," su promedio total entre las tres materias es: ",prtotal)