from flask import Flask

from .controllers import entry_controller

def create_app():
    app = Flask(__name__)

    # Import and register Blueprints
    from .controllers import auth, user
    app.register_blueprint(auth.bp)
    app.register_blueprint(entry_controller.bp)
    app.register_blueprint(user.bp)

    return app
