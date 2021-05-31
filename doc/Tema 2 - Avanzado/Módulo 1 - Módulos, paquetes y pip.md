# Namespaces

Todos los nombres en Python (sean variables, funciones, clases, constantes, etc.) han de ser únicos dentro de su _namespace_.

Un _namespace_ viene dado por el módulo en el que se define el nombre, siendo aquellos nombres que no están dentro de un módulo perte miembros del _namespace_ global.

Para evitar colisiones, Python obliga a referenciar al nombre de otro namespace precediéndolo del nombre de su módulo. Por ejemplo, para referenciar a la función `sin` del módulo `math` deberíamos hacer lo siguiente:

```python
import math # Esta instrucción se explica más adelante

math.sin(10)
```

Esta separación por _namespaces_ implica que un mismo nombre puede existir en ambos. Por ejemplo:

```python
import math

def sin(valor):
    print("Hola, " + str(valor) + ".")

sin(10)      # Imprimirá "hola, 10"
math.sin(10) # Ejecutará la función "sin" del módulo math
```

# Path de módulos y paquetes

A la hora de importar paquetes y módulos Python busca en la variable `sys.path` (requiere importar `sys`) la lista de directorios en la que encontrarlos.

Puede modificarse previo a realizar cuaquier importación, p.ej.:

```python
from sys import path
path.append('C:\\Users\\user\\py\\modules')

import module
```

# Importar módulos

## Instrucción import

La instrucción `import` permite importar módulos (sean de la biblioteca de Python o módulos externos) para usar alguna de la funcionalidad o constantes que éstos especifican.

Un ejemplo de importación básico de todos los métodos de algunos módulos:

```python
import sys
import math

# Opcionalmente, podemos importarlos todos a separados con comas
# import sys,math
```

Para referenciar a cualquier nombre del módulo tendremos que usar la notación `<modulo>.<nombre>`, tal y como se explicaba en la sección anterior sobre _namespaces_.

Adicionalmente, `import` permite cambiar el _namespace_ sobre el que se importa el módulo usando para ello la palabra clave `as`, por ejemplo:

```python
import math as matematicas

matematicas.sin(10)
```

## Instrucción from

Otra forma de importar módulos nace en la instrucción `from`, que tiene esta sintaxis:

    from <nombre del módulo> import <nombres a importar separados por comas>

La diferencia con `import` radica en que `from` tomará los nombres especificados del módulo dado y los traerá al _namespace_ actual, haciendo que deban ser referenciados sin usar la notación con puntos.

Un ejemplo pon la función `sin` del módulo `math`:

```python
from math import sin,pi

sin(pi) # No necesitamos referenciarlo con puntos
```

La palabra clave `as` permite sobreescribir el nombre con el que se importan al _namespace_ global:

```python
from math import pi as PI

print(PI)
```

Importar un nombre sobre el _namespace_ global hará que se sobreescriba cualquier nombre existente en el módulo global.

# Reflexión

Python tiene métodos reflexivos que permiten obtener datos de los nombres definidos. El uso de la reflexión escapa al alcance de este módulo, pero algunas funcionalidades son útiles para el caso de la importación de módulos.

La función `dir()` lista todos los nombres de un namespace:

```python
import math

dir()     # Devuelve una lista con los nombres del namespace global
dir(math) # Devuelve una lista con los nombres del namespace 'math'
```

La función `help`, posiblemente solo presente en una sesión interactiva, muestra ayuda de un nombre:

```python
import math

help(math.exp)
```

# Paquetes

Los paquetes son una abstraccioń más que permite englobar a varios módulos.

Si comparáramos un módulo con un paquete, el primero sería un archivo y el segundo un directorio.

Los paquetes son directorios con un conjunto de requisitos (explicados más adelante) y pueden importarse exactamente igual que con los módulos.

Para usarlos, sencilalmente basta crear una estructura de directorios (donde el directorio raíz es el paquete y los subdirectorios son _subpaquetes_) y añadir archivos con los módulos conforme sea necesario.

Para que el paquete funcione correctamente su directorio raíz ha de tener un fichero `__init__.py` vacío. Dicho fichero _puede_ tener código (que sería ejecutado al importar algo de dicho paquete), pero no es necesario.

Un ejemplo de esta estructura es:

```
.
└── api_methods/
    ├── http/
    |   ├── get.py
    |   └── post.py
    └── __init__.py
```

Si el directorio `api_methods^ estuviese en el path podríamos hacer lo siguiente:

```python
import api_methods.http

http.get()
http.post()
```

## Variables especiales

* `__name__`: el valor del nombre del archivo en el que está la variable (sin `.py`) o, en el caso del archivo que inicia la ejecución, la string `"__main__"`.

# Ecosistema de paquetes de Python

El [Python packaking Work Group](https://wiki.python.org/psf/PackagingWG) mantiene un conjunto de repositorios públicos con módulos y paquetes hechos por la comunidad conocido como el [Python Package Index](https://pypi.org/).

## Instalación de paquetes

El binario `pip` (acrónimo de "_PIP installs packages_") sirve para gestionar las dependencias de Python.

Comandos de pip:

* `list`: muestra los paquetes instalados.
* `help <comando>`: muestra ayuda de otros comandos de pip.
* `show <paquete>`: muestra información de un paquete.
* `search <búsqueda>`: busca paquetes en los repositorios.
* `install <paquete>`: instala un paquete.
* `install <paquete>==<version>`: instala un paquete a una versión dada.

A la hora de instalar se puede añadir el parámetor `--user` para hacer que la instalación sea a nivel de usuario, no a nivel de sistema.

# Módulos útiles

- `math`: operaciones matemáticas.
- `random`: operaciones con números aleatorios y elementos aleatorios de listas.
- `platform`: obtiene información del hardware de la máquina.

# Misc

* [Lista de módulos de la biblioteca estándar de Python](https://docs.python.org/3/py-modindex.html).
* [Documentación de Python sobre módulos](https://docs.python.org/3/tutorial/modules.html).
* [Python Package Index](https://pypi.org/).
* [Python packaking Work Group](https://wiki.python.org/psf/PackagingWG).