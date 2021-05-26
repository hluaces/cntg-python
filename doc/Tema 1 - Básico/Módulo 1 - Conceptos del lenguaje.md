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

# Tipos de argumentos

Las funciones tienen dos tipos de parámetros:

* **Posicionales**: aquellos cuya identidad se determina en función de la posición que ocupan en la lista de parámetros.
* **Nombrados**: aquellos cuya identidad se determina por el nombre que se le da al parámetro.

La declaración de cualquier tipo de parámetro permita que se use como nombrado o como posicional. Si queremos forzar un tipo u otro tenemos estas opciones.

Para pasar un argumento posicional se invoca de forma normal la función. En el caso de un parámetro nombrado sencillamente se indica con el formato `clave=valor` sin importar su orden o posición en la lista de argumentos.

**Opción #1**:

Si el primer parámetro se declara precedido de `*` éste tomará como valor una lista con todos los valores posicionales que se le pasen a la función.

```python
def imprimir_numeros(*numeros, fin_de_linea):
    print(numeros)
    if fin_de_linea:
        print("\n")

imprimir_numeros(1,2,3,4,5,fin_de_linea=False)
```

**Opción #2**:

Si se quieren especificar una mezcla de parámetros posicionales y nombrados puede añadirse un parámetro `*` que separe los posicionales del resto.

```python
def imprimir_numeros2(numero_1, numero_2, *, fin_de_linea):
    print([numero_1, numero_2])

    if fin_de_linea:
        print("\n")

imprimir_numeros2(4,5,fin_de_linea=True)
```

**Opción #3**:

Solo se quieren usar parámetros nombrados:

```python
def imprimir_numeros3(*, numero_1, numero_2, fin_de_linea):
    print([numero_1, numero_2])

    if fin_de_linea:
        print("\n")

imprimir_numeros3(numero_1=3,numero_2=4,fin_de_linea=True)
```