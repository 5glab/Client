from threading import Timer,Thread,Event
import time
class timer():

    def __init__(self, registry):
        self.config = registry.get("config")
        self.steps_true = None
        self.validFunction = None
        self.timer = None
        self.hFunction = None
        self.steps = None
        self.counter = 0
        self.isdone = False
        self.thread = None

    def runFunction(self, timer, hFunction, steps_true,steps):
        self.steps_true = steps_true
        self.validFunction = self.config.get("timer_functions")
        self.timer = timer
        self.hFunction = hFunction
        self.steps = steps
        self.thread = Timer(self.timer, self.handle_function)
        pass

    def check_function_exist(self):
        if self.hFunction not in self.validFunction:
            print "Function : ", self.hFunction  ,"is not valid"
            self.setDone()
            self.cancel()
            return False

    def handle_function(self):
        self.check_function_exist()

        if self.hFunction == "printer":
            if self.steps_true and self.counter < self.steps:
                self.printer()
            elif not self.steps_true:
                self.printer()
        self.checkSteps()
        if not self.checkDone():
            self.thread = Timer(self.timer, self.handle_function)
            self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
      self.thread.cancel()

    def printer(self):
        print "Timer | Step : ", self.counter

    def isDone(self):
        return self.isdone

    def setDone(self):
        self.isdone = True

    def checkDone(self):
        if self.isDone():
            self.cancel()
            return True

    def checkSteps(self):
        if self.steps_true:
            self.counter += 1
        if self.steps_true and self.counter == self.steps:
            self.setDone()

    def wait(self, timer_):
        time.sleep(timer_)
        pass