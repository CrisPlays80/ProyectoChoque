def clasificar_triage(velocidad, orientacion):
    if int(velocidad) > 120 and abs(int(orientacion)) > 30:
        return 1
    elif 90 < int(velocidad) <= 120 and 20 < abs(int(orientacion)) <= 30:
        return 2 
    elif 60 < int(velocidad) <= 90 and 10 < abs(int(orientacion)) <= 20:
        return 4  
    elif int(velocidad) <= 60 and abs(int(orientacion)) <= 10:
        return 5 
    else:
        return 3  

