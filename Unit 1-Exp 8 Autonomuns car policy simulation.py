road = ["S","G","R","G","D"]
pos = 0

while road[pos] != "D":
    if road[pos] == "R":
        print("Red light at", pos, "- waiting")
        pos += 1      # move after wait
    else:
        pos += 1
    print("Car at", pos)

print("Reached Destination")
