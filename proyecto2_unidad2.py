import os
import pandas
# Se importa la librería Gobject Instrospection (gi)
import gi
from os.path import isfile, join
# Importa Gtk
from gi.repository import Gtk
from clase_filechooser import clasfilechooser
# Selecciona que la versión de GTK a trabajar (3.0)
gi.require_version("Gtk", "3.0")


# se lista el contenido de una ruta
def listar(ruta):

    contenido = os.listdir(ruta)
    archivos = [nombre for nombre in contenido if isfile(join(ruta, nombre))]

    return archivos


class ventana_inicio:
    def __init__(self):
        self.builder = Gtk.Builder()
        # se selecciona archivo.ui del que se extrae la interfaz
        self.builder.add_from_file("proyecto2.ui")

        # se crea ventana principal
        self.ventana = self.builder.get_object("ventana_principal")
        self.ventana.set_default_size(850, 650)
        self.ventana.set_title("archivos")
        self.ventana.connect("destroy", Gtk.main_quit)

        # se crea boton encargado de abrir file chooser
        btn_abrir = self.builder.get_object("btn_abrir")
        btn_abrir.connect("clicked", self.abrir_filechooser)
        btn_abrir.set_label("escoger carpeta")

        # se llama a comboboxtext
        self.seleccion_año = self.builder.get_object("eleccion_año")

        # se llama a treeview y se le asigna que se active 
        # con un solo click
        self.treeview = self.builder.get_object("tree_view")
        self.treeview.connect("row-activated", self.tree_row_activated)
        self.treeview.set_activate_on_single_click(True)

        self.label_review = self.builder.get_object("review")
        self.label_review.set_label("")

        btn_editar = self.builder.get_object("btn_editar")
        btn_editar.connect("clicked", self.abrir_editar)

        btn_acercad = self.builder.get_object("btn_acercad")
        btn_acercad.connect("clicked", self.ventana_acercad)

        self.ventana.show_all()

    # funcion llama a ventana de dialogo en donde
    # se muestran los nombres de los creadores
    def ventana_acercad(self, btn=None):
        ventana_acerca = ventana_acercade()

    # funcion abre ventana editar al llamar a clase ventanaedit
    def abrir_editar(self, btn=None, mode=None):
        abrir_vntn_editar = ventanaedit()
        abrir_vntn_editar

    # función abre ventana file chooser
    def abrir_filechooser(self, btn=None, mode=None):
        file_chooser_abrir = clasfilechooser(mode)
        filechooser = file_chooser_abrir.filechooser

        # se añaden filtros para que file chooser
        # solo deje escoger carpetas
        filtro = Gtk.FileFilter()
        filtro.add_mime_type("folder")
        filtro.set_name("archivos")
        filtro.add_pattern("*")
        filechooser.add_filter(filtro)

        response = filechooser.run()

        # se le añaden acciones a botones
        if response == Gtk.ResponseType.OK:
            # se crea variable que almacenara opciones
            # en gtk.comboboxtext
            # la variable es limpiada para poder
            # almacenar solo las variables de la carpeta deseasa
            model = self.seleccion_año.get_model()
            model.clear()
            # se obtiene la ruta de la carpeta seleccionada,
            # se lista el contenido de la carpeta y
            # se le entrega a comboboxtext
            self.ruta = filechooser.get_current_folder()
            archivos = listar(self.ruta)
            for item in archivos:
                self.seleccion_año.append_text(item)
            self.seleccion_año.set_active(0)
            # al seleccionar un archivo de comboboxtext
            # se llama a la funcion creavista
            self.seleccion_año.connect("changed", self.creavista)
            filechooser.destroy()
        elif response == Gtk.ResponseType.CANCEL:
            filechooser.destroy()

    def creavista(self, path_file):
        self.archivo = self.seleccion_año.get_active_text()
        # se crea ruta de archivo
        path = self.ruta + "/" + self.archivo
        # lee el archivo csv
        data = pandas.read_csv(path)

        # se obtienen columnas de archivo
        if self.treeview.get_columns():
            for column in self.treeview.get_columns():
                self.treeview.remove_column(column)

        largo_columnas = len(data.columns)
        modelo = Gtk.ListStore(*(largo_columnas * [str]))
        self.treeview.set_model(model=modelo)

        cell = Gtk.CellRendererText()

        # se muestra contenido de archivo en pantalla
        for item in range(len(data.columns)):
            column = Gtk.TreeViewColumn(data.columns[item], cell, text=item)
            self.treeview.append_column(column)
            column.set_sort_column_id(item)
            if item == 3:
                # Se ocultan las columnas
                column.set_visible(False)

        for item in data.values:
            line = [str(x) for x in item]
            modelo.append(line)

        activado = self.treeview.get_selection()

    # funcion se encarga de mostrar columna review
    # de fila elegida en el label
    def tree_row_activated(self, model, path, iter_):

        self.model, it = self.treeview.get_selection().get_selected()
        if self.model is None:
            return False
        # Cada cambio de cursor se vera en el Gtk.Label
        text = "<b>Dato: </b> \n\n"
        text = f"{text}<b>{self.treeview.get_column(3).get_title()}: </b>\n"
        text = f"{text} {self.model.get_value(it, 3)}"
        text = f"{text}\n"
        # Aplica texto concatenado al label, con los valores de las
        # columnas ocultas del tree
        self.label_review.set_markup(text)


# clase ventana de edicion de datos
class ventanaedit:
    def __init__(self):

        self.builder = Gtk.Builder()
        self.builder.add_from_file("proyecto2.ui")
        self.ventanadialogo = self.builder.get_object("ventana_dialogo")
        self.ventanadialogo.set_title("cambiar datos")

        # se crean labels para mostrar id unico
        self.label_id = self.builder.get_object("nombre_id")
        self.label_id.set_label("id unico: ")
        self.id_unico = self.builder.get_object("id_unico")
        self.id_unico.set_label("")

        # se llama a calendario
        self.label_calendar = self.builder.get_object("calendari")
        self.label_calendar.set_label("calendario: ")
        self.calendar = self.builder.get_object("calendario")

        
        self.label_rating = self.builder.get_object("rating")
        self.label_rating.set_label("rating: ")

        self.rating_entrada = self.builder.get_object("entrada_rating")
        self.label_comentario = self.builder.get_object("comentario_paciente")
        self.label_comentario.set_label("Comentario paciente: ")

        self.ventanadialogo.show_all()

# clase encargada de mostrar ventana de dialogo
# en donde se muestra nombre de los creadores 
class ventana_acercade:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("proyecto2.ui")
        # se abre ventana de dialogo
        self.ventanadialogo = self.builder.get_object("acercade")
        self.ventanadialogo.set_title("Acerca de")
        # se le asignan los nombres de los creadores al label
        self.label_acerca = self.builder.get_object("acerca_d")
        self.label_acerca.set_label(
            "creadores: \n Denise valdés \n Sebastian Benavides"
        )

        self.ventanadialogo.show_all()


if __name__ == "__main__":
    ventana_inicio()
    Gtk.main()
