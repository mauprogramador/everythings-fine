from os import getenv

import dotenv  # pylint: disable=w0611 # noqa: F401
import flask  # pylint: disable=w0611 # noqa: F401
import flask_cors  # pylint: disable=w0611 # noqa: F401
from dotenv import load_dotenv

from src.app import app


if __name__ == "__main__":
    load_dotenv()
    port = int(getenv("PORT", "2004"))
    app.logger.info("Everything's Okay was initialized 🚀")
    app.run(host="0.0.0.0", port=port, load_dotenv=True)
