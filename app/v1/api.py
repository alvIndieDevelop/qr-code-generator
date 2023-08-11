from flask import Blueprint
from flask_restx import Api

blueprint_app_v1 = Blueprint("app_v1", __name__, url_prefix="/api/v1")
api_v1= Api(blueprint_app_v1, version="0.1", title="API V1", description="Api v1")

# import resources
from routes.ping import ping

# routes
api_v1.add_namespace(ping)
