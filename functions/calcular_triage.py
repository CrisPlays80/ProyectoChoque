def clasificar_triage(velocidad, orientacion):
    if velocidad > 120 and abs(orientacion) > 30:
        return 1
    elif 90 < velocidad <= 120 and 20 < abs(orientacion) <= 30:
        return 2 
    elif 60 < velocidad <= 90 and 10 < abs(orientacion) <= 20:
        return 4  
    elif velocidad <= 60 and abs(orientacion) <= 10:
        return 5 
    else:
        return 3  

