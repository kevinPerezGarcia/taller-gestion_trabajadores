from utils import limpiar_consola

def listar_trabajadores(lst_trabajadores: list) -> None:
    while True:
        limpiar_consola()
        print("=================================")
        print("COMPONENTE. LISTA DE TRABAJADORES")
        print("=================================")
        print("\nOpciones:\n")
        print("0. Volver")
        print("1. Acción. Listar trabajadores")
        
        opcion = int(input("\nIngrese una opción vía su código numérico: "))

        if opcion == 0:
            break
        elif opcion == 1:
            limpiar_consola()
            print("---------------------")
            print("LISTA DE TRABAJADORES")
            print("---------------------\n")
            print("DNI    Nombres y Apellidos Sexo   Edad   Año de Ingreso Salario")
            print("...... ................... ...... ...... .............. .......")
            for trabajador in lst_trabajadores:
                print(f"{trabajador["dni"]:<6}", end=" ")
                print(f"{trabajador["nombres_apellidos"]:<19}", end=" ")
                print(f"{trabajador["sexo"]:<6}", end= " ")
                print(f"{trabajador["edad"]:<6}", end=" ")
                print(f"{trabajador["anio_ingreso"]:<14}", end=" ")
                print(f"{trabajador["salario"]:<7}")
            input("\nPulse la tecla 'ENTER' para continuar.")
