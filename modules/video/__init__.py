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
        self.calculate = action.get("calculate")
        self.run_video()
        pass

    def run_video(self):
        _image = self.video.onlineImage("gray")
        #self.video.drowImage("Pic",_image)
        new_ = self.video.whiteAndBlackImage(_image,30)
        _status = self.calculate.imageThreshold(_image,30)
        self.video.drowImage("Pic",new_)
        
        if _status == "right":
            self.robot.goRight()
            self.timer.wait(0.5)
            self.robot.forward()
            self.timer.wait(0.35)
            self.robot.goLeft()
            self.timer.wait(0.5)
            self.robot.forward()
        if _status == "left":
            self.robot.goLeft()
            self.timer.wait(0.5)
            self.robot.forward()
            self.timer.wait(0.35)
            self.robot.goRight()
            self.timer.wait(0.5)
            self.robot.forward()
        if _status == "stright":
            self.robot.forward()
        print _status
        self.timer.wait(2)
        self.robot.goStop()
        pass
