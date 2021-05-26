# Introducción

Python es un lenguaje interpretado y dinámicamente tipado. Esto tiene _pros_ y _cons_

**Pros**

* Multiplataforma.
* Solo se requiere un intérprete para ejecutar.
* No es necesario compilarlo.

**Cons**

* Mucho más lento que los lenguajes convencionales.
* Al no producir código máquina, el intérpete ha de ser instalado en la máquina de los que deseen ejecutar el programa.

# Cython y otros bindings

Algunos proyectos (como _Ctyhon_ ) permite traspilar el código Python a código máquina (concretamente, lo convierten a C que a su vez se convierte a códiog máquina) en aras de hacer que el código sea más rápido.

No obstante, este código puede estar sometido a ciertas limitaciones.
