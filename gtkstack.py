__author__ = 'dpazolopez'

from gi.repository import Gtk

class StackWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Ejemplo Stack")
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

        checkbutton = Gtk.CheckButton("PULSA!")
        stack.add_titled(checkbutton, "pulsa", "Boton de chequeo")

        label = Gtk.Label()
        label.set_markup("<big>Una etiqueta</big>")
        stack.add_titled(label, "Etiqueta", "Una etiqueta")

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        vbox.pack_start(stack_switcher, True, True, 0)
        vbox.pack_start(stack, True, True, 0)

win = StackWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()