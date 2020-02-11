import os
from . import configs
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

redis_store = FlaskRedis()

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(configs.Config)
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    jwt.init_app(app)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from .controllers import api_blueprint
    from .controllers import swaggerui_blueprint

    app.register_blueprint(swaggerui_blueprint, url_prefix=os.getenv('SWAGGER_URL'))
    app.register_blueprint(api_blueprint)

    return app
