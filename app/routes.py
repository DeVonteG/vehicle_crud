from flask import(
    Flask,
    request
)


from datetime import datetime

from app.database import vehicle

VERSION = '1.0.0'

app = Flask(__name__)

@app.get("/ping")
def get_ping():
    response = {
        'status': 'ok',
        'message': 'pong'
    }
    return response


@app.get("/version")
def get_version():
    response = {
        "status": 'ok',
        'version': VERSION,
        "server_time": datetime.now().strftime("%F %H:%M:%S")
    }
    return response


@app.get("/vehicles")
def get_all_vehicles():
    vehicle_list = vehicle.scan()
    out = {
        "status": "ok",
        "vehicles": vehicle_list
    }
    return out


@app.get("/vehicles/<int:pk>")
def get_vehicle_by_id(pk):
    vehic_obj = vehicle.select_by_id(pk)
    out = {
        "status": "ok",
        "vehicle": vehic_obj
    }
    return out


@app.post("/vehicles")
def create_vehicle():
    raw_data = request.json
    vehicle.insert(raw_data)
    out = {
        "status": "ok",
        "message": "created"
    }
    return out, 201

@app.put("/vehicles/<int:pk>")
def update_vehicle(pk):
    raw_data = request.json
    vehicle.update(pk, raw_data)
    return "", 204

@app.delete("/vehicles/<int:pk>")
def deactivate_vehicle(pk):
    vehicle.deactivate(pk)
    return "", 204