# Proxy Inverso 

Un proxy inverso (o puerta de enlace) aparece para el cliente como un servidor web ordinario. No es necesaria ninguna configuración especial en el cliente. El cliente realiza solicitudes ordinarias de contenido en el espacio de nombres del proxy inverso. El proxy inverso luego decide dónde enviar esas solicitudes y devuelve el contenido como si fuera el origen.

Un uso típico de un proxy inverso es proporcionar a los usuarios de Internet acceso a un servidor que está detrás de un firewall. Los proxies inversos también se pueden usar para equilibrar la carga entre varios servidores de back-end o para proporcionar almacenamiento en caché para un servidor de back-end más lento. Además, los proxies inversos se pueden usar simplemente para llevar varios servidores al mismo espacio de URL.

Para ejecutar este ejemplo con docker se deben seguir los siguientes pasos:

1. Crear una red donde se puedan ver los contenedores:

```bash
$ docker network create reverse-proxy-net
```

2. Crear el contenedor de nuestra aplicación back-end.

```bash
$ docker build --tag node-http-server node-http-server
```

3. Descargar la imagen de apache

```bash
$ docker pull httpd:2.4
```

4. Descomentar la sección de modulos requeridos y la sección de *Includes* en el archivo [httpd.conf](/httpd.conf).

5. Iniciar el contenedor de la aplicación back-end.

```bash
$ docker run --name node-http-server --network reverse-proxy-net -d node-http-server
```

6. Iniciar el contenedor de apache

```bash
$ docker run -p 80:80 -v $(pwd)/httpd.conf:/usr/local/apache2/conf/httpd.conf -v $(pwd)/reverse-proxy/r-proxy.conf:/usr/local/apache2/conf/extra/r-proxy.conf --network reverse-proxy-net -d --name apache httpd:2.4
```

7. Añadir en el archivo hosts el nombre del servidor, el cual es `node.server.com` especificado en el *VirtualHost* apuntando a 127.0.0.1.

8. Visite en el navegador a la siguiente dirección: `http://node.server.com`