import sys
import string
import usb.core, usb.util, usb.control
import crc16
import time
import re
from app.device.models.Configuration import Configuration
from app.device.models.Status import Status
from app.device.models.FlagStatus import FlagStatus

class Inverter:
    deviceCache = None
    deviceFlagStatusCache = None

    # COMMAND+CRC16
    def getCommand(self, cmd):
        cmd = cmd.encode('utf-8')
        crc = crc16.crc16xmodem(cmd).to_bytes(2,'big')
        cmd = cmd+crc
        cmd = cmd+b'\r'
        while len(cmd)<8:
            cmd = cmd+b'\0'
        return cmd

    # SEND COMMAND
    def sendCommand(self, dev, cmd):
        dev.ctrl_transfer(0x21, 0x9, 0x1024, 0, cmd)

    # RESULT COMMAND
    def getResult(self, dev, timeout=150):
        res=""
        i=0
        while '\r' not in res and i<20:
            try:
                res+="".join([chr(i) for i in dev.read(0x81, 8, timeout) if i!=0x00])
                # print(res)
            except usb.core.USBError as e:
                if e.errno == 110:
                    pass
                else:
                    raise
            i+=1
        return res

    # REMOVE NON-NUMERICAL CHARACTERS FROM STRING
    def getOnlyNumbers(self, string):
        return re.sub("[^0-9]", "", string)

    def getDevice(self, vendorId, productId, serialNumberId = None):
        if self.deviceCache is not None:
            return self.deviceCache 

        device = None
        devList = usb.core.find(find_all=True, 
                                idVendor=vendorId, 
                                idProduct=productId)

        # For each device that we find...
        for dev in devList:
            serialNumberOutput = self.getSerialNumber(dev)

            if serialNumberId is None:
                #if no serial number id was specified, we'll return the first device found
                device = dev
                break
            else:
                if serialNumberId == serialNumberOutput:
                    #if serial number id was specified and 
                    #it matches with the device, we'll return that device
                    device = dev
                    break
        self.deviceCache = device
        return device

    def getSerialNumber(self, dev):
        interface = 0

        if dev.is_kernel_driver_active(interface):
            try:
                dev.detach_kernel_driver(interface)
            except usb.core.USBError as e:
                sys.exit("Could not detatch kernel driver from interface({0}): {1}".format(i, str(e)))

        serialNumberOutput = ""
        while len(serialNumberOutput) < 11:
            #output example: (92931712101193ÎÈ
            self.sendCommand(dev, self.getCommand("QID"))
            serialNumberOutput = str(self.getResult(dev))
        
        serialNumberOutput = self.getOnlyNumbers(serialNumberOutput)
        return serialNumberOutput

    # Inverter general status values
    def getStatus(self, dev):
        interface = 0
        if dev.is_kernel_driver_active(interface):
            try:
                dev.detach_kernel_driver(interface)
            except usb.core.USBError as e:
                sys.exit("Could not detatch kernel driver from interface({0}): {1}".format(i, str(e)))

        # 2.7 QPIGS<cr>: Device general status parameters inquiry
        self.sendCommand(dev, self.getCommand("QPIGS"))
        inverterValues = self.getResult(dev).replace('(', '')
        inverterValuesArray = inverterValues.split(" ")
        usb.util.dispose_resources(dev)

        return inverterValuesArray
        
    #rating
    def getConfiguration(self, dev):
        interface = 0
        if dev.is_kernel_driver_active(interface):
            try:
                dev.detach_kernel_driver(interface)
            except usb.core.USBError as e:
                sys.exit("Could not detatch kernel driver from interface({0}): {1}".format(i, str(e)))
        
        # 2.5 QPIRI<cr>: Device Rating Information inquiry
        self.sendCommand(dev, self.getCommand("QPIRI"))
        inverterValues = self.getResult(dev).replace('(', '')
        inverterValuesArray = inverterValues.split(" ")
        usb.util.dispose_resources(dev)
        return inverterValuesArray


    def getDeviceFlagStatus(self, dev):
        interface = 0
        if dev.is_kernel_driver_active(interface):
            try:
                dev.detach_kernel_driver(interface)
            except usb.core.USBError as e:
                if self.deviceFlagStatusCache is not None:
                    pass
                else:
                    sys.exit("Could not detatch kernel driver from interface({0}): {1}".format(i, str(e)))
        
        if self.deviceFlagStatusCache is not None:
            return self.deviceFlagStatusCache

        # 2.6 QFLAG<cr>: Device flag status inquiry
        self.sendCommand(dev, self.getCommand("QFLAG"))
        inverterValues = self.getResult(dev).replace('(', '')
        usb.util.dispose_resources(dev)
        deviceFlagStatusCache = inverterValues
        return inverterValues

class DataSource():
    inverter = None
    device = None
    def __init__(self):
        self.inverter = Inverter()
        self.device = self.inverter.getDevice(0x0665, 0x5161, None)

    def getConfiguration(self):
        if self.device:
            output = self.inverter.getConfiguration(self.device)
            return Configuration(output)

    def getStatus(self):
        if self.device:
            output = self.inverter.getStatus(self.device)
            return Status(output)

    def getFlagStatus(self):
        if self.device:
            output = self.inverter.getDeviceFlagStatus(self.device)
            return FlagStatus(output)


