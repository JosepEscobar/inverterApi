import sys
import string
import usb.core, usb.util, usb.control
import crc16
import time
import re
from app.device.models import Configuration, Status, FlagStatus

# COMMAND+CRC16
def getCommand(cmd):
    cmd = cmd.encode('utf-8')
    crc = crc16.crc16xmodem(cmd).to_bytes(2,'big')
    cmd = cmd+crc
    cmd = cmd+b'\r'
    while len(cmd)<8:
        cmd = cmd+b'\0'
    return cmd

# SEND COMMAND
def sendCommand(dev, cmd):
    dev.ctrl_transfer(0x21, 0x9, 0x1024, 0, cmd)

# RESULT COMMAND
def getResult(dev, timeout=150):
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
def getOnlyNumbers(string):
    return re.sub("[^0-9]", "", string)

def getDevice(vendorId, productId, serialNumberId = None):

    device = None
    devList = usb.core.find(find_all=True, 
                            idVendor=vendorId, 
                            idProduct=productId)

    # For each device that we find...
    for dev in devList:
        serialNumberOutput = getSerialNumber(dev)

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

    return device

def getSerialNumber(dev):

    interface = 0

    if dev.is_kernel_driver_active(interface):
        try:
            dev.detach_kernel_driver(interface)
        except usb.core.USBError as e:
            sys.exit("Could not detatch kernel driver from interface({0}): {1}".format(i, str(e)))

    serialNumberOutput = ""
    while len(serialNumberOutput) < 11:
        #output example: (92931712101193ÎÈ
        sendCommand(dev, getCommand("QID"))
        serialNumberOutput = str(getResult(dev))
    
    serialNumberOutput = getOnlyNumbers(serialNumberOutput)
    return serialNumberOutput

# Inverter general status values
def getStatus(dev):
    interface = 0
    if dev.is_kernel_driver_active(interface):
        try:
            dev.detach_kernel_driver(interface)
        except usb.core.USBError as e:
            sys.exit("Could not detatch kernel driver from interface({0}): {1}".format(i, str(e)))

    # 2.7 QPIGS<cr>: Device general status parameters inquiry
    sendCommand(dev, getCommand("QPIGS"))
    inverterValues = getResult(dev).replace('(', '')
    inverterValuesArray = inverterValues.split(" ")
    usb.util.dispose_resources(dev)

    return inverterValuesArray
    
#rating
def getConfiguration(dev):
    interface = 0
    if dev.is_kernel_driver_active(interface):
        try:
            dev.detach_kernel_driver(interface)
        except usb.core.USBError as e:
            sys.exit("Could not detatch kernel driver from interface({0}): {1}".format(i, str(e)))
    
    # 2.5 QPIRI<cr>: Device Rating Information inquiry
    sendCommand(dev, getCommand("QPIRI"))
    inverterValues = getResult(dev).replace('(', '')
    inverterValuesArray = inverterValues.split(" ")
    usb.util.dispose_resources(dev)
    return inverterValuesArray


def getDeviceFlagStatus(dev):
    interface = 0
    if dev.is_kernel_driver_active(interface):
        try:
            dev.detach_kernel_driver(interface)
        except usb.core.USBError as e:
            sys.exit("Could not detatch kernel driver from interface({0}): {1}".format(i, str(e)))
    
    # 2.6 QFLAG<cr>: Device flag status inquiry
    sendCommand(dev, getCommand("QFLAG"))
    inverterValues = getResult(dev).replace('(', '')
    usb.util.dispose_resources(dev)
    return inverterValues

class DataSource():
    def getConfiguration():
        inverter = getDevice(0x0665, 0x5161, None)
        if inverter:
            output = getConfiguration(inverter)
            return Configuration(output)

    def getStatus():
        inverter = getDevice(0x0665, 0x5161, None)
        if inverter:
            output = getStatus(inverter)
            return Status(output)

    def getFlagStatus():
        inverter = getDevice(0x0665, 0x5161, None)
        if inverter:
            output = getDeviceFlagStatus(inverter)
            return FlagStatus(output)


