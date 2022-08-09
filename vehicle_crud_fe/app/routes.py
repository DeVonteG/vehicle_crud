from flask import (Flask, render_template )

import requests
URL = "http://127.0.0.1:5000/vehicles"

app = Flask(__name__)

@app.get("/")
def get_index():
    return render_template("index.html")

@app.get("/vehicles")
def display_vehicles():
    vehicle_list= requests.get(URL).json()
    return render_template(
        "vehicles.html", vehicles= vehicle_list.get("vehicles")
    )

@app.get("/vehicles/<int: pk>")
def display_vehicle_profile(pk):
    url = "%s/%s" % (URL, pk)
    response = requests.get(url)
    vehicle_json= response.json().get("vehicle")[0]
    return render_template("vehicle.html", vehicle = vehicle_json)
