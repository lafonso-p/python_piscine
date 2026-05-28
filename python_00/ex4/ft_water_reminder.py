def ft_water_reminder():
    plant_age = int(input('Days since last watering:'))
    if plant_age <= 2:
        print('Plant are fine')
    else:
        print('Water the plants!')
