class controller:
    def __init__(self, action):
        self.robot = action.get("robot")
        self.config = action.get("config")
        self.report = action.get("log")
        self.socket = action.get("socket")
        self.timer = action.get("timer")
        self.line = action.get("line")
        self.video = action.get("video")
        self.socket_ = action.get("socket")
        self.http_connection = action.get("http")
        self.run_request()
        pass

    def run_request(self):
        self.http_connection.send({"name": "mohammad"})
        pass

    def run_socket(self):
        _image = self.video.onlineImage("rgb")
        encode = self.video.doEncoding(_image, 100)
        self.socket_.create(encode)
        quit()
        pass

    def run_video(self):
        _image = self.video.onlineImage("gray")
        encode = self.video.doEncoding(_image, 100)
        decode = self.video.doDecoding(encode)
        self.video.drowImage("After Encoding", decode)
        pass

    ''' Main _run_ --> SPM'''
    def run_main(self):
        # self.robot.forward()
        # self.timer.wait(2)
        # self.robot.goStop()
        flag = True

        while True:
                if flag:
                    self.robot.forward()
                    flag = False
                finish = self.line.finish()
                position = self.line.position()
                print position
                if position[0] == "left":
                    self.robot.goStop()
                    self.robot.goRight()
                    self.timer.wait(0.1)
                    self.robot.goStop()
                    flag = True
                    continue
                elif position[0] == "right":
                    self.robot.goStop()
                    self.robot.goLeft()
                    self.timer.wait(0.1)
                    self.robot.goStop()
                    flag = True
                    continue
                if finish:
                    self.timer.wait(0.01)
                    finish = self.line.finish()
                    if finish:
                        self.robot.goStop()
                        self.sendRequestToServer("intersection_permission")
                        break

        print "Finish Module"
        pass

    def sendRequestToServer(self, _request_):
        if _request_ == "intersection_permission":
            print "send request to server please wait ..."
        pass

    
