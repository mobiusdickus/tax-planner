import os

from flask import Flask

from src import main, settings as S, utils as u


def create_app():
    # Create and configure the app
    app = Flask(__name__)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Register blueprints
    app.register_blueprint(main.bp)

    # Write client secret (service account json) to file
    u.decode_base64(S.CLIENT_SECRET_FILE, S.CLIENT_SECRET_FILENAME)

    return app
