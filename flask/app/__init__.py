import os
from datetime import datetime

from app import settings
from app.api.restx import api

from flask import Blueprint, Flask, current_app
from app.api.endpoints.test import ns as test_ns

application = Flask(__name__)


def configure_app(flask_app):
    # DB_HOST = os.getenv("DB_HOST")
    # DB_PORT = os.getenv("DB_PORT")
    # DB_DATABASE = os.getenv("DB_DATABASE")
    # DB_USER = os.getenv("DB_USER")
    # DB_PASSWORD = os.getenv("DB_PASSWORD")

    # flask_app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
    # flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['RESTX_SWAGGER_UI_DOC_EXPANSION'] = settings.RESTX_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTX_VALIDATE'] = settings.RESTX_VALIDATE
    flask_app.config['RESTX_MASK_SWAGGER'] = settings.RESTX_MASK_SWAGGER
    flask_app.config['RESTX_ERROR_404_HELP'] = settings.RESTX_ERROR_404_HELP
    # flask_app.config['SCHEDULER_JOBSTORES'] = {
    #     'default': SQLAlchemyJobStore(
    #         url=flask_app.config['SQLALCHEMY_DATABASE_URI'],
    #         tableschema=os.getenv('SCHEMA_NAME')
    #     ),
    # }
    # do not allow for api access job management
    # flask_app.config['SCHEDULER_API_ENABLED'] = False
    # flask_app.config['JOBS'] = [
    #     {
    #         'id': 'c2322554-7c8a-4540-99e9-2ded1ac4f75f',
    #         'func': run_queued_messages,
    #         'trigger': 'interval',
    #         'seconds': 5,
    #         'replace_existing': True
    #     }
    # ]
    # flask_app.config['SCHEDULER_EXECUTORS'] = {
    #     'default': {
    #         'type': 'threadpool', 
    #         'max_workers': 2
    #     }
    # }
    # flask_app.config['SCHEDULER_JOB_DEFAULTS'] = {
    #     'coalesce': False,
    #     'max_instances': 1
    # }


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(test_ns)

    flask_app.register_blueprint(blueprint)

    # db.init_app(flask_app)


initialize_app(application)
# db.application = application

# # scheduler = APScheduler()
# # scheduler.init_app(application)
# # scheduler.start()

