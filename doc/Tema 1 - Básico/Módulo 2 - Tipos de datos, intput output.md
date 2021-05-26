# Variables

* Preferiblemente nombradas en _snake case_ (p.ej.: `mi_variable` o `conector_base_datos`).
* Las variables no son tipoadas ni hay que declararlas. Cuando se les asigna un valor éstas se crean.
* Inicializarla pasa simplemente por usar `=` para darle un valor, p.ej.:
    ```python
    entero = 2
    flotante = .2
    cadena = "hola, mundo
    ```
* No se pueden usar variables que no existan.

# Tipos de datos

* **Enteros**: `1`..
    * Pueden venir en formato octal: `0o123`.
    * O hexadecimal: `0x123`.
    * O binario: `0b1011`.
    * Pueden usar el caracter `_` para separar el número por legibilidad: `1_000_000`.
* **Flotantes**: `1.25`.
    * Puede omitirse la parte entera si es `0`: `.25` significa `0.25`.
    * Puede omitirse la parte decimal si es `0`. Es decir: `1.` es igual que `1.0`.
    * Pueden expresarse en formato científico: `1E8` o `1e8` significan "_1 * 10 elevado a 8 (1_000_000)_".
    * El formato científico también acepta negativos: `2E-4` es lo mismo que `0.0002`.
* **Strings**: `"monty python"`.
    * Un _string_ con comillas usando `\`: `"monty python's \"the flying circus\""`.
    * Usando mezclas de comillas: `'monty python's "the flying circus"'`.
    * Los _strings_ pueden estar vacíos, véase `""` o `''`.
* **Booleano**: `True` y `False` .
    * La capitalización es importante. `true` o `TRUE` no son booleanos.
* **Long**: convertido internamente por Python cuando el número es muy largo. Son flotantes sin factor decimal.
* `NULL`

# Operadores básicos

 * **Suma** (`+`).
 * **Resta** (`-`).
 * **División** (`/`): las divisiones **siempre generan flotantes**. `2/2` da como resultado `1.0`.
 * **División entera** `//`. Es lo mismo que `/` pero devolverá un entero si los dos numerandos de la división son enteros.
    * Usar con cautela. Por detrás realiza varios redondeos.
    * Los redondeos **pueden ser hacia abajo** (negativos).
 * **Multiplicación** (`*`).
 * **Módulo** (`%`).
 * **Exponente** (`**`): `3**2` es igual a `9`.
 
**TIP**: pueden hacerse raíces cuadradas con el operador _exponente_. La raíz cuadrada de 2 de un número es lo mismo que elevarlo a `0.5`, por tanto, la raíz cuadrada de 16 es igual a `16**0.5`.

## Prioridades aritméticas

1. `+` y `-` (usados como unarios, es decir: `-1` o `++1`).
2. Exponente `**`.
3. `*`, `/`, `//`, `%`.
4. `+` y `-` como operaciones binarias (p.ej.: `1+2` o `2-3`).

## Operadores rápidos

Permiten modificar el valor de una variable. Es un `short-hand` para operadores binarios normales.

- `*=`
- `/=`
- `-=`
- `+=`
- `**=`
- `%=`

## Operadores de string

- `+`: concatena cadenas.
- `*`: repite cadenas (p.ej.: `"hola"*5` sería `"holaholaholaholahola"`).

# Comentarios

```python
# Esto es un comentario de una línea

'''
Esto es un comentario multilínea
Se usan en la documentación automática de Python
Yayyyyyyyyyy!
''' 
```
# Funciones 

* La función `int()` permite cambiar a entero. Su **segundo parámetro** permite especificar base (p.ej.: `int("1011", 2)`).
* La función `str()` convierte a _string_ un valor.
* La función `input()` permite obtener datos del teclado.
* La función `print()` imprime un conjunto de valores en pantalla, que puede ser de cualquier tipo.

# Miscelánea

* La guía de estilo de Python es [PEP8](https://www.python.org/dev/peps/pep-0008/)
