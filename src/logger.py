from logging.config import dictConfig
from os import mkdir
from os.path import exists


class FlaskLoggerConfig:

    __FMT = "%(asctime)s %(levelname)s: %(message)s"
    __DATEFMT = "%d-%m-%Y %H:%M:%S"
    __FOLDER = ".logs"
    __CONFIG = {
        "version": 1,
        "formatters": {
            "default": {
                "format": __FMT,
                "datefmt": __DATEFMT,
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
    __FILE = {
        "class": "logging.handlers.TimedRotatingFileHandler",
        "filename": f"{__FOLDER}/records.log",
        "when": "D",
        "interval": 1,
        "formatter": "default",
    }

    def __init__(self, logging_file: bool) -> None:
        config = self.__CONFIG

        if logging_file:
            if not exists(self.__FOLDER):
                mkdir(self.__FOLDER)

            config["handlers"].setdefault("time-rotate", self.__FILE)
            config["root"]["handlers"].append("time-rotate")

        dictConfig(config)
