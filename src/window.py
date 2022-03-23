# window.py
#
# Copyright 2022 Camila Martinez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk, Gio
from gi.repository import Adw

import subprocess

Adw.init()


@Gtk.Template(resource_path='/org/example/App/window.ui')
class GnomeAppWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'GnomeAppWindow'

    view_switcher : Adw.ViewSwitcherTitle = Gtk.Template.Child()
    stack : Adw.ViewStack = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.view_switcher.set_stack(self.stack)


@Gtk.Template(resource_path='/org/example/App/statuspage.ui')
class StatusPage(Adw.Bin):
    __gtype_name__ = 'StatusPage'

    status_button: Gtk.Button = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup_actions()

    def setup_actions(self):
        self.status_button.connect("clicked", self.print_clicked)

    def update_running_status(self):
        if subprocess.Popen('pidof applock', shell=True, stdout=subprocess.PIPE).stdout.read():
            print('app is running')
        else:
            print('not running')

    def print_clicked(self, _a):
        print("hello bois")
        self.update_running_status()

@Gtk.Template(resource_path='/org/example/App/settingspage.ui')
class SettingsPage(Adw.Bin):
    __gtype_name__ = 'SettingsPage'

    listbox : Gtk.ListBox = Gtk.Template.Child()
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
            self.listbox.prepend(row)
        #self.application_name.set_text(app.get_display_name())
        #self.application_icon.set_from_gicon(app.get_icon())

    def create_row(self, title, icon, subtitle):
        actionrow = Adw.ActionRow()
        actionrow.set_title(title)
        actionrow.set_icon_name(icon)
        if subtitle:
            actionrow.set_subtitle(subtitle)
        return actionrow

class AboutDialog(Gtk.AboutDialog):

    def __init__(self, parent):
        Gtk.AboutDialog.__init__(self)
        self.props.program_name = 'gnome-app'
        self.props.version = "0.1.0"
        self.props.authors = ['Camila Martinez']
        self.props.copyright = '(C) 2021 Camila Martinez'
        self.props.logo_icon_name = 'org.example.App'
        self.set_transient_for(parent)
