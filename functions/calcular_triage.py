def clasificar_triage(velocidad, orientacion):
    if velocidad > 120 and abs(orientacion) > 30:
        return 5
    elif 90 < velocidad <= 120 and 20 < abs(orientacion) <= 30:
        return 4 
    elif 60 < velocidad <= 90 and 10 < abs(orientacion) <= 20:
        return 3  
    elif velocidad <= 60 and abs(orientacion) <= 10:
        return 1 
    else:
        return 2  

