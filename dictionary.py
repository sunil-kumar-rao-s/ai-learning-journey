ev_stations = {
    "charger1": {"uid": "001", "location": "BTM", "kwh": 3.7},
    "charger2": {"uid": "002", "location": "BSK", "kwh": 7.2},
}

status_msg = "charger1 is currently online "
msg = status_msg.split()
ev_stations[msg[0]]["status"] = msg[-1]
print(ev_stations)

for key, station in ev_stations.items():
    if "status" not in station:
        station["status"] = "not yet connected"

print(ev_stations)

for station in ev_stations.values():
    if station["kwh"] < 5:
        station["size"] = "small"
    station["kwh"] = "medium"

print(ev_stations)
