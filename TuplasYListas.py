"""Ejercicios de tuplas y listas"""
print("Ejercicio 1:")
tupla=(1,2,3,4,5)
print("el primer elemento de la tupla es:",tupla[0],"el segundo elemento de la lista es:",tupla[4])
print("Ejercicio 2:")
listadnmd=[2.6,6.7,3.1,9.7,9.0]
print("el segundo elemento de la lista de decimales es:",listadnmd[1],"el cuarto elemento de la lista de decimales es",listadnmd[3])
print("Ejercicio 3:")
tpl3=(1,2,3)
fstnm=tpl3[0]
sndnm=tpl3[1]
thrdnm=tpl3[2]
print("los elementos de la tupla son:",fstnm,sndnm,thrdnm)
print("Ejercicio 4:")
listadnme=[5,6,2,9,10]
op=listadnme[0]+listadnme[1]+listadnme[2]+listadnme[3]+listadnme[4]
result=op
print("el resultado de la suma de los elementos de la lista es:",op)
print("Ejercicio 5:")
tplfl=(6.2,4.7,9.0,1.5,7.0)
op1=tplfl[0]+tplfl[1]+tplfl[2]+tplfl[3]+tplfl[4]
op2=op1/5
print("el promedio de los elementos de la tupla de números flotantes es:",op2)
print("Ejercicio 6:")
listaint=[56,98,33,23]
el1=listaint[0]
el2=listaint[1]
el3=listaint[2]
el4=listaint[3]
print("los elementos de la lista de números enteros son:",el1,el2,el3,el4)
print("Ejercicio 7:")
tlpm=(6,87)
oper=tlpm[0]*tlpm[1]
print("el resultado de la multiplicación de los elementos de la tupla es:",oper)
print("Ejercicio 8:")
lst=[56,20,11]
lst.append(98)
print("el primer elemento de la lista es:",lst[0],"el último elemento de la lista es:",lst[3])
print("Ejercicio 9:")
tuppla=(3,5,96,12)
sm=tuppla[0]+tuppla[1]
print("la suma de los primeros dos elementos de la tupla es:",sm)
print("Ejercicio 10")
ls=[20,10,40,50,60]
up=ls[1]-ls[3]
print("la diferencia entre el segundo elemento de la lista y el cuarto es:",up)
print("Ejercicio 11:")
tl=(5,19,3,56,2)
multi=tl[0]*tl[4]
print("el resultado de la multiplicación del primer y último elemento es:",multi)
print("Ejercicio 12:")
llst=[20,2,4]
div=llst[0]/llst[2]
print("el resultado de la división entre el primer número de la lista y el último es:",div)
print("Ejercicio 13")
tllp=(100,435,567,5)
print("el tercer elemento de la tupla es:",tllp[2])
print("Ejercicio 14:")
nmf=[5.6,4.7,3.2,1.7,9.87]
sm=nmf[0]+nmf[1]+nmf[2]+nmf[3]+nmf[4]
print("el resultado de la suma de los elementos de la lista es:",sm)
print("Ejercicio 15")
listaa=[56,57,90,3]
print("la lista convertida en tupla es:",tuple(listaa))
print("Ejercicio 16")
tuplaa=(2,7,10)
listica=list(tuplaa)
listica.append(6)
print("la tupla convertida en lista con el elemento agregado es:",listica)