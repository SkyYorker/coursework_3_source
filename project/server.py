from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, render_template
from flask_restx import Api


from project.exceptions import BaseServiceError
from project.setup.api import api
from project.setup.db import db
from project.views import auth_ns, genres_ns, user_ns, movies_ns, directors_ns


def base_service_error_handler(exception: BaseServiceError):
    return jsonify({'error': str(exception)}), exception.code




def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)


    @app.route('/')
    def index():
        return render_template('index.html')

    CORS(app=app)
    db.init_app(app)
    api.init_app(app)

    # Регистрация эндпоинтов
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)


    app.register_error_handler(BaseServiceError, base_service_error_handler)

    return app


