from gi.repository import Gtk, Gio
from gi.repository import Adw

@Gtk.Template(resource_path='/org/example/App/actionrow.ui')
class ActionRow(Gtk.Box):
    __gtype_name__ = 'ActionRow'

    title : Gtk.Label = Gtk.Template.Child()
    subtitle : Gtk.Label = Gtk.Template.Child()
    image : Gtk.Image = Gtk.Template.Child()
    switch : Gtk.Switch = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_title(self):
        return self.title.get_text()

    def set_title(self, text: str):
        self.title.set_text(text)

    def set_subtitle(self, text: str):
        self.subtitle.set_text(text)

    def set_icon(self, gicon):
        if gicon == None:
            pass
        else:
            self.image.set_from_gicon(gicon)
    
