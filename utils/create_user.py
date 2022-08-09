import requests

URL = "http://127.0.0.1:5002/vehicles"

def create_vehicle(make, model, owner_first, owner_last):
    owner={
        "make": make,
        "model": model,
        "owner_first": owner_first,
        "owner_last": owner_last,
    }
    response = requests.post(URL, json=owner)
    if response.status_code == 201:
        print(
            "Successfully created a new user; Got: %s"
            % response.json().get("message")
        )
    else:
        print(
            "Something went wrong while creating a new user."
        )

if __name__ == "__main__":
    vmake = input("Type in make of your vehicle: ")
    vmodel = input("Type in your model of your vehicle: ")
    fname = input("Type in users first name: ")
    lname = input("Type in users last name: ")
    create_vehicle(vmake, vmodel, fname, lname)