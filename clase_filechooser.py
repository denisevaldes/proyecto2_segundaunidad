import gi
# Importa Gtk
from gi.repository import Gtk
# Selecciona que la versión de GTK a trabajar (3.0)
gi.require_version("Gtk", "3.0")


class clasfilechooser:

    def __init__(self, mode="open_mode"):
        builder = Gtk.Builder()
        builder.add_from_file("proyecto2.ui")
        # se abre file chooser
        self.filechooser = builder.get_object("filechooser")

        # se crean botones
        self.filechooser.add_buttons(
                        Gtk.STOCK_CANCEL,
                        Gtk.ResponseType.CANCEL,
                        Gtk.STOCK_OPEN,
                        Gtk.ResponseType.OK,
                        )
        self.filechooser.set_action(Gtk.FileChooserAction.SELECT_FOLDER)
        self.filechooser.show_all()
