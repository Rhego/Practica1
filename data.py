import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def buscador(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0: 
        yn = input("Usted quiso decir %s, Presione S si es si, o N si es  no: " % get_close_matches(w,data.keys())[0] )
        yn = yn.upper()
        if yn == "S":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "La palabra no existe!! por favor intente nuevamente"
        else:
            return "Opcion no valida"    
    else:
        return "Por favor intente nuevamente."



word = input("Que palabra desea buscar: ")

salida = buscador(word)

if type(salida) == list:
    for item in salida:
        print(item)
else:
    print(salida)      

#Prueba commit2
#test