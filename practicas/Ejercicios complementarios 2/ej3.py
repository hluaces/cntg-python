#!/usr/bin/env python

def show_docs():
    """Muestra la documentación de algunas funciones por pantalla."""

    print("abs()", abs.__doc__)
    print("int()", int.__doc__)
    print("len()", len.__doc__)


if __name__ == "__main__":
    show_docs()