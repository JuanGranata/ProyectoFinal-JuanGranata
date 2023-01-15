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
Esta version ya tiene funcionando el modulo de Usuarios (creacion, busqueda, edicion, listar y borrar), el modulo de post donde 
se puede crear, editar, listar y borrar).
El modulo Mensajes, esta presentando desperfectos tecnicos, estamos trabajando para solucionarlo a la brevedad...!!!

Set de pruebas segun cada vista:




Base de Datos SQLite
    superuser: jgranata
    password: jgranata
