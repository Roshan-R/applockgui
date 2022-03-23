from gi.repository import Gtk, Gio
from gi.repository import Adw


@Gtk.Template(resource_path='/org/example/App/applistpage.ui')
class ApplistPage(Adw.Bin):
    __gtype_name__ = 'ApplistPage'

    listbox : Gtk.ListBox = Gtk.Template.Child()
    searchentry : Gtk.SearchEntry = Gtk.Template.Child()
    #application_name : Gtk.Label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        applist = Gio.AppInfo.get_all()
        for app in applist:
            name = app.get_display_name()
            icon = app.get_icon()
            if icon:
                icon = icon.get_names()[0]
            description = app.get_description()
            row = self.create_row(name, icon, description)
            switch = Gtk.Switch()
            switch.set_valign(Gtk.Align.CENTER)
            row.add_suffix(switch)
            row.set_activatable_widget(switch)
            self.listbox.prepend(row)
        self.listbox.set_filter_func(self.filter_func, None, False)
        #self.application_name.set_text(app.get_display_name())
        #self.icon_application.set_from_gicon(app.get_icon())

        self.searchentry.connect("search-changed", self.searcher)

    def print(self, _a, _b):
        print(_a, _b)

    def searcher(self, _a):
        self.listbox.invalidate_filter()

    def filter_func(self, row, _b, _c):
        a = row.get_title().lower().find(self.searchentry.get_text().lower())
        return not a

    def create_row(self, title, icon, subtitle):
        actionrow = Adw.ActionRow()
        actionrow.set_title(title)
        actionrow.set_icon_name(icon)
        if subtitle:
            actionrow.set_subtitle(subtitle)
        return actionrow

