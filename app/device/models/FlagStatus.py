import json
import config.default as config



class FlagStatus():
    keysDictionary = {
            "a": "is-buzzer-enabled",
            "b": "is-overload-bypass-function-enabled",
            "j": "is-power-saving-enabled",
            "k": "is-display-escape-to-default-automaticaly-enabled",
            "u": "is-overload-restart-enabled",
            "v": "is-over-temperature-restart-enabled",
            "x": "is-backlight-on-enabled",
            "y": "is-alarm-on-when-primary-source-interrupt-enabled",
            "z": "is-fault-code-record-enabled"
        }
    flagStatusDictionary = {}

    def __init__(self, value): 
        # Sacar la información que tenemos des de la E hasta la D y tendremos los valores activos
        splitedValues = value.split("D")
        splitedValues[0] = splitedValues[0].replace("E", "")
        splitedValues[1] = splitedValues[1].replace("\r", "")
        splitedValues[1] = splitedValues[1].replace("+", "")

        enabledFlags = splitedValues[0]
        disabledFlags = splitedValues[1]

        # Handle enabled values
        for index, value in enumerate(enabledFlags):
            self.flagStatusDictionary[self.keysDictionary[value]] = True

        for index, value in enumerate(disabledFlags):
            self.flagStatusDictionary[self.keysDictionary[value]] = False
            
        print("🌵 FlagStatus values:")
        print(self.flagStatusDictionary)

    def __repr__(self):
        return f'Status({self.gridVoltatge})'

    def __str__(self):
        return f'{self.gridVoltatge}'

    def toJSON(self):
        return json.dumps(self.flagStatusDictionary, default=lambda o: o.__dict__, sort_keys=True, indent=4)