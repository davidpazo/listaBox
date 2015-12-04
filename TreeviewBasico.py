from gi.repositori import Gtk

class TreeviewBasico:
    def __init__(self):
        self.ventana = Gtk.window()
        self.ventana.set_title("Ejemplo basico de TreeView")
        self.ventana.set_size_request(200,200)
        self.ventana.connect("delete_event", self.cerrar_ventana)
        #Creamos el modelo
        self.treestore = Gtk.TreeStore(str)

    for padre in range (4):
        punteroPadre = self.treestore.append (None, ['Padre %i'% padre])
        for hijo in range(3):
            self.treestore.append(punteroPadre, ["Hijo %i del padre %i"%(hijo, padre)])
    #Creamos la vista y le asignamos el modelo
    self.treeview = Gtk.TreeView (self.treestore)
    self.tvcolumna = Gtk.TreeViewColumn('Columna 0')
    self.treeview.append_column(self.tvcolumna)
    self.celda = Gtk.CellRendererText()
    self.tvcolumna.pack_start(self.celda,True)
    self.tvcolumna.add_atribute(self.celda,'text',0)