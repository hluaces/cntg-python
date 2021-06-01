# Formatos de cadenas

## ASCII y code points

El clásico ASCII permite almacenar carácteres usando un único _byte_. De éstos caracteres, los primeros 128 corresponden al alfabeto latino.

Los 128 restantes son insuficientes para representar el resto de caracteres usados por los distintos idiomas del mundo, por lo que pronto quedó claro que ASCII no era un estándar que pudiese usarse para la internacionalización.

Esto también dejó evidente que, a la hora de almacenar cadenas y carácteres, tendríamos que establecer el concepto de _code points_.

## Code points

Un _code point_ no es más que un valor numérico que identifica a una letra.

Puesto que los lenguajes del mundo requieren distintos conjuntos de caracteres, éstos a su vez necesitarán usar un conjunto distinto de identificadores.

Esto se soluciona con las _code pages_, que no son más que diferentes estándares que permiten hacer que la mitad superior de la tabla ASCII (es decir: los valores superiores a 128) permitan almacenar distintos carácteres: p.ej.: el alfabeto griego, las letras latinas con acentos, etc.

Esto implica que, para saber el valor de un _code point_ será imprescindible saber a qué _code page_ se corresponde.

Un ejemplo de _code page_ puede ser la ISO-8859-1 (también conocida como "_latin1_").

## Unicode

Las _code pages_ fueron un parche temporal. Pronto quedó patente que no servirían para cubrir las necesidades de internacionalización del mundo debido a que no eran prácticas (se necesitaba un gran número de _code pages_) y a que tampoco permitían representar de forma simultánea carácteres de _code pages_ distintas.

La solución que traía Unicode para esto era un tamaño de página de caracteres mucho mayor con capacidad para más de un millón de carácteres. En estas enormes tablas los primeros 128 carácteres se correspondían con el alfabeto latino y los primeros 256 con las del _code point_ ISO-8859-1, que se corresponde con los carácteres usados en Europa del oeste.

Unicode también se dividía en varios estándares (el equivalente a las _code pages_) agrupando carácteres que tuviesen un uso o naturaleza similar.

Un ejemplo de estos estándares sería `UCS-4`, que usaba 32 bits para almacenar los carácteres.

Unicode tiene un carácter especial conocido como _Byte Order Mark_ (o "_BOM_") que es un carácter mágico que guarda metadatos de la _code page_.

## UTF-8

Unicode resultó ser, también, un parche temporal. Los principales problemas que tenía eran los siguientes:

Por un lado, usaba demasiada memoria para almacenar caracteres. Usar 32 bits para almacenar una letra (`a`) que puede representarse con 8 resultaba en un incremento de memoria 4 veces superior.

Por otro lado, el problema de raíz no estaba solucionado, puesto que Unicode también estaba limitado en el número de carácteres (su _code page es finito_ a pesar de disponer de millones de huecos).

La solución pasaba por crear cadenas que pudiesen tener un tamaño arbitrario y que solo usasen la memoria que su carácter necesitase. Eso lo consiguen utilizando carácteres especiales que se pueden considerar "_flags_" cuya labor es la de indicar que varios bytes conforman un único carácter.

Hay varias representaciones de UTF que toman un número inicial de bytes diferente, siendo el más usado UTF-8, p.ej.: UTF-8, UTF-16, UTF-32.

La forma de tratar el _Byte Order Mark_ por parte de algún software, en ocasiones, puede causar problemas de visualización en documentos UTF-8. No es raro, por ello, encontrarse con variantes de UTF que llevan la coletilla "`+BOM`" (p.ej.: `UTF-8+BOM`).

Éste es el estándar actual que estamos usando y con el que Python es completamente compatible.

# Strings

## Cadenas multi línea

Pueden usarse tres carácteres de comillas simple (`'`) o comillas doble (`"` )consecutivos para hacer un string multi línea:


```python
text1 = """Ejemplo de comentario multi línea
número 1
con comillas dobles
"""

text2 = '''Ejemplo de comentario multi línea
número 2
con comillas dobles
'''
```

## Operadores de strings

- `+`: concatena dos cadenas.
- `*`: multiplica una cadena por un número.
- `+=`: concatena una cadena (variable) con otra.
- `*=`: multiplica una cadena (variable) por un número.

## Operar con valores de code point

La función `ord(<caracter>)` permite obtener el _code point_ de un número:

```python
print(ord("a"))   # 97
print(ord("😁"))  # 128513
```

La función `chr(número)` devuelve el valor de un _code point_:

```python
chr(97)     # "a"
chr(128513) # "😁"
```

Otras funciones de _code points_:

- `min()`: devuelve el carácter cuyo _code point_ es el más pequeño de una cadena.
- `max()`: devuelve el carácter cuyo _code point_ es el más grande de una cadena.

## Listas como iterables

Las listas son objetos iterables. Esto significa que:

* Puede iterarse sobre ellas con un `for` (cada elemento sería una letra).
* Se pueden aplicar _slices_ sobre las cadenas.
* Pueden usarse los operadores `in`  y `not in` para determinar si una cadena está en otra cadena (p.ej.: `"la" in "hola"`)
* Puede usarse el método `index()` para buscar el índice en el que se encuentra una letra dentro de una cadena.
* Pueden usarse otros métodos nativos de iterables: `list()`, `count()`.

Las cadenas en Python son inmutables. Esto implica que:

- No se puede usar `del` para borrar letras de una palabra.
- No existe el método `append()`.
- No existe el método `insert()`.

## Métodos útiles de cadenas

- `center(<anchura>)`: centra la cadena en un campo de anchura dada.
- `endswith(<cadena>)`: determina si una cadena termina con una cadena dada.
    * También hay `startswith()`.
- `find(<cadena>)`: permite buscar una cadena en otra.
    * Es una función segura que no levanta error.
    * Puede pasarse un segundo parámetro para revertir.
    * Puede pasarse un tercer parámetro para omitir coincidencias.
    * `rfind()` hace lo mismo, pero buscando por la derecha.
- Métodos para determinar el contenido de una cadena:
    * `isalnum()`: Devuelve `True` si solo contiene números y letras.
    * `isalpha()`: Devuelve `True` si la cadena solo contiene letras.
    * `isdigit()`: Devuelve `True` si la cadena solo contiene números.
    * `islower()` e `isupper()`.
    * `isspace()`.
- `join(<lista>)`: convierte una lista en una cadena usando como caracter de unión el valor de la cadena sobre la que se llame el método, p.ej.: `",".join(["1","2","3"])`.
- `split(<delimitador>)`: separa una cadena en una lista usando el delimitador para diferenciar entre elementos.
- Métodos de capitalización:
    * `capitalize()`.
    * `lower()`.
    * `upper()`.
    * `swapcase()`.
    * `tile()`: hace un `capitalize()` a todas las palabras de una frase.
- `strip()`, `lstrip()` y `rstrip()`: elimina los espacios que preceden a la cadena, van después de ella o ambos.
- `replace(<que>, <con que>)`: reemplaza una parte de la cadena con otra.

## Comparación de cadenas

Al compararse las cadenas con operadores lógicos (`==`, `!=`, etc.) se buscará el primer _code point_ distinto en ambas y se usará ese para la comparación.

Comparar dos cadenas de longitudes distintas hará que la más larga se considere más grande.

# Excepciones

## Uso de try / except

Las excepciones en Python pueden gestionarse con bloques `try` / `except`. Python prefiere el uso de excepciones a las constantes comprobaciones de errores, que pueden causar que el código pierda legibilidad.

Un ejemplo de uso de `try` que atrapa todas las excepciones:

```python
try:
    x = 2 / 0
except:
    print("Ha ocurrido un error")
```

## Múltiples excepts

El problema de usar `except` para gestionar excepciones es que, en ocasiones, no podemos saber cuál se ha disparado.

Hay dos formas de identificar qué excepción se lanza en un código que pueda generar más de una. La primera es usar varios bloques `except`:

```python
try:
    a = []
    x = 2 / len(a)
    print(a[0])
except ZeroDivisionError:
    print("División entre cero")
except IndexError:
    print("Acceso a elemento inexistente")
except:
    print("Ha ocurrido una excepción no controlada")
```

La segunda es que las sentencias `except` agreguen las distintas excepciones a tratar entre paréntesis, por ejemplo:

```python
try:
    a = []
    x = 2 / len(a)
    print(a[0])
except (ZeroDivisionError, IndexError):
    print("Ha ocurrido un error")
```

## Excepciones básicas de Python

Las excepciones básicas de Python se heredan de la siguiente forma:

```
BaseException
├── Exception
|   ├── MemoryError
|   ├── StandardError
|   |   └── ImportError
|   ├── LookupError
|   |   ├── KeyError
|   |   └── IndexError
|   ├── ValueError
|   └── ArithmeticError
|       ├── OverflowError
|       └── ZeroDivisionError
├── SystemExit
└── KeyboardInterrupt
```

A la hora de hacer _match_, los bloques `except` usarán la primera coincidencia que se encuentren entre la lista de `excepts`, teniendo en cuenta que podrán hacer match tanto en el propio nombre de la excepción como en el de cualquiera de las que hereden. P.ej.:

```python
try:
    # Este código lanza una excepción de tipo ZeroDivisionError
    x = 2 / 0
# El código entrará en este bloque ya que ZeroDivisionError
# hereda de ArithmeticError
except ArithmeticError
    print("Arithmetic error")
# Este código no se ejecutará
except ZeroDivisionError:
    print("Zero division")
```

## Lanzar excepciones

La instrucción `raise` permite lanzar una excepción si se conoce su nombre, por ejemplo:

```python
raise ZeroDivisionError('Ocurrió una división entre cero.')
```

Adicionalmente, también puede usarse sin ningún argumento siempre que esté dentro de un bloque `except`. En ese caso propagará la excepción al contexto superior.

```python
try:
    x = 2 / 0
except ZeroDivisionError:
    print("Ocurrió una división entre cero.")

    try:
        x = 2 / 0
    except ZeroDivisionError:
        print("Ocurrió una segunda división entre cero.")
        raise
```

En el ejemplo anterior el segundo `except` levanta una excepción. Dicha excepción no es tratada en el primer `except` por lo que el programa falla.

## Aserciones

La instrucción `assert` lanza una excepción `AssertionError` si la expresión que se le pase no se evalúa como `True` (o un valor _truthy_). P.ej.:

```python
try:
    x = input("Introduce un número: ")
    assert x.isnumeric()
except AssertionError:
    print("Valor inválido")
```

# Misc

* [Unicode VS UTF-8](https://stackoverflow.com/questions/643694/what-is-the-difference-between-utf-8-and-unicode).
* [Byte Order Mark](https://en.wikipedia.org/wiki/Byte_order_mark).