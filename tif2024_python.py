"""
Input_uint:
Entrada de dato restringido solo a enteros positivos, si el usuario ingresa un valor 
incorrecto será reinterpretado como int(-1)
"""
def Input_uint():
    valor = input()
    if valor.isdecimal():
        resultado = int(valor)
    else:
        resultado = -1

    return resultado




"""
Input_pfloat:
Entrada de dato restringido a floats positivos. Si el usuario ingresa un valor incorrecto será
reinterpretado como float(-1.0)
"""
def Input_pfloat():
    resultado = -1.0
    valor = input()

    if len(valor) > 0 and valor[0] != '.' and valor[-1] != '.':
        valor_sin_punto = valor.replace(".", "", 1) # remueve el primer '.' que se encuentre
        if valor_sin_punto.isdecimal():
            resultado = float(valor)

    return resultado




"""
LeerCP:
funcion para la entrada de dato 'codigo pieza'
La funcion no finaliza hasta que el usuario ingrese un numero entero entre 0 y 99. 
"""
def LeerCP():
    CP = Input_uint()
    while not (0 <= CP <= 99 ):
        print("codigo de pieza invalido. vuelva a ingresarlo")
        CP = Input_uint()

    return CP





"""
LeerCC:
funcion para la entrada de dato 'codigo componente'
La funcion no finaliza hasta que el usuario ingrese '0' o un numero entero entre 101 y 9999 cuyos
ultimos 2 digitos sean iguales a CP.
"""
def LeerCC(CP):
    CC = Input_uint()

    while not((CC == 0) or (101<=CC<=9999) and (CC%100 == CP)):
        print("codigo de componente invalido, vuelva a ingresarlo")
        CC = Input_uint() 
    return CC




"""
IngresarPrecio:
funcion para la entrada de dato 'precio componente'
La funcion no finaliza hasta que el usuario ingrese un numero entre 10.0 y 999.99
"""
def IngresarPrecio(CC):
    print("ingrese el precio del componente ",CC)
    PrC = Input_pfloat()
    while not (10.00 <= PrC <= 999.99):
        print("precio invalido, vuelva a ingresarlo")
        PrC = Input_pfloat()
    return PrC





"""
IngresarComponentes:
funcion para ingresar al menos 1 codigo de componente con su respectivo precio.
la funcion finaliza cuando el usuario ingresa '0' y devuelve el precio total de todos los componentes
ingresados 
"""
def IngresarComponentes(CP):
    print("ingrese un codigo de componente")
    while (CC := LeerCC(CP)) == 0:
        print("debe ingresar al menos un componente!")

    PrT = IngresarPrecio(CC)

    print("ingrese un segundo codigo de componente o 0 para terminar")
    while (CC := LeerCC(CP)) != 0:
        PrC = IngresarPrecio(CC)
        PrT = PrT + PrC
        print("ingrese otro codigo de componente o 0 para terminar")
    
    return PrT





"""
ProgramaPrincipal:
bucle principal del programa donde se procesan todas las piezas.
Por cada pieza procesada se imprime su codigo y su precio final
El programa termina cuando el usuario ingresa '0' e imprime la cantidad total de piezas procesadas.
"""
def ProgramaPrincipal():
    contador_de_piezas = 0

    print("ingrese codigo de pieza o 0 para terminar")
    while (CP := LeerCP()) != 0:
        contador_de_piezas = contador_de_piezas + 1
        print("el codigo de pieza es: ",CP)
        PrT = IngresarComponentes(CP)
        print("Precio final de pieza ",CP,": ", PrT, "\n")
        print("ingrese otro codigo de pieza o 0 para terminar")

    print("cantidad de piezas procesadas: ",contador_de_piezas)



ProgramaPrincipal()