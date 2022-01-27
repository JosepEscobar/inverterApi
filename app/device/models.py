import json

class Rating():
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
        print("arrayValues")
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
        return f'Rating({self.gridVoltatge})'

    def __str__(self):
        return f'{self.gridVoltatge}'

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class Status():
    gridVoltatge = ""
    gridFrequency = ""
    acOutputVoltage = ""
    acOutputFrequency = ""
    acOutputApparentCurrent = ""
    acOutputActivePower = ""
    outputLoadPercent = ""
    busVoltage = ""
    batteryVoltage = ""
    batteryChargingCurrent = ""
    batteryCapacitypercent = ""
    inverterHeatSinkTemperature = ""
    pvInputCurrentForBattery = ""
    pvInputVoltage = ""
    batteryVoltageFromScc = ""
    batteryDischargeCurrent = ""
    deviceStatus = ""
    pvInputPower = ""
    
    def __init__(self, arrayValues):
        print("arrayValues")
        print(arrayValues)
      
        self.gridVoltatge = arrayValues[0]
        self.gridFrequency = arrayValues[1]
        self.acOutputVoltage = float(arrayValues[2])
        self.acOutputFrequency = float(arrayValues[3])
        self.acOutputApparentCurrent = int(arrayValues[4])
        self.acOutputActivePower = int(arrayValues[5])
        self.outputLoadPercent = int(arrayValues[6])
        self.busVoltage = arrayValues[7]
        self.batteryVoltage = float(arrayValues[8])
        self.batteryChargingCurrent = int(arrayValues[9])
        self.batteryCapacitypercent = int(arrayValues[10])
        self.inverterHeatSinkTemperature = int(arrayValues[11])
        self.pvInputCurrentForBattery = int(arrayValues[12])
        self.pvInputVoltage = float(arrayValues[13])
        self.batteryVoltageFromScc = arrayValues[14]
        self.batteryDischargeCurrent = arrayValues[15]
        self.deviceStatus = arrayValues[16]
        self.pvInputPower = int(arrayValues[19])

    def __repr__(self):
        return f'Status({self.gridVoltatge})'

    def __str__(self):
        return f'{self.gridVoltatge}'

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)