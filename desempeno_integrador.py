#Programa para saber el agua que se utiliza en el hogar
print("         Bienvenido al programa sobre el uso y consumo del agua", "\n")
nombre=input("¿Cuál es su nombre: ")
if nombre==("Manuel"):
    nombre=("Manuel")
else:
    print("Usuario no identificado, se le asignarà uno")
    nombre=("Usuario")
print("\n")
print("Bienvenido", nombre)
print("\n")
n=int(input("¿En cuantos procesos utiliza el agua: "))
print("\n")
uso_de_agua=[]
for i in range(n):
    print("Repuesta ",i+1)
    uso_de_agua.append(input("¿En qué utiliza el agua en su hogar: "))   
print("\n")
pre0=input("¿Desea agregar una nueva respuesta: ")
if pre0==("si"):
    uso_de_agua.append(input(("Ingrese su nueva respuesta: ")))
else:
    print(  "**Mostrar lista**")
print(uso_de_agua, "\n")
print("Ahora que sabemos en que se utiliza, hay que saber el consumo en Litros (Diario)")
p1=input("¿Conoce su consumo real: ")
consum=int(0)
while p1:
    if p1==("si"):
        consum=int(input("Ingrese su consumo diario real: "))
        break
    elif p1==("no"):
        consum=int(input("Entonces ingrese un aproximado: "))
        break
else:
    print("Alerta!, no ingreso un valor necesario")
print("\n")
print("Ahora escoja una opción para ver su consumo")
r=int(input("""Ingrese un numero para escojer su opciòn:
1. Diario
2. Semanal
3. Mensual
4. Anual
Respuesta: """))
while r:
    if r==1:
        print(nombre,"su consumo diario es: ", consum*1," Litros")
        break
    elif r==2:
        print(nombre,"su consumo semanal es: ", consum*7," Litros")
        break
    elif r==3:
        print(nombre,"su consumo mensual es: ", consum*30," Litros")
        break
    elif r==4:
        print(nombre,"su consumo anual es: ", consum*365," Litros")
        break
    else:
        print("Escoja una opciòn vàlida.!","\n")
        break
print("\n")
print(nombre, "Ahora sabremos si consume el agua necesaria para su uso diario: ")
print("\n")
while True:

    if consum<=200 or consum<299:
        print("Su consumo de agua es bajo")
        break
    elif consum>=300 and consum<=600:
        print("Su consumo de agua es normal")
        break
    elif consum>=600 and consum<=800:
        print("Su consumo de agua es elevado")
        break
    elif consum>=801 and consum<=1000:
        print("Considere cuidar y reducir el uso del agua")
        break
    elif consum==(1001) or consum==(1002):
        print("Está al limite de uso permitido")
        break
else:
    print("Su consumo de agua es muy alto, considere reducir y cuidar el agua.!")
print("\n")
print("         Programa terminado       ")
