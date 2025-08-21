from utils import limpiar_consola

dct_trabajador = {}

def modificar_trabajador(lst_trabajadores) -> None:
    while True:
        limpiar_consola()
        print("======================================")
        print("COMPONENTE. MODIFICACION DE TRABAJADOR")
        print("======================================")
        print("\nOpciones:\n")
        print("0. Volver")
        print("1. Acción. Modificar trabajador")

        opcion = int(input("\nIngrese una opción vía su código numérico: "))

        if opcion == 0:
            break
        elif opcion == 1:
            limpiar_consola()
            print("----------------------------------")
            print("ACCION. MODIFICACION DE TRABAJADOR")
            print("----------------------------------")
            dni_a_modificar = input("\nIngrese el DNI del trabajador a modificar: ")
            for ind, trabajador in enumerate(lst_trabajadores):
                if trabajador["dni"] == dni_a_modificar:
                    tpl_modificacion = (True, ind, trabajador)
                else:
                    tpl_modificacion = (False, None)
            
            if tpl_modificacion[0]:
                confirmacion_modificacion = input(f"\n¿Está seguro que desea modificar el registro del trabajador cuyo DNI es '{dni_a_modificar}'? (S/N): ").upper()
                if confirmacion_modificacion == "N":
                    continue
                else:
                    indice = tpl_modificacion[1]
                    print("")
                    dct_trabajador["dni"] = dni_a_modificar
                    dct_trabajador["nombres_apellidos"] = input("Nombres y apellidos: ")
                    dct_trabajador["sexo"] = input("Sexo: ")
                    dct_trabajador["edad"] = input("Edad: ")
                    dct_trabajador["anio_ingreso"] = input("Año de ingreso: ")
                    dct_trabajador["salario"] = input("Salario: ")
                    lst_trabajadores[indice] = dct_trabajador

                    print(f"\n¡Registro del trabajador con DNI '{dni_a_modificar}', modificado!")
                    input("\nPresione la tecla 'ENTER' para continuar.")
            else:
                print(f"\n¡Trabajador, con DNI: {dni_a_modificar}, no registrado!")
