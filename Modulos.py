import math

validacion=("si desea continuar presione (Y), de lo contrario presione (N)")

def opciones():
    print("-----------------------------------")
    print("A) area de un circulo")
    print("B) volumen de un cubo")
    print("C) volumen de un paralelepipedo")
    print("D) volumen de un piramide")
    print("E) volumen de un cilindro")
    print("F) volumen de un cono")
    print("G) volumen de un esfera")
    print("H) area de un trapito")
    print("I) raiz cuadrada")
    print("X) salir")
    print("-----------------------------------")

def Area_circulo ():
    print("A ingresado a la opcion de area de un circulo")
    print("ingres un valor para el radio del circulo")
    while True:
        try:
            radio=(int(input()))
            resultado=((math.pi)*(math.pow(radio,2)))
            print("el valor del area es ",resultado)
            break
        except ValueError:
            print("ingrese un numero valido")
    print(validacion)
    validation()

def vol_cubo ():
    print("A ingresado a la opcion de volumen de un cubo")
    print("ingrese el valor de uno de sus lados")
    while True:
        try:
            lado=(int(input()))
            resultado=math.pow(lado,3)
            print("el valor del area es ",resultado)
            break
        except ValueError:
            print("ingrese un numero valido")
    print(validacion)
    validation()

def vol_para ():
    print("A ingresado a la opcion de volumen de un paralelepipedo")
    print("ingrese el valor de su altura")
    while True:
        try:
            altura=(int(input()))
            break
        except ValueError:
            print("ingrese un numero valido")
    print("ingrese el valor de uno de sus lados")
    while True:
        try:
            lado1=(int(input()))
            break
        except ValueError:
            print("ingrese un numero valido")
    print("ingrese el valor del segundo lado")
    while True:
        try:
            lado2=(int(input()))
            resultado=(lado1*lado2*altura)
            print("el valor del area es ",resultado)
            break
        except ValueError:
            print("ingrese un numero valido")
    print(validacion)
    validation()
    
def vol_piram ():
    print("A ingresado a la opcion de volumen de un piramide")
    print("ingrese el valor de su altura")
    while True:
        try:
            altura=(int(input()))
            break
        except ValueError:
            print("ingrese un numero valido")
    print("ingrese el valor del primer lado de la base")
    while True:
        try:
            lado1=(int(input()))
            break
        except ValueError:
            print("ingrese un numero valido")
    print("ingrese el valor del segundo lado de la base")
    while True:
        try:
            lado2=(int(input()))
            resultado=((lado1*lado2*altura)/3)
            print("el valor del area es ",resultado)
            break
        except ValueError:
            print("ingrese un numero valido")
    print(validacion)
    validation()

def vol_cil ():
    print("A ingresado a la opcion de volumen de un cilindro")
    print("ingrese el valor del radio")
    while True:
        try:
            radio=(int(input()))
            break
        except ValueError:
            print("ingrese un numero valido")
    print("ingrese el valor de su altura")
    while True:
        try:
            altura=(int(input()))
            resultado=(((math.pi)*(math.pow(radio,2)))*altura)
            print("el valor del area es ",resultado)
            break
        except ValueError:
            print("ingrese un numero valido")
    print(validacion)
    validation()

def vol_con ():
    print("A ingresado a la opcion de volumen de un cono")
    print("ingrese el valor del radio")
    while True:
        try:
            radio=(int(input()))
            break
        except ValueError:
            print("ingrese un numero valido")
    print("ingrese el valor de su altura")
    while True:
        try:
            altura=(int(input()))
            resultado=((((math.pi)*(math.pow(radio,2)))*altura)/3)
            print("el valor del area es ",resultado)
            break
        except ValueError:
            print("ingrese un numero valido")
    print(validacion)
    validation()

def vol_esf ():
    print("A ingresado a la opcion de volumen de un esfera")
    print("ingrese el valor del radio")
    while True:
        try:
            radio=(int(input()))
            resultado=(((math.pi)*(math.pow(radio,2)))*(4/3))
            print("el valor del area es ",resultado)
            break
        except ValueError:
            print("ingrese un numero valido")
    print(validacion)
    validation()

def area_trap ():
    print("A ingresado a la opcion de area de un trapecio")
    print("ingrese el valor de su altura")
    while True:
        try:
            altura=(int(input()))
            break
        except ValueError:
            print("ingrese un numero valido")
    print("ingrese el valor de uno de los lados paralelos")
    while True:
        try:
            lado1=(int(input()))
            break
        except ValueError:
            print("ingrese un numero valido")
    print("ingrese el valor del lado paralelo opuesto")
    while True:
        try:
            lado2=(int(input()))
            resultado=(((lado2+lado1)*altura)/2)
            print("el valor del area es ",resultado)
            break
        except ValueError:
            print("ingrese un numero valido")
    print(validacion)
    validation()

def raiz_cuad ():
    print("A ingresado a la opcion de la raiz cuadrada")
    print("ingrese el valor del numero")
    while True:
        try:
            numero=(int(input()))
            resultado=math.sqrt(numero)
            print("el valor de la raiz cuadrada de ",numero," es ",resultado)
            break
        except ValueError:
            print("ingrese un numero valido")
    print(validacion)
    validation()

def validation():
    while True:
        try:
            op=input()
            if op=="y" or op=="Y":
                break
            elif op=="n" or op=="N":
                print("has salido de programa")
                exit()
            else:
                print("ingrese un valor valido (Y/N)")
        except:
            print("adios")
            quit()
