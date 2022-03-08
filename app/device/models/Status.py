import json
import config.default as config

class Status():
    gridVoltatge = ""
    gridFrequency = ""
    gridPower = ""
    acOutputVoltage = ""
    acOutputFrequency = ""
    acOutputApparentCurrent = ""
    acOutputActivePower = ""
    outputLoadPercent = ""
    busVoltage = ""
    batteryVoltage = ""
    batteryChargingCurrent = ""
    batteryChargingPower = ""
    batteryDischargePower = ""
    batteryCapacitypercent = ""
    inverterHeatSinkTemperature = ""
    pvInputCurrentForBattery = ""
    pvInputVoltage = ""
    batteryVoltageFromScc = ""
    batteryDischargeCurrent = ""
    deviceStatus = ""
    pvInputPower = ""
    
    def __init__(self, arrayValues):
        print("🌵 Status arrayValues:")
        print(arrayValues)
      
        self.gridVoltatge = float(arrayValues[0])
        self.gridFrequency = float(arrayValues[1])
        self.acOutputVoltage = float(arrayValues[2])
        self.acOutputFrequency = float(arrayValues[3])
        self.acOutputApparentCurrent = int(arrayValues[4])
        self.acOutputActivePower = int(arrayValues[5])
        self.outputLoadPercent = int(arrayValues[6])
        self.busVoltage = int(arrayValues[7])
        self.batteryVoltage = float(arrayValues[8])
        self.batteryChargingCurrent = int(arrayValues[9])
        self.batteryDischargeCurrent = int(arrayValues[15])
        self.batteryCapacitypercent = int(arrayValues[10])
        self.inverterHeatSinkTemperature = int(arrayValues[11])
        self.pvInputCurrentForBattery = int(arrayValues[12])
        self.pvInputVoltage = float(arrayValues[13])
        self.batteryVoltageFromScc = float(arrayValues[14])
        self.deviceStatus = arrayValues[16]
        self.pvInputPower = int(arrayValues[19])

        self.batteryDischargePower = self.batteryDischargeCurrent * self.batteryVoltage
        self.batteryChargingPower = self.batteryChargingCurrent * config.CAHRGING_VOLTATGE
        
        if  self.gridVoltatge > 0 and self.batteryDischargePower == 0:
            self.gridPower = (self.batteryChargingPower - self.pvInputPower) + self.acOutputActivePower
        else:
            self.gridPower = 0

    def __repr__(self):
        return f'Status({self.gridVoltatge})'

    def __str__(self):
        return f'{self.gridVoltatge}'

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
