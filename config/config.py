import os
import time
class config:
    def __init__(self):
        self.config_ = {}
        self.config_['base'] = os.getcwd()
        self.config_['server'] = "http://localhost/"
        self.config_['port'] = 80
        self.config_['path'] = "robot/"
        self.config_['req_url'] = self.config_['server'] + self.config_['path'] + "requests?data="
        self.config_['auther'] = "5G LAB - Seyyedmohammad hosseini"
        self.config_['version']  = "1.0.0.0"
        self.config_['startTime'] = "04.25.2016"
        self.config_['timer_functions'] = ['printer']
        self.config_['error_log_dir'] = self.config_['base'] + "/log/error.txt"
        self.config_['modules_dir'] = self.config_['base'] + "/modules/"
        self.config_['module_loader'] = "__init__.py"
        self.config_['defaultRobotSpeed'] = 100
        pass

    def get(self, key):
        if self.config_.has_key(key):
            return self.config_[key]
        else:
            return False

    def set(self, key, value):
        if not self.config_.has_key(key):
            self.config_[key] = value
            return True
        else:
            return False

    def update(self, key, value):
        if self.config_.has_key(key):
            self.config_[key] = value
            return True
        else:
            return False


