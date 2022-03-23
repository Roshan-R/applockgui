from gi.repository import Gtk, Gio
from gi.repository import Adw


@Gtk.Template(resource_path='/org/example/App/settingspage.ui')
class SettingsPage(Adw.Bin):
    __gtype_name__ = 'SettingsPage'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
