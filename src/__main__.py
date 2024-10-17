from os import getenv

import dotenv  # pylint: disable=w0611 # noqa: F401
import flask  # pylint: disable=w0611 # noqa: F401
import flask_cors  # pylint: disable=w0611 # noqa: F401
from dotenv import load_dotenv

from src.app import app
from src.logger import FlaskLoggerConfig


load_dotenv()
PORT = int(getenv("PORT", "2004"))
LOGGING_FILE = bool(getenv("LOGGING_FILE", None))


if __name__ == "__main__":
    FlaskLoggerConfig(LOGGING_FILE)
    app.logger.info("\033[93mEverything's Fine was initialized 🚀\033[m")
    app.run(host="0.0.0.0", port=PORT, load_dotenv=True)
