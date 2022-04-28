# SSL

SSL (Secure Sockets Layer) es la tecnología estándar para mantener segura una conexión a Internet y proteger los datos confidenciales que se envían entre dos sistemas, evitando que los hackers lean y modifiquen cualquier información transferida, incluidos los posibles datos personales.

Para ejecutar este ejemplo con docker se deben seguir los siguientes pasos:

1. Descargar la imagen de apache:

```bash
$ docker pull httpd:2.4
```

2. Descomentar la sección de modulos requeridos y la sección de *Includes* en el archivo [httpd.conf](/httpd.conf).

3. Iniciar el contenedor de apache

```bash
$ docker run -p 80:80 -p 443:443                                        
-v $(pwd)/httpd.conf:/usr/local/apache2/conf/httpd.conf 
-v $(pwd)/ssl/ssl.conf:/usr/local/apache2/conf/extra/ssl.conf 
-v $(pwd)/ssl/server.crt:/usr/local/apache2/conf/server.crt 
-v $(pwd)/ssl/server.key:/usr/local/apache2/conf/server.key 
-v $(pwd)/ssl/index.html:/usr/local/apache2/htdocs/index.html 
--name apache -d httpd:2.4
```

4. Añadir en el archivo hosts el nombre del servidor, el cual es `ssl.example.com` especificado en el *VirtualHost* apuntando a *127.0.0.1*

5. Visite en el navegador a la siguiente dirección: `http://node.server.com`

___
>**Nota**: Los certificados usados en este proyecto solo sirven el propósito de demonstración, estos no deben ser utilizados en un ambiente de producción.