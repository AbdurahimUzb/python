def route_info(distance):

    dis = distance.get("distance")
    speed = distance.get("speed")
    time = distance.get("time")

    if distance and time:
        print(
            f"Distance to your destination is {speed * time}")
    elif dis:
        print(f"Distance to your destination {dis}")
    else:
        print("No distance info is available")


example = {
    "time": 10,
    "speed": 2,
    "distance": "1000 meter",
}

route_info(example)
