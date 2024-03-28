
## Proyecto sprint 6: Introducción a la automatización de pruebas


## _Descripción_



> El proyecto es un sistema elaborado mediante el lenguaje de programación "Python" aprovechando su versatilidad y amplio manejo de librerias. Con las pruebas desarrolladas en el proyecto, buscamos comprobar la entrada de datos específicamente en el campo "nombre" en la creación de kits de la aplicación "Urban Grocers", esto con el fin de garantizar su correcto funcionamiento y administración de datos, a su vez, estas pruebas podrían ser utilizadas y/o modificadas para aplicarse en otros contextos con diferentes parámetros de entrada.





## Documentación utilizada

Para el desarrollo del proyecto se consultó la documentación oficial de python así como la libreria "requests" para realizar las solicitudes HTTP, al igual, el marco de prueba "pytest" fue utilizado para realizar las pruebas unitarias del proyecto.

- [Python] - https://docs.python.org/3/
- [Libreria request] - https://requests.readthedocs.io/en/latest/
- [Pytest] - https://docs.pytest.org/en/7.1.x/contents.html


## Tecnologías y técnicas utilizadas 

El proyecto fue desarrollado en el lenguaje de programación python aprovechando su versatilidad y amplia variedad de librerias, tomando esto en cuenta, garantizamos la calidad del código, mejoramos la administración de errores y, garantizamos la confiabilidad y funcionalidad del código. Al igual, fueron utilizadas pruebas unitarias para comprobar la entrada de datos en los campos correspondientes y así agilizar su verificación.

    Herramientas y técnicas 
    Desarrollo del código: Python
    Editor de código: Pycharm
    Control de versiones: Git 
    Pruebas unitarias: Pytest

## Instalación y ejecución del proyecto

    Instalación
1. Clonar el repositorio desde Github con el siguiente URL: https://github.com/Alainjc/qa-project-06-es.git
2. Instalar las dependencias del proyecto usando los siguientes comandos desde la línea de comandos: 
    - 'pip install requests'
    - 'pip install pytest'


    Ejecución
- Abrir la línea de comandos 
- Navegar hasta el directorio donde se encuentra el archivo "qa-project-06-es"
- Usar el comando "pytest" para ejecutar las pruebas

## Descripción del contenido 

El proyecto contiene los siguientes archivos:

    configuration.py
Se específica la URL del contenedor así como los endpoints usados para la creación de un nuevo usuario y para la creación de un nuevo kit.

    data.py
Se específican las variables con los datos en formaton JSON que serán utilizados para realizar las solicitudes HTTP y las pruebas unitarias de los archivos "sender_stand_request.py" y "create_kit_name_kit_test" respectivamente.

    sender_stand_request.py
Se muestran las funciones que se usarán para enviar los solicitudes HTTP mediante el uso de la URL y los enpoints especificados en el archivo "configuration.py". Las funciones del archivo nos ayudan a crear un nuevo usuario, extraer el "token" de autorización y a crear un nuevo kit a partir del usuario recien creado.
    
    create_kit_name_kit_test.py
Se desarrollan las pruebas para verificar la entrada de datos en el campo "name" en la creación de kits, se hace uso de las variables especificadas en el archivo "data.py" y se realizan las solicitudes HTTP mediante el uso de las funciones del archivo "sander_stand_request.py", de la misma manera, se comprueba el código de respuesta HTTP para verificar el resultado actual y comparlo con el resultado esperado.


## Autor/es
>Alain Julián Chan Pat
GITHUB: https://github.com/Alainjc

