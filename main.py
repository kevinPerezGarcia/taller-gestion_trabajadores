def main() -> None:
    while True:
        opcion = interfaz()
        if opcion == 0:
            break
        elif opcion == 1:
            registrar_trabajador()
        elif opcion == 2:
            listar_trabajadores()
        elif opcion == 3:
            consultar_trabajador()
        elif opcion == 4:
            eliminar_trabajador()
        elif opcion == 5:
            modificar_trabajador()


main()