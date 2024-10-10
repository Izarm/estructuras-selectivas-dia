# Simple
a = 33
b = 200

if b > a:
    print(b," es mayor que " ,a)

# Doble

y = 200
z = 333

if y > z:
    print(y," es mayor que ",z)
else:
    print(y, " No es mayor que ",z)

#Multiple
C = 7
D = 7

if C > D:
    print(C, " es mayor que ",D)
elif C < D:
    print(C, " No es mayor que ",D)
else:
    print(C, " Es igual que ",D)

#Condiciones enlazadas

x = 15

if x > 10:
    print("Por encima de diez,")
    if x > 20:
        print("y tambien por encima de 20!")
    else:
        print("pero no por encima de 20.")

#Parametro end y sep

print("Estudiar los sabados", end=' ')
print("es genial")

print("Daniela","Luis","Carlos","Camila") #Agrega un espacio por defecto
print("Daniela","Luis","Carlos","Camila", sep="") #Quita espacio
print("Daniela","Luis","Carlos","Camila", sep=",") #Agrega una coma
print("Daniela","Luis","Carlos","Camila", sep ="_", end='   _Curso_Python')#Implementacion end y sep
