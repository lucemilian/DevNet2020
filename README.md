# DevNet2020
Becas Digitaliza: DevNet - Ene 20
- - - -
## Listado de actividades **[EVUALUABLES]** :
>Tareas [Actualizado a día 13/04/2020]

- [x] Crear una cuenta de GitHub y, al menos, un repositorio público.

>![avatar]: Repositiorio incialmente privado, pasado a público en cuanto el tutor pida acceso.
------
- [x] Calculadora (es una tarea a la que le añadiremos más funcionalidades).
    - [x] Crear un menú que indique las opciones que hay.
    - [x] Como mínimo, incluir: suma, resta, multiplicación, división, exponenciales y raíces cuadradas. Se pueden añadir más funcionalidades.
    - Podéis usar las funciones y técnicas vistas en las sesiones, o implementar otras que consideréis oportunas. Obviamente, ser eficientes tendrá más nota.

>![avatar]: Calculadora creada, con nombre "MathPy".
-----
- [x] Crear un programa que permita conectarse con el controlador APIC-EM de Cisco
    - [x] El usuario tendrá que escoger la opción que quiera (no tendrá que especificar la url a mano)
    - [x] Añadir, como mínimo, 4 funcionalidades

>![avatar]: Programa creado, con nombre "APICEM.EXE".
----
- [X] Instalar el laboratorio de la máquina virtual el router CSR1000v.
    > Os he añadido el anuncio "Instalación Máquina Virtual - Cisco Cloud Services Router 1000V Series", el cual os describe los pasos a seguir y dónde están los archivos

    > [Esta actividad no se evaluará como tal, pero la incluyo aquí porque hay que preparar el entorno (o el Sandbox de cisco.developer.com) para poder hacer la tarea siguiente].

>![avatar]: Más fácil de lo que parecía.

----
- [x] Crear un script que permita conectarnos a nuestra Router CSR1000v (bien sea en local o a través del Sandbox) y que, a través de un menú, nos aparezcan una serie de opciones que nos permita realizar las siguientes tareas:
    - [#] Obtener un listado de las interfaces del router (indicar, en modo tabla, el nombre de la interfaz, su IP y MAC)
    - [X] Crear Interfaces
    - [x] Borrar Interfaces
    - [X] Obtener la tabla de routing y crear una tabla con Identificador (0,1,2...), Red de destino, e Interfaz de salida.
    - [ ] Implementar una petición a 2 módulos de yang diferentes compatibles con nuestro router

>![avatar]: Casi Terminado, con problemas:
  -  No he encontrado la dirrecion MAC en varios modelos yang, pero no aparece al realizar petición GET. Tampoco aparece nada con el modelo "Cisco-IOS-XE-arp".
  -  Se ha usado más de un metodo para realizar las tareas.


- - - -

[avatar]: https://avatars0.githubusercontent.com/u/20265786?s=60&u=7fbaefdf4b1a1e7f87c3e8ec411d99a18eb76319&v=4