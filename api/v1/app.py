#!/usr/bin/python3

from flask import Flask
from api.v1.views import app_views
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Teardown app context"""
    storage.close()


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')
    app.register_blueprint(app_views, url_prefix="/api/v1")
    app.run(host=host, port=port, threaded=True)
