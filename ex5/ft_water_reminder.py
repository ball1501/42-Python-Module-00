def ft_water_reminder():
    wr = int(input("Days since last watering: "))
    if wr <= 2:
        print("Plants are fine")
    else:
        print("Water the plants!")
