import json
import config.default as config

class FlagStatus():
    labelsDictionary = {
        "a": "buzzer",
        "b": "overload-bypass-function",
        "j": "power-saving",
        "k": "display-escape-to-default-automaticaly",
        "u": "overload-restart",
        "v": "over-temperature-restart",
        "x": "backlight-on",
        "y": "alarm-on-when-primary-source-interrupt",
        "z": "fault-code-record"
    }
    
    def __init__(self, value): 
        # Sacar la información que tenemos des de la E hasta la D y tendremos los valores activos
        # EuvxyDabjkzj
        splitedValues = value.split("D")
        # [0]Euvxy [1]abjkzj
        splitedValues[0] = splitedValues[0].replace("E", "")
        splitedValues[1] = splitedValues[1].replace("\r", "")
        splitedValues[1] = splitedValues[1].replace("+", "")
        # [0]uvxy [1]abjkzj
        #['uvxy', 'abjkzj+\r']



        # El resto hasta el + serán los valores iactivos
        # Mapear letras con el diccionario y ponerlo todo en un array
        # Devolverlo codificado en JSON
        print("🌵 FlagStatus values:")
        print(splitedValues)

    def __repr__(self):
        return f'Status({self.gridVoltatge})'

    def __str__(self):
        return f'{self.gridVoltatge}'

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)