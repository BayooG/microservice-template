import logging
import os

from logging.handlers import RotatingFileHandler

from dotenv import load_dotenv
from distutils.util import strtobool



from flask_script import Server, Manager
from app import application 
from debugger import initialize_flask_server_debugger_if_needed


manager = Manager(application)
manager.add_command("debug", Server(port=5000, use_debugger=True, host='0.0.0.0'))

load_dotenv()

if __name__ == "__main__":
    file_handler = RotatingFileHandler('./error.log', maxBytes=1024 * 1024 * 100, backupCount=20)

    # if bool(strtobool(os.getenv('DEBUG'))):
    #     application.logger.setLevel(logging.DEBUG)
    #     file_handler.setLevel(logging.DEBUG)
    # else:
    application.logger.setLevel(logging.WARN) 
    file_handler.setLevel(logging.WARN)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    application.logger.addHandler(file_handler)

    initialize_flask_server_debugger_if_needed()
    manager.run()