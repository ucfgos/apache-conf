# Django

Django es un marco web Python de alto nivel que fomenta un desarrollo rápido y un diseño limpio y pragmático. Creado por desarrolladores experimentados, se ocupa de gran parte de las molestias del desarrollo web, por lo que puede concentrarse en escribir su aplicación sin necesidad de reinventar la rueda. Es gratis y de código abierto.

Para ejecutar este ejemplo con docker se deben seguir los siguientes pasos:

1. Ejecutar el siguiente comando

    ```bash
    docker compose up django 
    ```

1. Añadir al archivo *[hosts](https://en.wikipedia.org/wiki/Hosts_(file))* la siguiente entrada: `127.0.0.1  django.app.com`

1. Visitar en el navegador a la dirección anterior.

___
>**Nota**: La variable SECRET_KEY utilizada en este proyecto es insegura y no debe ser utilizada en ambientes de producción