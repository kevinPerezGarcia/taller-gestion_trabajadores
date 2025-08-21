from utils import limpiar_consola

def eliminar_trabajador(lst_trabajadores: list) -> None:
    while True:
        limpiar_consola()
        print("=====================================")
        print("COMPONENTE. ELIMINACION DE TRABAJADOR")
        print("=====================================")
        print("\nOpciones:\n")
        print("0. Volver")
        print("1. Acción. Eliminar trabajador")
        opcion = int(input("\nIngrese una opción vía su código numérico: "))
        if opcion == 0:
            break
        elif opcion == 1:
            limpiar_consola()
            print("---------------------------")
            print("ACCION. ELIMINAR TRABAJADOR")
            print("---------------------------")

            dni_a_eliminar = input("\nIngrese el DNI del trabajador a eliminar: ")

            for ind, trabajador in enumerate(lst_trabajadores):
                if trabajador["dni"] == dni_a_eliminar:
                    tpl_eliminacion = (True, ind, trabajador)
                else:
                    tpl_eliminacion = (False, None)

            if tpl_eliminacion[0]:
                confirmacion_de_eliminacion = input(f"\n¿Está seguro que desea eliminar el registro del trabajador cuyo DNI es {dni_a_eliminar}? (S/N): ").upper()
                if confirmacion_de_eliminacion == 'N':
                    continue
                else:
                    indice = tpl_eliminacion[1]
                    del lst_trabajadores[indice]
                    print(f"\n¡Registro del trabajador con DNI '{dni_a_eliminar}' eliminado!")
                    input("\nPresione la tecla 'ENTER' para continuar.")
            else:
                print(f"\n¡Trabajador, con DNI: {dni_a_eliminar}, no registrado!")
