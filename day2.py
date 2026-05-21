ev_stations = ["Uttarahalli", "Indiranagar", "Banashankari", "BTM"]
print(ev_stations[0:-1])

ev_stations[2] = "KHB Layout"
print(ev_stations)

ev_stations.append("AppendedStation")
print(ev_stations)

print(sorted(ev_stations))

print(ev_stations.pop())
print(ev_stations.index("Uttarahalli"))

ev_stations[0],ev_stations[-1] = ev_stations[-1],ev_stations[0]
print(ev_stations)

ev_stations = [station for station in ev_stations if len(station)<5]
print(ev_stations)