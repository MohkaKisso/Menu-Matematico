import Modulos as modulo

print("bienvenido al programa porfavor ingrese una de las opciones")

while True:
    modulo.opciones()
    print("ingrese una opcion")
    option=input()

#---------------------------Area de un Circulo--------------------------------

    if option=="a" or option=="A":
        modulo.Area_circulo()

#---------------------------Volumen de un Cubo--------------------------------

    elif option=="b" or option=="B":
        modulo.vol_cubo()

#-----------------------Volumen de un paralelepipedo--------------------------

    elif option=="c" or option=="C":
        modulo.vol_para()
    
#-----------------------Volumen de un piramide--------------------------   
    
    elif option=="d" or option=="D":
        modulo.vol_piram()
    
#-----------------------Volumen de un cilindro--------------------------   
    
    elif option=="e" or option=="E":
        modulo.vol_cil()
    
#-----------------------Volumen de un cono--------------------------   
   
    elif option=="f" or option=="F":
        modulo.vol_con()
    
#-----------------------Volumen de un esfera--------------------------   
   
    elif option=="g" or option=="G":
        modulo.vol_esf()
    
#-----------------------Area de un trapecio--------------------------   
   
    elif option=="h" or option=="H":
        modulo.area_trap()
    
#--------------------------Raiz cuadrada------------------------------   
   
    elif option=="i" or option=="I":
        modulo.raiz_cuad()
    
#-------------------------------Exit------------------------------------   
  
    elif option=="x" or option=="X":
        break
    else:
        print("ingrese una opcion valida")
