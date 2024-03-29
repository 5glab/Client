import os
class registry:
    def __init__(self):
        self.data_ = {}
        self.config = None
        self.loader = None
        pass

    def get(self, key):
        if self.data_.has_key(key):
            return self.data_[key]
        else:
            return False

    def set(self, key, value):
        self.data_[key] = value

    def has(self, key):
        if self.data_.has_key(key):
            return True
        else:
            return False
        pass

    def analysis(self):
        self.config = self.data_['config']
        self.loader = self.data_['loader']
        pass

    def run(self):
        self.analysis()
        self.loader.controller()
        pass
