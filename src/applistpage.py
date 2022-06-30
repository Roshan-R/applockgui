from gi.repository import Gtk, Gio, GLib
from gi.repository import Adw

from .config import Config

@Gtk.Template(resource_path='/org/example/App/applistpage.ui')
class ApplistPage(Adw.Bin):
    __gtype_name__ = 'ApplistPage'

    listbox : Gtk.ListBox = Gtk.Template.Child()
    searchentry : Gtk.SearchEntry = Gtk.Template.Child()
    #application_name : Gtk.Label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.appinfo = {}

        self.config = Config()

        applist = Gio.AppInfo.get_all()
        for app in applist:
            name = app.get_display_name()
            icon = app.get_icon()
            if type(icon) != Gio.FileIcon and type(icon) != type(None):
                icon = icon.get_names()[0]
            else:
                icon = ""
            description = app.get_description()
            executable = app.get_executable()
            self.appinfo[name] = {"description":description, "icon":icon, "executable":executable}
            row = self.create_row(name, icon, description, executable)
            self.listbox.prepend(row)
        # print(self.appinfo)
        # print(GLib.get_user_config_dir() + "/applock-gui")
        self.listbox.set_filter_func(self.filter_func, None, False)
        #self.application_name.set_text(app.get_display_name())
        #self.icon_application.set_from_gicon(app.get_icon())
        self.searchentry.connect("search-changed", self.searcher)

    def searcher(self, _a):
        self.listbox.invalidate_filter()

    def filter_func(self, row, _b, _c):
        a = row.get_title().lower().find(self.searchentry.get_text().lower())
        return not a

    def handle_switch(self, _a):
        row = _a.get_parent().get_parent().get_parent()
        title = row.get_title()
        # print(self.appinfo[title]["executable"])
        self.config.handle_program(self.appinfo[title]["executable"])

    def create_row(self, title, icon, subtitle, executable):
        actionrow = Adw.ActionRow()
        actionrow.set_title(title)
        actionrow.set_icon_name(icon)
        if subtitle:
            actionrow.set_subtitle(subtitle)
        switch = Gtk.Switch()
        if self.config.is_in_config(executable):
            switch.set_state(True)
        switch.set_valign(Gtk.Align.CENTER)
        actionrow.add_suffix(switch)
        switch.connect("activate", self.handle_switch)
        actionrow.set_activatable_widget(switch)
        return actionrow
