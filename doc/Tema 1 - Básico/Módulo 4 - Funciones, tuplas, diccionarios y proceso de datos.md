# Funciones

## Definición

Las funciones han de definirse antes de ser usadas. El código se lee de arriba a abajo.

La definición de una función sigue esta sintáxis:

```python
def <nombre de función>(<lista de parámetros>):
    <cuerpo de la función>
```

Por ejemplo:

```python
def imprimir_valor(valor):
    print(valor)
```

## Tipos de parámetros

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

## Retorno

`return` puede usarse para devolver valores o salir de la función.

Adicionalmente, puede retornarse `None` de forma explícita (o implícita, si no se devuelve otro valor).

## Scope

Las funciones pueden acceder a variables que estén fuera de su _scope_. Intentar modificarlas, no obstante, creará una nueva variable en lugar de modificar la externa.

Por ejemplo:

```python
var = 1

def modificar_var:
    print(var)
    var = 2
    print(var)
 
print(var)      # imprime "1"
modificar_var() # imprime "1" seguido de "2"
print(var)      # imprime "1"
```

Puede usarse la keyword `global` precediendo a una variable para dar escritura de una variable fuera del _scope_ de una función.


```python
var = 1

def modificar_var:
    global var
    
    print(var)
    var = 2
    print(var)

print(var)      # imprime "1"
modificar_var() # imprime "1" seguido de "2"
print(var)      # imprime "2"
```

# Tuplas

Las tuplas son _secuencias_ de Python, al igual que las listas. La diferencia es que éstas son _inmutables_, es decir: una vez creadas no pueden modificarse.

Las tuplas pueden crearse de dos formas: con paréntesis o solo con valores separados por comas:

```python
tupla = (1, 2, 3, 4, 5) # forma preferida
tupla2 = 1, 2, 3, 4, 5

# Las tuplas de un elemento han de inicializarse con una coma al final
tupla3 = (1,)
tupla4 = 1,
```

Las tuplas conservan todas las operaciones de las listas, exceptuando aquellas que alteran su contenido (agregar y eliminar elementos).

# Diccionarios



# Misc

* [Lista de funciones _builtin_ de Python](https://docs.python.org/3/library/functions.html)