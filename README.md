# Environment

1. Crea imagen de docker

    ```bash
    hector@red-queen:~/CNTG - python 2021$ cd docker/
    hector@red-queen:~/CNTG - python 2021/docker$ docker build -t local/cntg-python .
    ````

2. Arranca la imagen de docker con el directorio de prácticas para probar:

    ```bash
    cd ..
    docker run -it -v $(pwd)/:app local/cntg-python bash
    ```

# Configuración sublime

Con la imagen creada, este "_build system_" puede permitir ejecutar desde dentro de Docker:

```
{
    "cmd": ["docker", "run", "--rm", "-v", "$file:/app/$file",
            "local/cntg-python", "python",  "-u", "/app/$file"],
    "file_regex": ".*\\.py",
    "selector": "source.python"
}

```
