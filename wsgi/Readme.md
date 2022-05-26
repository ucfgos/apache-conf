# WSGI
[WSGI](https://wsgi.readthedocs.io/) Es una especificación que describe cómo un servidor web se comunica con las aplicaciones web y cómo las aplicaciones web se pueden encadenar para procesar una solicitud.

Para ejecutar este ejemplo con docker se deben seguir los siguientes pasos:

1. Ejecutar el siguiente comando

    ```bash
    docker compose up wsgi
    ```

1. Añadir al archivo *[hosts](https://en.wikipedia.org/wiki/Hosts_(file))* la siguiente entrada: `127.0.0.1  wsgi.apache.com`

1. Visitar en el navegador a la dirección anterior.