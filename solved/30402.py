image = [input() for _ in range(15)]

for line in image:
    if "w" in line:
        print("chunbae")
        break
    elif "b" in line:
        print("nabi")
        break
    elif "g" in line:
        print("yeongcheol")
        break
    else:
        continue
