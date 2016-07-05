import os
import sys
import importlib
import string

class loader:
    def __init__(self, registry):
        self.data_ = registry
        self.config = registry.get("config")
        self.report = registry.get("log")
        self.modules_path = self.config.get("modules_dir")
        self.active_module = self.config.get("active_module")
        self.active_module_dir = self.modules_path + self.active_module + "/"
        self.module_loader = self.config.get("module_loader")
        self.module_loader_path = self.active_module_dir + self.module_loader
        pass

    def controller(self):
        self.checkModuleExist()
        self.checkModuleLoader()
        self.loadModuler()
        pass

    def checkModuleExist(self):
        modules = [name for name in os.listdir(self.modules_path) if os.path.isdir(self.modules_path + name)]
        if self.active_module not in modules:
            print "Module (" + self.active_module + ") Not Exist"
            self.report.error("file", "Module (" + self.active_module + ") Not Exist", "engine/static/loader", True)
        pass

    def loadModuler(self):
        sys.path.insert(1, self.modules_path)
        try:
            my_module = importlib.import_module(self.active_module)
        except:
            print "Import Module Error"
            self.report.error("file", "Import Module -> " + self.active_module + " Error", "engine/static/loader", True)
        globals()["load_module_data"] = my_module
        try:
            load_module_data.controller(self.data_)
        except:
            print "Class Controller Not Exist : " + str(self.data_) 
            self.report.error("file", "Class Controller Not Exist : " + str(self.data_), "engine/static/loader", True)

    def checkModuleLoader(self):
        files = [name for name in os.listdir(self.active_module_dir) if os.path.isfile(self.active_module_dir + name)]
        if self.module_loader not in files:
            print self.active_module + " -> " + self.module_loader + " Not Exist"
            self.report.error("file", self.active_module + " -> " + self.module_loader + " Not Exist", "engine/static/loader", True)
        pass
