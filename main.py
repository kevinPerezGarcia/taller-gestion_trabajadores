from modulos.interfaz import interfaz
from modulos.registrar import registrar_trabajador
from modulos.listar import listar_trabajadores
from modulos.consultar import consultar_trabajador
from modulos.eliminar import eliminar_trabajador
from modulos.modificar import modificar_trabajador

lst_trabajadores = []

def main() -> None:
    while True:
        opcion = interfaz()
        if opcion == 0:
            break
        elif opcion == 1:
            registrar_trabajador(lst_trabajadores)
        elif opcion == 2:
            listar_trabajadores(lst_trabajadores)
        elif opcion == 3:
            consultar_trabajador(lst_trabajadores)
        elif opcion == 4:
            eliminar_trabajador(lst_trabajadores)
        elif opcion == 5:
            modificar_trabajador(lst_trabajadores)


if __name__ == "__main__":
    main()