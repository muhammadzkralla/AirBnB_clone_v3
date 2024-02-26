#!/usr/bin/python3
"""
Start listening
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
classes = {"amenities": Amenity, "cities": City, "places": Place,
           "reviews": Review, "states": State, "users": User}


@app_views.route("/status", strict_slashes=False)
def status():
    """respond with OK for /status"""
    j_status = {"status": "OK"}
    return jsonify(j_status)


@app_views.route("/stats", strict_slashes=False)
def count_all():
    """respond with OK for /stats"""
    return jsonify({
        name: storage.count(obj) for name, obj in classes.items()
    })
