from config import config
from engine.static import registry
from engine.static import session
from engine.static import loader
from engine.static import robot
from engine.static import line
from engine.static import timer
from engine.static import log
from engine.static import video
from engine.static import calculate
from engine.static.connection import socket_connection
from engine.static.connection import http_connection

class index:
    def __init__(self):

        registry_ = registry.registry()

        config_ = config.config()
        config_.set("active_module", "video")
        registry_.set("config", config_)

        log_ = log.handler(registry_)
        registry_.set("log", log_)

        timer_ = timer.timer(registry_)
        registry_.set("timer",timer_)

        session_ = session.sessions()
        registry_.set("session", session_)

        socket_ = socket_connection.connection(registry_)
        registry_.set("socket", socket_)

        http_ = http_connection.connection(registry_)
        registry_.set("http", http_)

        calculate_ = calculate.calculate(registry_)
        registry_.set("calculate", calculate_)

        video_ = video.video(registry_)
        registry_.set("video", video_)

        robot_ = robot.robot(registry_)
        registry_.set("robot", robot_)

        line_ = line.line(registry_)
        registry_.set("line", line_)

        loader_ = loader.loader(registry_)
        registry_.set("loader", loader_)

        registry_.run()
        pass
index()
