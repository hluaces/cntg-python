# Operadores booleanos

* **Igualdad** `==`: compara dos valores y devuelve `True` si son iguales o `False` si no.
* **No igualdad** `!=`: compara dos valores y devuelve `True` si son distintos, o `False` si no.
* **Comparación** (`>`, `<`, `>=`, `<=`): compara dos operandos para determinar si uno es más grande, más pequeño, mayor o igual o menor o igual, respectivamente. 

Las comparaciones se hacen _por valor_, no _por referencia_.

## Prioridades operadores booleanos

Cualquier operador aritmético (módulotiene más prioridad que estos elementos):

1. `>`, `<`, `>=`, `<=`
2. `==`

# Condicionales

## if

`if` permite hacer comparaciones. Nótese que la sintáxis **requiere** indentación. 

```python
if True:
    print("Es verdadero")
else:
    print("Es falso")
```

Existe también `elif`

```python
numero = 1

if numero == 1 then:
    print("Es uno")
elif numero == 2 then:
    print("Es dos")
else:
    print("WTF is this shit")
```

También puede hacerse en dos líneas (no recomendado):

```python
numero = 2

if numero == 1: print("es uno")
else: print("no es uno")
```

Y también está la versión en una línea:

```python
numero = 2
print("hola") if numero % 2 == 0 else print("adios")
```

# Bucles

## while

Similar al if. Ejemplo de bucle infinito:

```python
while true:
    print("Bucle infinito")
```

Bucle con una expresión evaluada:

```python
numero = 10

while numero != 0:
    print("El número es " + str(numero))
    numero-=1
```

Bucle con `else`. Esa sección siempre se ejecuta al final del bucle:

```python
numero = 10

while numero != 0:
    print("El número es " + str(numero))
else:
    print("Ha terminado el bucle while")
```

## for

Más similar a `foreach` que a un `for` como tal.

Puede usarse una llamada a `range()` para emular un for típico:

```python
for i in range(100):
    print("Número: " + str(i))
else:
    print("Los for también tienen \"else\".")
```

Iterar sobre listas:

```python
pares = [2,4,6,8,10,12,14,16,18,20]

for par in pares:
    print("Par: " + str(par))
```

## break y continue

Tanto `while` como `for` pueden usar las sentencias `break` y `continue` para modificar el comportamiento de un bucle. La sentencia `pass` sirve como _placeholder_ en un bucle, pero **no hace nada** (ni saltar la ejecución actual).

```python
for i in range(2,100,2):
    print("Número: " +str(i))

    if i == 10:
        continue

    if i > 20:
        break
```

# Lógica booleana

## and 

Operador "_Y_" lógico.

```python
numero = 1
if numero % 2 == 1 and numero < 2:
    print("Número menor que 2 e impar.")
```
## or

Operador "_O_" lógico.

```python
numero = 4
if numero == 1 or numero == 4:
    print("El número es 1 o 4.")
```

## not

Operador "_no_" lógico.

```python
numero = 3
if not (numero == 1 or numero == 4):
    print("El número NO es 1 o 4.")
```
## in

Comprueba si un elemento está en una lista.

```python
lista = [1, 2, 3, 4, 5]

if 1 in lista:
    print("1 está en la lista.")
```

## not in

Comprueba si un elemento _no_ está en una lista.

```python
lista = [1, 2, 3, 4, 5]

if 0 not in lista:
    print("0 NO está en la lista.")
```

## Comparaciones

* `>`
* `<`
* `>=`
* `>=`

Al **comparar strings** hace una cosa rara **no usa orden lexicográfico**, hace una mezcla de esto y de longitud de cadenas.

## lógica de bits

### Operadores lógica de bits

* `&`: conjunction, requiere dos "_1_" para que el resultado sea "_1_".
* `|`: disjunction, requiere uno o más "_1_" para que el resultado sea "_1_".
* `~`: negation.
* `^`: exclusive or (xor), requires exactamente un "_1_" para que el resultado sea "_1_".
* `<<`: _shift_ a la izquierda.
* `>>`: _shift_ a la derecha.

## Prioridad de operadores booleanos

Los operadores booleanos unarios tienen más prioridad que los aritméticos (ver módulo 2). El resto, están todos por debajo.

La lista sería:

1. Operadores `not`.
2. [Insertar aquí tabla de prioridades de operadores aritméticos.
3. `and`, `or`, `>`, `<`, `>=`, `<=` y operadores de bit.

# Listas

Las listas son variables que se almacenan **por referencia** no por valor. Pueden usarse los métodos de _slicing_ (el operador `:`) para hacer una copia de los valores de una lista.

## Declarar listas

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## Listas heterogéneas

```python
numeros = [1, 2, 3, ["una", "lista", "interior"], 5, "hola troncos", 8.2]
```

## Comienzo de las listas

Las listas empiezan en `0`.

```python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Imprime "1"
print(str(lista[0])) 
```

## Longitud de las listas

Su longitud puede comprobarse con la función `len()`:

```python
lista = [1, 2, 3, 4, 5, 6, 7]

print(len(lista)) # imprime 7
```

## Slices

El operador `:` permite obtener partes de una lista:

```python
lista = [1, 2, 3, 4, 5, 6, 7]

lista[0:2] # devuelve [1, 2, 3]
lista[5:]  # devuelve [6, 7]
lista[:3]  # devuelve [1, 2, 3]
lista[:]   # Devuelve una copia de la lista entera **POR VALOR** no referencia

# Los índices negativos solo pueden uarse al final de ":"
lista[0:-3] # devuelve [1, 2, 3, 4]
```

## Inicializar varios elementos de una lista

```python

# Pueden inicializarse valores usando comas para hacerlo a la vez
# La siguiente línea cambia los valores de los primeros 3 elementos
lista[0], lista[1], lista[2] = 1., 2., 3.

# Puede usarse lo mismo para revertir una lista
lenght = len(lista)
for i in range(len(lista) // 2):
    lista[i], lista[lenght -i - 1] = lista[lenght -i - 1], lista[i]
```

## Manipular listas

```python
lista = [0, 2, 3, 4, 5, 6, 7, 8, 9]

# Inserta un elemento al final
lista.append(10)
me refiero en el caso de querer hacer algo en la primera iteración, que es algo que hacías en el do
# Inserta un elemento antes de un índice concreto
lista.insert(1, 1)

# Borra un elemento de la lista
del(lista[9])

# Borra un slice entero
del(lista[0:1])

# Borra una lista entera
del list

# Borrar una lista entera solo borra la referencia
lista = [0, 1, 2, 3]
lista_2 = lista
del lista_2
print(lista) # La variable "lista" sigue existiendo
```

## Operaciones con listas

Las listas pueden ser sumadas

```python
a = [1, 2, 3]
b = [3, 4, 5]
c = a + b # Da como resultado [1, 2, 3, 3, 4, 5]
```

También pueden ser multiplicadas

```python
a = [2, 3, 4]
b = a * 3    # da como resultado [2, 3, 4, 2, 3, 4, 2, 3, 4]

## Ordenar listas

```python
lista = [0, 2, 3, 4, 5, 6, 7, 8, 9]

# Ordenación
lista.sort()

# Esto la revierte
lista.reverse()
```

## List comprehension

Idioma que permite generar de forma masiva una lista. La sintaxis es:

```python
[<expresión> for <identifivador> in <lista>]
```

El idioma genera una lista donde cada valor será la evaluación de `<expresión>` para cada `<identificador>` presente en la lista `<lista>`.

Por ejemplo, para generar una lista que contenga 10 strings `"A"`:

```python
["A" for i in range(10)]
```

También hay una sintáxis que permite usar condicionales:

```python
[<expresion> for <identificador> in <lista> if <expresión de comprobación>]
```

Ejemplo para generar los números pares entre 0 y 100

```python
[i for i in range(100) if i % 2 == 0]
```

Se pueden anidar para generar listas multidimensionales. Un tablero de ajedrez (8x8) podría hacerse así:

```python
[[0 for fila in range(8)] for columna in range(8)]
```

# Funciones 

## Funciones vs métodos

* Las funciones no alteran los datos de entrada, los métodos sí pueden hacerlo.
* Los métodos pertenecen a los datos con los que trabajan (p.ej.: un objeto).
* Las funciones pertencen al código genral.

# Misc

* `list(<iterable>)` convierte un iterable en una lista.
* `range(start, stop, step)` genera una secuencia de números.
* `len(lista)` devuelve la longitud de una lista.
* Python no permite mezclar _tabs_ y _espacios_ como indentación. 