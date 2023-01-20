ENTREGA DEL PROYECTO FINAL
Se debe entregar:
✔	Se deberá realizar de forma individual, crearás una aplicación web estilo blog programada en Python en Django. Esta web tendrá administrador, perfiles, registros, páginas y formularios.
✔	La entrega se realizará enviando el link a GitHub, en el readme de GitHub deberá estar el nombre completo del estudiante y una descripción de dos o tres renglones contando qué hizo. 
✔	En el GitHub debe haber un video o link a vídeo donde el estudiante muestra su web funcionando en no más de diez minutos. 
Dentro del GitHub deberá existir una carpeta con por lo menos 3 casos de pruebas debidamente documentados.

Consigna: Se tiene que crear una Web semejante a un Blog, dicha web deberá contar con usuarios y permisos para ellos. La web deberá contar con:
✔	Contar con algún acceso visible a la vista de "Acerca de mí" donde se contará acerca de los dueños de la página manejada en el route about/.  (En castellano un acerca de mí que hable un poco de los creadores de la web y del proyecto).
✔	Contar con algún acceso visible a la vista de blogs que debe alojarse en el route pages/. (Es decir un html que permite listar todos los blogs de la BD, con una información mínima de dicho blog)
✔	Acceder a una pantalla que contendrá las páginas. Al clickear en “Leer más” debe navegar al detalle de la page mediante un route pages/<pageId>. (Al hacer clic se ven más detalle de lo que se veía en el apartado anterior) 
✔	Si no existe ninguna página mostrar un "No hay páginas aún". (Aclarando, si en la página hacemos clic en algún lugar que no existe que diga eso, o que lleve a un html con esos mensaje, no dejar botones que no responden)
✔	Para crear, editar o borrar las fotos debes estar registrado como Administrador.
✔	Cada blog, es decir cada model Blog debe tener como mínimo, un título, subtítulo, cuerpo, autor, fecha y una imagen (mínimo y obligatorio, puede tener más).
✔	Piezas sugeridas, no hace falta que estén todas, pero tiene que haber por lo menos un CRUD completo y el módulo de Login debe ser sólido:

--------------------------------------------------------------------------------------------------------
Esta version ya tiene funcionando el modulo de Usuarios (creacion, busqueda, edicion, listar y borrar), el modulo de posteos donde 
se puede crear, listar y borrar), tambien esta en funcionamiento el modulo de mensajeria, en el cual con una bandeja de mensajes donde se listan los mensajes enviados y recibidos.
Todas las funciones principales se pueden utilizar con un usuario registra.
Cada Usuario tiene la opcion de editar su perfil, en el cual tiene un campo de biografia, puede adjuntar una foto (avatar) y cargar su pagina web.

Video en youtube:
https://youtu.be/NWlMZHKICcI

Descipcion de cada Vista:
Antes de correr las pruebas hay que asegurarse que estamos logueados al portal.

- Modulo Posteo:
    1- Este modulo puede ser accedido sin necesidad de estar logueado. 
    2- Selecionar el boton y nos despliega el listados de posteos cargados en el portal y las opciones para cada uno.
    3- Si elegimos la opcion "leer", nos muestra el detalle del posteos. Si elegimos la opcion "borrar" nos borra el posteo. Si eliges la opcion "crear nuevo posteo" te permite 
    cargar uno nuevo. La opcion "volver" regresa a la pagina de inicio.
    4- Las opciones "crear nuevo post" y "borrar" solo son visualizadas por los ususarios logueados.

- Modulo Mensajes:
    1- Este modulo solo puede ser accedido por los usuario logueados.
    2- Al ingresar se muestra una bandeja de mensajes, donde se listan los mensajes enviado y recibidos.
    2- Clickeando directamente sobre el mensaje nos da la opcion de "responder" el mensaje si estamos en la bandeja de Entrada.
    Si estamos en la bandeja de Salida nos pemite leer en detalle el mensaje enviado.
    3- Cuando ingresamos al mensaje recibido, automaticamente se cambia un registo que indica que el mensaje ya fue leido.

- Modulo Perfil:
    1- Aca permite al usuario registrar un nuevo usuario, buscar un usuario especifico, listar los usuarios y editar su perfil (bio, avatar y pagina web).
    2- En la opcion "editar profile" nos da la opcion de cargar nuestra biografia, subir un avatar y poner nuestra pagina web.
    3- Una vez seleccionado salvado los cambios nos despliega la informacion y nos vuleve a dar la opcion de editar nuevamente el profile o de volver
    al menu de perfil.

- Modulo Acerca de:
    1- Eneste modulo hago una breve resenia de mi persona.


Base de Datos SQLite
    superuser: jgranata
    password: jgranata
