from gi.repository import Gtk, Gio
from gi.repository import Adw

@Gtk.Template(resource_path='/org/example/App/statuspage.ui')
class StatusPage(Adw.Bin):
    __gtype_name__ = 'StatusPage'

    #status_button: Gtk.Button = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.setup_actions()

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

