#Datos
"""
No 6 : Dados tres números, ordenarlos de mayor a menor. 
Jesús Alejandro Sánchez Muñoz
758377 
Igenieria Mecanica 
Algoritmos y Programcion 
ESI232B2 
Jorge Zaldivar
18/Feb/25 
10 minutos de duracion
"""


# Entradas
A = float(input("Ingrese su primer numero :  \n"))
B = float(input("Ingrese su segundo numero : \n"))
C = float(input("Ingrese un tercer numero : \n"))

if A > B > C :
    print("El orden de mayor a menor es : " ,A , B, C)
elif B > C >A:
    print("El orden de mayor a menor es : " ,B ,C ,A )
elif C > A > B:
    print("El orden de mayor a menor es : " ,C ,A ,B )
elif A > C > B:
    print("El orden de mayor a menor es : ", A, C, B)
elif C > B > A:
    print("El orden de mayor a menor es : " ,C ,B ,A )
elif B > A > C:
    print("El orden de mayor a menor es : " ,B ,A ,C )
else : 
    print(A, B, C)

# Proceso


# Salidas

