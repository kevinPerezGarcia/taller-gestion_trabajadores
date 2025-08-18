# Taller. Sistema de Gestión de Trabajadores (CLI)

Pequeño proyecto educativo en Python para administrar una **agenda de trabajadores** desde la consola. El objetivo **no es** solo “hacer que funcione”, sino **evolucionar el mismo problema** a través de distintos **paradigmas de programación**:

1. **Estructurado** → 2) **Procedimental** → 3) **Modular** → 4) **Orientado a Objetos (POO)**

Cada etapa agrega organización, validaciones, pruebas y persistencia, manteniendo la funcionalidad base: **registrar, consultar, eliminar, listar** trabajadores.

---

## Contenidos

* [Objetivos de aprendizaje](#objetivos-de-aprendizaje)
* [Requisitos](#requisitos)
* [Ejecución rápida](#ejecución-rápida)
* [Modelo de datos](#modelo-de-datos)
* [Funcionalidades](#funcionalidades)
* [Roadmap por paradigmas](#roadmap-por-paradigmas)

  * [Fase 1 — Estructurado](#fase-1--estructurado)
  * [Fase 2 — Procedimental](#fase-2--procedimental)
  * [Fase 3 — Modular](#fase-3--modular)
  * [Fase 4 — Orientado-a-Objetos](#fase-4--orientado-a-objetos)
* [Persistencia de datos](#persistencia-de-datos)
* [Validaciones y manejo de errores](#validaciones-y-manejo-de-errores)
* [Pruebas](#pruebas)
* [Estructura de carpetas sugerida](#estructura-de-carpetas-sugerida)
* [Estilo y convenciones](#estilo-y-convenciones)
* [Mejoras futuras (Backlog)](#mejoras-futuras-backlog)
* [Licencia](#licencia)

---

## Objetivos de aprendizaje

* Comprender **cómo cambia el diseño** del mismo programa según el paradigma.
* Practicar **entrada/salida por consola**, **validación** y **estructuras de datos**.
* Introducir **persistencia** (JSON/CSV) y **pruebas automatizadas**.
* Evolucionar hacia **abstracciones** (clases, repositorios, servicios).

---

## Requisitos

* **Python 3.10+**

---

## Ejecución rápida

```bash
python main.py
```

---

## Modelo de datos

Cada **trabajador** es un diccionario (Fase 1–3) o una instancia de clase (Fase 4):

```python
{
  "dni": str,                 # único
  "nombre_apellido": str,     # “Titulo Capitalizado”
  "año_de_ingreso": int,
  "sexo": "F" | "M",
  "edad": int,
  "salario": float
}
```

**Lista en memoria** `lst_trabajadores: list[trabajador]`.

---

## Funcionalidades

* **Registrar** trabajador (evita duplicados por `dni`).
* **Consultar** trabajador por `dni`.
* **Eliminar** trabajador por `dni`.
* **Listar** todos los trabajadores.

Comandos disponibles en el menú:

```
1) Registrar   2) Consultar   3) Eliminar   4) Listar   0) Salir
```

---

## Roadmap por paradigmas

A continuación, cómo se resolverá progresivamente.

### Fase 1 — Estructurado

**Objetivo:** código lineal, funciones mínimas y variables globales (como en el avance actual).

* **Archivo único** `main.py`.
* **Variables globales**: `lst_trabajadores`, `dct_trabajador` (plantilla).
* **Persistencia**: no hay (datos en memoria hasta salir).
* **Ventajas**: rápido de implementar, ideal para aprender flujo básico.
* **Limitaciones**: alto acoplamiento, difícil de probar y mantener.

---

### Fase 2 — Procedimental

**Objetivo:** separar **lógica de negocio** de la **interacción con el usuario** manteniendo funciones puras cuando sea posible.

* **Funciones de consola**:

  * `registrar_trabajadores()`
  * `consultar_trabajadores()`
  * `eliminar_trabajadores()`
  * `listar_trabajadores()`
  * Validadores: `validar_anio`, `validar_edad`, `validar_sexo`, `validar_salario`
  * Búsqueda: `buscar_dni(dni)`

  **Sugerencias para completar funciones:**

* `consultar_trabajadores()`:

  * Pedir `dni`.
  * Usar `buscar_dni`.
  * Mostrar datos si existe; si no, mensaje en amarillo.

* `eliminar_trabajadores()`:

  * Pedir `dni`.
  * Confirmar eliminación.
  * Remover por índice devuelto por `buscar_dni`.

* `listar_trabajadores()`:

  * Recorrer `lista_trabajadores`.
  * Mostrar en tabla simple alineada por columnas.

* **Refactor**:

  * Extraer funciones que **no lean input** directamente (p. ej., `agregar_trabajador(lista, trabajador)`, `eliminar_por_dni(lista, dni)`).
  * Dejar el **input/print** únicamente en funciones de “interfaz”.
* **Beneficios**: facilita pruebas de lógica sin depender de input por consola.
* **Persistencia (opcional)**: JSON simple mediante funciones `guardar(lista) / cargar()`.

**Ejemplo de firma de funciones puras:**

```python
def agregar_trabajador(lista, nuevo) -> list:
    if any(t["dni"] == nuevo["dni"] for t in lista):
        raise ValueError("DNI duplicado")
    return [*lista, nuevo]
```

---

### Fase 3 — Modular

**Objetivo:** dividir en **módulos** para responsabilidad única.

**Sugerencia de módulos:**

* `ui.py` → interacción por consola (menú, prompts, formateo).
* `validaciones.py` → validadores y normalizadores.
* `domain.py` → operaciones de negocio (agregar, buscar, eliminar, listar).
* `storage.py` → persistencia (`JSON`/`CSV`).
* `main.py` → punto de entrada que orquesta módulos.

**Beneficios:** mantenible, favorece reutilización y pruebas.

**Decisiones:**

* Persistencia por defecto en `data/trabajadores.json`.
* Control de errores centralizado en `ui.py` (mensajes amigables).

---

### Fase 4 — Orientado a Objetos

**Objetivo:** encapsular datos y comportamientos, separar capas.

**Propuesta de clases (mínimo):**

* `Trabajador` (Entidad):

  * Atributos: `dni`, `nombre_apellido`, `anio_ingreso`, `sexo`, `edad`, `salario`
  * Métodos: `from_dict`, `to_dict`, `__str__`
  * Invariantes: DNI no vacío, sexo ∈ {F, M}, etc.
* `RepositorioTrabajadores`:

  * Métodos: `agregar`, `obtener(dni)`, `eliminar(dni)`, `listar()`
  * Implementaciones:

    * `RepositorioEnMemoria`
    * `RepositorioJSON(ruta_archivo)`
* `ServicioTrabajadores` (casos de uso):

  * Orquesta validaciones y repositorio.
  * Aplica reglas (no duplicados, normalización de nombres).
* `Consola` (UI):

  * Menú, prompts, formateo de tablas, mensajes de error.

**Diagrama textual (simplificado):**

```
Consola -> ServicioTrabajadores -> Repositorio (EnMemoria/JSON)
                     ^
                     |
                Trabajador
```

**Beneficios:** bajo acoplamiento, fácil cambiar la persistencia, pruebas unitarias claras.

---

## Persistencia de datos

Estrategias por fase:

* **Fase 1**: no persiste.
* **Fase 2** (opcional) / **Fase 3**: `JSON`

  * `guardar(lista, ruta)` / `cargar(ruta)`.
* **Fase 4**:

  * `RepositorioJSON` por defecto.
  * Futuro: `CSV`, `SQLite` o `TinyDB`.

**Formato JSON sugerido:**

```json
[
  {
    "dni": "12345678",
    "nombre_apellido": "Ana Pérez",
    "año_de_ingreso": 2020,
    "sexo": "F",
    "edad": 28,
    "salario": 2500.0
  }
]
```

---

## Validaciones y manejo de errores

* `dni`: no vacío; opcionalmente **solo dígitos** y longitud esperada (e.g., 8).
* `nombre_apellido`: limpiar espacios, capitalizar.
* `año_de_ingreso`: entero; rango razonable (e.g., 1970–año actual).
* `sexo`: “F” o “M”.
* `edad`: entero ≥ 14 (o política que definas) y ≤ 100.
* `salario`: float ≥ salario mínimo (si aplica) y ≤ tope razonable.
* **Mensajes**: usar colores ANSI ya presentes (amarillo para warnings, verde para ok).
* **Errores recuperables** en UI (no romper el programa por una entrada incorrecta).

---

## Estructura de carpetas sugerida

**Fase 1 (Estructurado) y Fase 2 (Procedural):**

```
./
└── main.py
```

**Fase 3 (modular):**

```
./
├── main.py
├── ui.py
├── domain.py
├── validaciones.py
├── storage.py
├── data/
│   └── trabajadores.json   (opcional)
└── tests/
    ├── test_domain.py
    └── test_validaciones.py
```

**Fase 4 (POO):**

```
./
├── main.py
├── app/
│   ├── __init__.py
│   ├── consola.py
│   ├── servicios.py
│   ├── modelos.py          # class Trabajador
│   ├── repositorios.py     # EnMemoria, JSON
│   └── validaciones.py
├── data/
│   └── trabajadores.json
└── tests/
    ├── test_modelos.py
    ├── test_repositorios.py
    └── test_servicios.py
```

---

## Estilo y convenciones

* **PEP 8** (nombres en `snake_case`, líneas ≤ 88–100 chars).
* **Mensajes de commit** claros (p. ej., `feat: agregar persistencia JSON`).
* **Tipar** firmas de funciones y clases en Fase 4.
* **Internacionalización**: la interfaz será en español; los identificadores en español o inglés, pero consistentes.

---

## Mejoras futuras (Backlog)

* Persistencia en **SQLite** con `sqlite3`.
* **Filtros** y **búsqueda avanzada** (por sexo, rango de edad, por año de ingreso).
* **Ordenamiento** al listar (por apellido, salario, etc.).
* **Reportes** (promedios, medianas, percentiles de salario).
* Exportación a **CSV**.
* **Logs** (archivo `logs/app.log` con operaciones y errores).
* Interfaz **TUI** (Textual/Rich) o **GUI** simple (Tkinter).
* Soporte para **salarios en diferentes monedas**.
* Validación de `dni` con **regex** y/o consulta externa (si aplica).

---

### Nota final

Este README describe **cómo** evolucionará el código existente para aprender por etapas. Cada fase deberá conservar la funcionalidad base del menú, pero con mayor calidad interna: primero separando responsabilidades, luego persistiendo los datos y, finalmente, encapsulando en clases y capas.
