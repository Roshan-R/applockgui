import os
import pylibconfig2 as cfg
from gi.repository import GLib

class Config:

    def __init__(self) -> None:
        self.config_file_path = GLib.get_user_config_dir() + "/app-lock/config"
        self.read_config()

    def read_config(self):
        with open(self.config_file_path) as f:
            text = f.read()
            self.c = cfg.Config(text)

    def handle_program(self, program:str):
        if program not in self.c.programs:
            self.add_program(program)
        else:
            self.remove_program(program)

    def add_program(self, program : str):
            print("[config] : adding ", program)
            self.c.programs.append(program)
            full_path = os.popen('which ' + program).read()
            program = full_path.strip('\n')
            self.c.programs.append(program)
            self.write_config()

    def remove_program(self, program : str):
            print("[config] : removing ", program)
            self.c.programs.remove(program)
            full_path = os.popen('which ' + program).read()
            program = full_path.strip('\n')
            self.c.programs.remove(program)
            self.write_config()

    def is_in_config(self, program: str):
            return program in self.c.programs

    def write_config(self):
        with open(self.config_file_path, 'w+') as f:
            f.write(str(self.c))

    
