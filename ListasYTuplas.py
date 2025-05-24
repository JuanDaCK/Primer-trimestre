"""Números ingresados por el usuario"""
print("Por favor, ingrese 10 números a continuación.")
nm1=int(input("Primer número:"))
nm2=int(input("Segundo número:"))
nm3=int(input("Tercer número:"))
nm4=int(input("Cuarto número:"))
nm5=int(input("Quinto número:"))
nm6=int(input("Sexto número:"))
nm7=int(input("Séptimo número:"))
nm8=int(input("Octavo número:"))
nm9=int(input("Noveno número:"))
nm10=int(input("Décimo número:"))
Lista=[nm1,nm2,nm3,nm4,nm5,nm6,nm7,nm8,nm9,nm10]
Tpl1=(nm1,nm1**2)
Tpl2=(nm2,nm2**2)
Tpl3=(nm3,nm3**2)
Tpl4=(nm4,nm4**2)
Tpl5=(nm5,nm5**2)
Tpl6=(nm6,nm6**2)
Tpl7=(nm7,nm7**2)
Tpl8=(nm8,nm8**2)
Tpl9=(nm9,nm9**2)
Tpl10=(nm10,nm10**2)
Lista2=[Tpl1,Tpl2,Tpl3,Tpl4,Tpl5,Tpl6,Tpl7,Tpl8,Tpl9,Tpl10]
st=nm1+nm2+nm3+nm4+nm5+nm6+nm7+nm8+nm9+nm10
pm=st/10
ds=st*2
mp=pm/2
Lista3=[nm1**nm7,nm3+nm9,nm4*nm5,nm10/nm2,nm8-nm6]
print("Los números que ingresaste son:",Lista)
print("Los números con sus cuadrados son:",Lista2)
print("El resultado de la suma de los números que ingresaste es:",st)
print("El promedio de los números es:",pm)
print("El doble de la suma de los números es:",ds)
print("La mitad del promedio de los números es",mp)