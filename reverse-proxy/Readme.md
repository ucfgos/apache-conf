# Proxy Inverso 

Un proxy inverso (o puerta de enlace) aparece para el cliente como un servidor web ordinario. No es necesaria ninguna configuración especial en el cliente. El cliente realiza solicitudes ordinarias de contenido en el espacio de nombres del proxy inverso. El proxy inverso luego decide dónde enviar esas solicitudes y devuelve el contenido como si fuera el origen.

Un uso típico de un proxy inverso es proporcionar a los usuarios de Internet acceso a un servidor que está detrás de un firewall. Los proxies inversos también se pueden usar para equilibrar la carga entre varios servidores de back-end o para proporcionar almacenamiento en caché para un servidor de back-end más lento. Además, los proxies inversos se pueden usar simplemente para llevar varios servidores al mismo espacio de URL.

Para ejecutar este ejemplo con docker se deben seguir los siguientes pasos:


1. Ejecutar el siguiente comando

    ```bash
    docker compose up reverse-proxy
    ```

1. Añadir al archivo *[hosts](https://en.wikipedia.org/wiki/Hosts_(file))* la siguiente entrada: `127.0.0.1  node.server.com`

1. Visitar en el navegador a la dirección anterior.