# proyecto2_segundaunidad

Este proyecto trata sobre la manipulación, obtención , edición y  guardado  de datos  a partir de un CSV, el cual contiene datos obtenidos de pacientes sometidos a diferentes tratamientos con drogas, y por cada paciente un comentario aludiendo a los síntomas que presentan después de dicha exposición.

Colaboradores:
              -Denise Valdés 
              -Sebastian Benavides


Pasos a seguir :
1.-  Abrir  el archivo  “creacion_de_archivos.py” así se crearan los archivos csv divididos por año.

	-para tener en consideración al momento de abrir “creacion_de_archivos.py”: 
		 Ejemplo 1:
		“carpeta = Path('/home/hp/Programacion 1/Unidad 2/proyecto 2 unidad 2				/archivos1')”  

		lo que hace es crear una carpeta  en la ubicación seleccionada  llamada en este caso “archivo1” 
		la que debería ser modificada  dependiendo de la ubicación
		que el usuario 	quiera entregarle.

2.-  Abrir  el archivo “Parte2.proyecto2.py”, e inicializar.  

3.-  Al momento de inicializado el programa saldrán varias opciones la cual deberá elegir “escoger carpeta”, el cual  abrirá una ventana para ubicar  la carpeta contenedora de los archivos creados separados por fechas, luego de encontrada la carpeta apreté abrir( ubicado en la parte superior derecha).

4.- luego de cargada la carpeta seleccionada podrá ver como se cargaron todos los archivos que contenía dicha carpeta, seleccione un archivo y luego seleccione una fila que desee, para finalizar este paso apretar editar.

5.- ya presionado el botón editar se abrirá una “ventana de dialogo”, con la “unique_ID” en la parte superior de la fila seleccionada , la cual podrá ser editada, modificando la fecha con “Gtk.Calendar”, el rating y el comentario del paciente con ”Gtk.TextView”, para luego guardar los datos editados en el mismo “CSV” que fue  seleccionado previamente conservando el “unique_ID”

6.- En la Ventana de inicio podrá encontrar  un botón “acerca de”, el cual contiene los nombres de los creadores del programa.
