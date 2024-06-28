nominaPasajeros=[]
asientosDisponibles=("asientoComun","espacioAdicionalParaPiernas","NoReclina")
Asientocomún=60000 
Espacioadicionalparapiernas=80000 
Noreclina=50000 
cantidad=0
total=0



def comprarPasajes():

    pasajes=int(input("¿CUÁNTOS PASAJES DESEA COMPRAR?  "))
    print("TIPOS DE ASIENTOS DISPONIBLES")
    print("*****************************")
    print("(1)ASIENTO COMÚN")
    print("(2)ESPACIO ADICIONAL PARA PIERNAS")
    print("(3)NO RECLINA")
    print()
    
  

def mostrarUbicacionesDisponibles():
def verListadoDePasajeros():
    print("RUT: ")

def buscarPasajeros():
def reasignarAsiento():

def mostrarGananciasTotales():
    print("TIPO DE ASIENTO\t             CANTIDAD\t       TOTAL")
    print("--------------------------------")
    print("ASIENTO COMUN $",Asientocomún)
    print("--------------------------------")
    print("ESPACIO PARA PIERNAS $",Espacioadicionalparapiernas,)
    print("--------------------------------")
    print("NO RECLINA $",Noreclina)
    print("--------------------------------")
    print("TOTAL",total)


while True:

    print("VENTAS DE PASAJES VUELOS NACIONALES")
    print()
    print("(1)Comprar pasajes")
    print("(2)Mostrar ubicaciones disponibles")
    print("(3)Ver listado de pasajeros")
    print("(4)Buscar pasajero")
    print("(5)Reasignar asiento")
    print("(6)Mostrar ganancias totales")
    print("(7)Salir")

    opcion=int(input("INGRESE UNA OPCION: "))

    if opcion==1:
        comprarPasajes()
    elif opcion==2:
        mostrarUbicacionesDisponibles()
    elif opcion==3:
        verListadoDePasajeros()
    elif opcion==4:
        buscarPasajeros()
    elif opcion==5:
        reasignarAsiento()
    elif opcion==6:
        mostrarGananciasTotales()
    elif opcion==7:
        break


