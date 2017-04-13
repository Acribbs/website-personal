from flask import Flask
from flask_googlemaps import GoogleMaps
from flask_compress import Compress

app = Flask(__name__)
Compress(app)
from app import views

GoogleMaps(app, key="AIzaSyBKZ8HTbkOmKT2oaJ_8p8djs02C4OlF44I")

