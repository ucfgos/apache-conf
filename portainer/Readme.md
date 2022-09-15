# Portainer

Portainer es una plataforma ligera de prestación de servicios para aplicaciones en contenedores que se puede utilizar para gestionar entornos Docker, Swarm, Kubernetes y ACI. Está diseñado para ser tan simple de implementar como de usar. La aplicación le permite administrar todos los recursos de su orquestador (contenedores, imágenes, volúmenes, redes y más) a través de una GUI "inteligente" y/o una API extensa.

Para ejecutar este ejemplo con docker se deben seguir los siguientes pasos:

1. Ejecutar el siguiente comando

    ```bash
    docker compose up portainer 
    ```

1. Añadir al archivo *[hosts](https://en.wikipedia.org/wiki/Hosts_(file))* la siguiente entrada: `127.0.0.1  portainer.server.com`

1. Visitar en el navegador a la dirección anterior.