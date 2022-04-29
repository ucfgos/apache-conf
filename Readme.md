# Configuración de Apache

El propósito de este repositorio es mostrar ejemplos de configuración de un servidor [Apache](https://httpd.apache.org), siguiendo buenas prácticas, para distintos escenarios.

Las demostraciones de cada ejemplo se hacen utilizando [Docker](https://www.docker.com) y la imágen httpd:2.4 para una mayor simplicidad.

A continuación se listan los ejemplos de configuraciones realizados hasta ahora:

* **Proxy inverso**: [Readme.md](reverse-proxy/Readme.md)
* **SSL**: [Readme.md](ssl/Readme.md)
* **Equilibrio de Carga**: [Readme.md](reverse-proxy/Readme.md)

## Contribución

Para contribuir con más ejemplos, se debe crear un [Pull Request](https://github.com/ucfgos/apache-conf/pulls) con los siguientes pasos:

* Crear una carpeta con el caso de uso que se desea agregar
* Añadir como comentarios los módulos requeridos en la sección *Extra Modules* del archivo [httpd.conf](httpd.conf)
* Añadir como un comentario el camino del archivo de configuración de apache al final del archivo [httpd.conf](httpd.conf).
* Añadir a la lista de este Readme el caso de uso ejemplificado. 

Si se desea se puede contribuir con ejemplos que no utilicen docker.