print("Sistema de calificación:")
print("Ingrese los siguientes datos a continuación para poder calcular sus notas")
nombre=input("Ingrese su nombre completo: ")
grado=input("Ingrese su grado: ")
ti=int(input("Ingrese su documento de identidad:"))
notam=float(input("Ingrese la nota mínima requerida para aprobar: "))
print(f"A continuación, ingrese sus notas: ")
print("Matemáticas: ")
mat1=float(input("Ingrese su primera nota de matemáticas: "))
mat2=float(input("Ingrese su segunda nota de matemáticas: "))
mat3=float(input("Ingrese su tercera nota de matemáticas: "))
suma=mat1+mat2+mat3
prmat=suma/3
print("El promedio de tu nota de matemátias es: ",prmat)
print("Usted aprobó matemáticas?", prmat>=notam)
print("Ingrese sus notas de español:")
esp1=float(input("Ingrese su primera nota de español: "))
esp2=float(input("Ingrese su segunda nota de español: "))
esp3=float(input("Ingrese su tercera nota de español: "))
suma2=esp1+esp2+esp3
pres=suma2/3
print("El promedio de tu nota de español es: ",pres)
print("Usted aprobó español?", pres>=notam)
print("Ingrese sus notas de inglés: ")
ing1=float(input("Ingrese su primera nota de inglés: "))
ing2=float(input("Ingrese su segunda nota de inglés: "))
ing3=float(input("Ingrese su tercera nota de inglés: "))
suma3=ing1+ing2+ing3
pring=suma3/3
print("El promedio de su nota de inglés es: ",pring)
print("Usted aprobó inglés?", pring>=notam)
print("Ingrese sus notas de biología: ")
bio1=float(input("Ingrese su primera nota de biologia: "))
bio2=float(input("Ingrese su segunda nota de biología: "))
bio3=float(input("Ingrese su tercera nota de biología: "))
sumabio=bio1+bio2+bio3
prbio=sumabio/3
print("El promedio de su nota de biología es: ",prbio)
print("Usted aprobó biología? ",prbio>=notam)
print("Ingrese sus notas de física:")
fis1=float(input("Ingrese su primera nota de física: "))
fis2=float(input("Ingrese su segunda nota de física: "))
fis3=float(input("Ingrese su tercera nota de física: "))
sumafis=fis1+fis2+fis3
prfis=sumafis/3
print("El promedio de su nota de física: ",prfis)
print("Usteda aprobó sociales?", prfis>=notam)
print("Ahora, comprobemos si aprobó el grado:")
sumapromedios=prmat+pres+pring+prbio+prfis
promediototal=sumapromedios/5
print("El promedio de tus notas fue de: ",promediototal)
print(f"El estudiante aprobó el grado? ",promediototal>=notam)
