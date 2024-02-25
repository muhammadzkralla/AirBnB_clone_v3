#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def api_status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})
