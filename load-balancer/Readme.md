# Equilibrio de Carga

El equilibrio de carga es el proceso de distribución del tráfico de red entre varios servidores. Esto garantiza que ningún servidor único tenga demasiada demanda. Al distribuir el trabajo de manera uniforme, el equilibrio de carga mejora la capacidad de respuesta de la aplicación. También aumenta la disponibilidad de aplicaciones y sitios web para los usuarios.

Para ejecutar este ejemplo con docker se deben seguir los siguientes pasos:

1. Crear una red donde se puedan ver los contenedores

```bash
$ docker network create load-balance-net
```

2. Crear la imagen de nuestra aplicación back-end.

```bash
$ docker build --tag node-http-server node-http-server
```

3. Descargar la imagen de apache

```bash
$ docker pull httpd:2.4
```

4. Descomentar la sección de modulos requeridos y la sección de *Includes* en el archivo [httpd.conf](/httpd.conf).

5. Iniciar los contenedores de la aplicación back-end.

```bash
$ docker run --name node-http-server-0 --network load-balance-net -d node-http-server
```

```bash
$ docker run --name node-http-server-1 --network load-balance-net -d node-http-server
```

6. Iniciar el contenedor de apache

```bash
$ docker run -p 80:80 -v $(pwd)/httpd.conf:/usr/local/apache2/conf/httpd.conf -v $(pwd)/load-balancer/l-balancer.conf:/usr/local/apache2/conf/extra/l-balancer.conf --network load-balancer-net -d --name apache httpd:2.4
```

7. Añadir en el archivo hosts el nombre del servidor, el cual es `balanced.server.com` especificado en el *VirtualHost* apuntando a 127.0.0.1.

8. Visite en el navegador a la siguiente dirección: `http://balanced.server.com`