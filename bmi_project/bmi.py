def oblicz_bmi(waga, wzrost):
    '''Oblicza BMI oraz printuje status'''
    bmi = int(waga / (wzrost/100) ** 2)
    if bmi < 18.5:
        status = "Niedowaga"
    elif 18.5 <= bmi < 24.9:
        status = "Prawidłowa waga"
    elif 25 <= bmi < 29.9:
        status = "Nadwaga"
    else:
        status = "Otyłość"
    print(status)
    return bmi