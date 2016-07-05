import numpy as np
class calculate:
    def __init__(self, registry):
        self.config = registry.get("config")
        self.report = registry.get("log")
        pass
    def new_abs(self,number):
        if number < 0:
            return -1 * number
        else:
            return number
    def imageThreshold(self, image,throshold):
        dimensional = np.array(image)
        (d1, d2) = np.shape(dimensional)
        print (d1,d2)
        flag = False
        x = [0,0,0,0]
        t = 0;
        for i in range(2,3):
            for j in range(d2):
                if image[i][j] < throshold:
                    if not flag:
                        if t<4:
                            x[t] = j
                            t = t + 1
                        flag = True
                else:
                    if flag:
                        flag = False
        flag = False
        for j in range(d2):
            if image[40][j] < throshold:
                if not flag:
                    if(t<4):
                        x[t] = j
                        t = t+1
                    flag = True                  
            else:
                if flag:
                    flag = False
        print x
        val1 = self.new_abs(x[0]-x[2])
        val2 = self.new_abs(x[1]-x[3])
        print (val1,val2)
        if(val1>35 and val2<25):
            return "left"
        if(val1<27 and val2>25):
            return "right"
        return "stright"
