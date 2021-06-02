# Clases

## Sintáxis de las clases

Las clases de Python se definen de la forma siguiente:

```python
#!/usr/bin/env/python


class Stack:

    def __init__(self, list=[]): # *1, *2
        self.__list = list       # *3, *4

    def push(self, element):
        self.__list.append(element)

    def pop(self):
        return self.__list.pop()

    def safe_pop(self, default=None):
        try:
            return self.pop()
        except IndexError:
            return default


class AddingStack(Stack):            # *5
    instancias = 0                   # *7

    def __init__(self, starting_value=0):
        Stack.__init__(self)
        self.__sum = starting_value
        AddingStack.instancias += 1  # *7

    def __substract(self):           # *9
        if isinstance(self.__sum, list):
            self.__sum.pop()
        else:
            self.__sum -= ret

    def push(self, element):
        self.__sum += element
        Stack.push(self, element)    # *6

    def pop(self):
        ret = Stack.pop(self)        # *6
        self.__substract()
        return ret

    def get_sum(self):
        return self.__sum


if __name__ == "__main__":
    stack = Stack()
    adding_stack = AddingStack([]) # *8

```

Varias cosas a destacar (están numeradas en el código superior):

1. La firma del constructor es `__init__(self)`, donde `self` es el objeto recién creado.
2. Todas las firmas de métodos incluirán el mismo parámetro `self`, que referencia al objeto sobre el que se llama el método en cuestión.
3. La forma de inicializar atributos es, sencillamente, crearlos al vuelo en el constructor usando el símbolo `.` para referenciar que pertenece al objeto recién creado. Estos son atributos públicos.
4. Los atributos privados se preceden de `__` haciendo que no puedan ser accesibles desde el exterior. No obstante, éstas si lo son, solo que Python internamente les cambia el nombre (ver uso de `__dict__` más abajo).
5. La herencia se define añadiendo un parámetro en la definición de clase que referencie a la superclaes.
6. Para invocar a un método de la superclase utilizamos la superclase como forma para invocar al método.
7. Las variables estáticas (es decir: variables **de clase**) se inicializan después de declarar el nombre de clase y comparten valor en todas las instancia de dicha clase.
8. El primer parámetro `self` no se pasa en las invocaciones a los métodos. Es proporcionado por el propio Python al ser invocado el método.
9. Los métodos cuyo nombre comience con `__` también se consideran privados.

Métodos y variables especiales:

* Las instancias tienen una variable mágica `__dict__` que devuelve un diccionario con los nombres y valores de sus atributos.
* La variable `__module__` devuelve el módulo que contiene la clase.
* La variable `__main__` contiene el nombre de la clase, pero solo es accesible desde el interior del objeto. Para saberlo desde fuera se puede usar `type()`.
* `__bases__` es una tupla que define las superclases, ordenadas, de un objeto.

## Acceso a atributos

Los objetos de Python, al tener atributos dinámicos, pueden conjuntos atributos completamente distintos entre si. Esto es un problema puesto que acceder a un atributo inválido lanza una excepción `AttributeError`:

```python
class Test
    def __init__(self):
        self.foo = "bar"

a = Test()

try:
    a.bar
except AttributeError:
    print("Error al acceder al atributo 'bar' de un objeto 'Test'.")

if a.hasattr('bar'):
    print(a.bar)
```

# Colas

## Stack

Un _stack_ es una cola LIFO (_Last In First Out_).

## Queue

Una _queue_ es una cola FIFO (_First In First Out_).

# Misc