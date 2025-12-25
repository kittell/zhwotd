import json
import os
from zhwotd.gui import GUI

class Application:
    def __init__(self):
        self.config = self._load_config()
        print(self.config)
        return
    
    def _load_config(self):
        config = dict()
        f_dir = os.path.dirname(__file__)
        f_name = 'config.json'
        f_fullpath = os.path.join(f_dir, f_name)
        with open(f_fullpath, 'r') as f: 
            config = json.load(f)
        return config

    def start(self):
        gui = GUI(self, self.config)
        return