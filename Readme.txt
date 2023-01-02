Objetivos generales
✓ Desarrollar una WEB Django con patrón MVT subida a Github.

Se debe entregar
✓ Link de GitHub con el proyecto totalmente subido a la plataforma.
✓ Proyecto Web Django con patrón MVT que incluya:
    1. Herencia de HTML.
    2. Por lo menos 3 clases en models.
    3. Un formulario para insertar datos a todas las clases de tu models.
    4. Un formulario para buscar algo en la BD
    5. Readme que indique el orden en el que se prueban las cosas y/o donde están las funcionalidades.
--------------------------------------------------------------------------------------------------------

Set de pruebas segun cada vista:

Empleados:
    - Cargar Nombre (texto hasta 50 caracteres)
    - Apellido (texto hasta 50 caracteres)
    - DNI (numero entero)
    - Email (texto con @)
    - Cargo (texto hasta 50 caracteres)
    - Fecha de Nacimiento (formato anio-mes-dia, ej: 1973-07-06).

Cliente:
    - Cargar nombre de Cliente (texto hasta 50 caracteres)
    - Direccion (texto hasta 50 caracteres)
    - Pedido (texto hasta 50 caracteres)
    - Estado ((texto hasta 50 caracteres, ej: Activo/Inactivo)

Producto:
    - Codigo (numero entero)
    - Descripcion (texto hasta 50 caracteres)
    - Cantidad (numero entero)

Cuando se finaliza la carga, el programa llama a una pagina con un mensaje indicando la carga correcta.

Busqueda:
	Para el modulo de busqueda, esta definido por el momento solo para "Clientes". Se debe indicar el noombre
	a buscar, y el programa, en caso de encontrarlo, devolvera el nombre y estado. EN caso de no estar cargado 
	en la base de datos, devolvera un mensaje que no fue encontrado.


Base de Datos SQLite
    superuser: admin
    password: admin
