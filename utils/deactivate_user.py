import requests

URL = "http://127.0.0.1:5002/vehicles"

def deactivate_vehicle(id):

    url=URL+"/"+id
    response = requests.delete(url)
    if response.status_code == 204:
        print (
            "Successfully deactivated vehicle; Got %s"
        )
    else:
        print("Something went wrong while deactivating record"
        )

if __name__ == "__main__":
    vmake = input("Type in the make of your vehicle: ")
    vmodel = input("Type in the model of your vehicle: ")
    fname = input("Type in the user's first name: ")
    lname = input("Type in the user's last name: ")
    deactivate_vehicle(vmake, vmodel, fname, lname)