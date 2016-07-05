import sys
import datetime

class handler:
    def __init__(self, registry):
        # type: (object) -> object
        # type: (object) -> object
        self.registry = registry
        self.error_log_dir = self.registry.get("config").get("error_log_dir")
        self.type_ = "file"
        pass

    def error(self, output_type, text, location, sys_exit):
        t = datetime.time(1, 2, 3)
        d = datetime.date.today()
        localtime = datetime.datetime.combine(d, t)
        if output_type == "file":
            with open(self.error_log_dir, "a") as error_log:
                error_log.write("File  : " + location + "\nError : " + text + "\nTime  : " + str(localtime) )
                error_log.write("\n----------------------------------------- \n")
            if sys_exit:
                sys.exit()
        pass