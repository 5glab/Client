    import httplib
    import json

    def getText(txt):
        lines = txt.split('\n')
        for line in lines:
            return line.strip()

    def sendRequest(server,port,path,method):
        headers = {'Content-Type': 'application/json'}
        httpServ = httplib.HTTPConnection(server,port)
        httpServ.connect()
        httpServ.request(method,path,"",headers)
        response = httpServ.getresponse()
        if response.status == httplib.OK:
            Result = getText(response.read())
            Result = str(Result)
            print Result
        else:
            print False
        httpServ.close();