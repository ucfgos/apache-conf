# SSL

SSL (Secure Sockets Layer) es la tecnología estándar para mantener segura una conexión a Internet y proteger los datos confidenciales que se envían entre dos sistemas, evitando que los hackers lean y modifiquen cualquier información transferida, incluidos los posibles datos personales.

Para ejecutar este ejemplo con docker se deben seguir los siguientes pasos:



1. Ejecutar el siguiente comando

    ```bash
    docker compose up ssl
    ```

1. Añadir al archivo *[hosts](https://en.wikipedia.org/wiki/Hosts_(file))* la siguiente entrada: `127.0.0.1  ssl.example.com`

1. Visitar en el navegador a la dirección anterior.

___
>**Nota**: Los certificados usados en este proyecto solo sirven el propósito de demonstración, estos no deben ser utilizados en un ambiente de producción.