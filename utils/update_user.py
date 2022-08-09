import requests

URL = "http://127.0.0.1:5002/vehicles"

def update_vehicle(id,make,model,owner_first,owner_last):
    user= {
        "make":make,
        "model":model,
        "owner_first":owner_first,
        "owner_last":owner_last
    }
    url = URL+"/"+id
    response = requests.put(url, json=user)
    if response.status_code == 204:
        print (
            "Successfully updated vehicle record; Godt %s"
        )
    else:
        print(
            "Something went wrong while updating vehicle record"
        )

if __name__ == "__main__":
    uid = input("Type in users id: ")
    vmake = input("Type in make of your vehicle: ")
    vmodel = input("Type in model of your vehicle: ")
    fname = input("Type in users first name: ")
    lname = input("Type in users last name: ")
    update_vehicle(uid, vmake, vmodel, fname, lname)