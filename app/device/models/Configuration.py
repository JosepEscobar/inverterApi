import json
import config.default as config

class Configuration():
    gridVoltatge = ""
    gridCurrent = ""
    acOutputVoltage = ""
    acOutputFrequency = ""
    acOutputCurrent = ""
    acOutputApparentCurrent = ""
    acOutputActivePower = ""
    batteryVoltage = ""
    batteryRechargeVoltage = ""
    batteryUnderVoltage = ""
    batteryBulkVoltage = ""
    batteryFloatVoltage = ""
    batteryType = ""
    currentMaxAcChargingCurrent = ""
    currentMaxChargingCurrent = ""
    inputVoltageRange = ""
    outputSourcePriority = ""
    chargerSourcePriority = ""
    parallelMaxNum = ""
    machineType = ""
    topology = ""
    outputMode = ""
    batteryRedischargeVoltage = ""
    pvOkConditionForParallel = ""
    pvPowerBalance = ""
    
    def __init__(self, arrayValues):
        print("🌵 Configuration arrayValues: ")
        print(arrayValues)
      
        self.gridVoltatge = arrayValues[0]
        self.gridCurrent = arrayValues[1]
        self.acOutputVoltage = arrayValues[2]
        self.acOutputFrequency = arrayValues[3]
        self.acOutputCurrent = arrayValues[4]
        self.acOutputApparentCurrent = arrayValues[5]
        self.acOutputActivePower = arrayValues[6]
        self.batteryVoltage = arrayValues[7]
        self.batteryRechargeVoltage = arrayValues[8]
        self.batteryUnderVoltage = arrayValues[9]
        self.batteryBulkVoltage = arrayValues[10]
        self.batteryFloatVoltage = arrayValues[11]
        self.batteryType = arrayValues[12]
        self.currentMaxAcChargingCurrent = arrayValues[13]
        self.currentMaxChargingCurrent = arrayValues[14]
        self.inputVoltageRange = arrayValues[15]
        self.outputSourcePriority = arrayValues[16]
        self.chargerSourcePriority = arrayValues[17]
        self.parallelMaxNum = arrayValues[18]
        self.machineType = arrayValues[19]
        self.topology = arrayValues[20]
        self.outputMode = arrayValues[21]
        self.batteryRedischargeVoltage = arrayValues[22]
        self.pvOkConditionForParallel = arrayValues[23]
        self.pvPowerBalance = arrayValues[24]

    def __repr__(self):
        return f'Configuration({self.gridVoltatge})'

    def __str__(self):
        return f'{self.gridVoltatge}'

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)