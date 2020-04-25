from um3api import Ultimaker3
import time

HOST = "" # UM3 IP goes here

api = Ultimaker3(HOST, "statecheck")

while True:
    status = api.get("api/v1/printer/status").json()
    state = api.get("api/v1/print_job/state").json()
    print("status = " + status)
    print("state = " + str(state))
    print()
    time.sleep(1)
