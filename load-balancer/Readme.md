# Equilibrio de Carga

El equilibrio de carga es el proceso de distribución del tráfico de red entre varios servidores. Esto garantiza que ningún servidor único tenga demasiada demanda. Al distribuir el trabajo de manera uniforme, el equilibrio de carga mejora la capacidad de respuesta de la aplicación. También aumenta la disponibilidad de aplicaciones y sitios web para los usuarios.

Para ejecutar este ejemplo con docker se deben seguir los siguientes pasos:

1. Ejecutar el siguiente comando

    ```bash
    docker compose up load-balancer 
    ```

1. Añadir al archivo *[hosts](https://en.wikipedia.org/wiki/Hosts_(file))* la siguiente entrada: `127.0.0.1  balanced.server.com`

1. Visitar en el navegador a la dirección anterior.