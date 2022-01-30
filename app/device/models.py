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
        return f'Configuration({self.gridVoltatge})'

    def __str__(self):
        return f'{self.gridVoltatge}'

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


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
        print("arrayValues")
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
        
        if self.batteryChargingCurrent > 0 and self.acOutputActivePower > 0 and self.gridVoltatge > 0:
            batteryCurrent = (self.batteryChargingCurrent * config.CAHRGING_VOLTATGE) / self.gridVoltatge
            gridCurrent = self.acOutputActivePower/self.gridVoltatge
            self.gridPower = int(self.gridVoltatge * (batteryCurrent + gridCurrent))
        else:
            self.gridPower = int(self.gridVoltatge * self.acOutputActivePower)

    def __repr__(self):
        return f'Status({self.gridVoltatge})'

    def __str__(self):
        return f'{self.gridVoltatge}'

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)