import requests
import json

class connection:
    def __init__(self, register):
        self.config = register.get("config")
        self.report = register.get("log")
        self.socket = register.get("socket")
        self.req_url = self.config.get("req_url");
        self.sock = None
        pass

    def send(self, parameters):
        parameters['ip'] = self.socket.get_ip()
        headers = {'content-type': 'application/json'}
        url = self.req_url + json.dumps(parameters)
        r = requests.get(url, headers=headers)
        print r.text
        pass

