import sys
from ctypes import *
from yet.workbench import Device

if sys.platform.startswith("win"):
    dwf = cdll.dwf
elif sys.platform.startswith("darwin"):
    dwf = cdll.LoadLibrary("/Library/Frameworks/dwf.framework/dwf")
else:
    dwf = cdll.LoadLibrary("libdwf.so")

class DwfSpiMaster(SpiMaster):

class DwfDevice(Device):
    params = ['configuration']
    param_props = {'configuration': {brief' : 'FPGA Configuration', 'default': None}}
    instruments = [DwfSpiMaster]
    def __init__(self):
        self.configured = False

    def is_configured(self):
        return self.configured

    def get_instances(self):
        instances = list()
        c_num_devices = c_int()
        c_device_name = create_string_buffer(64)
        c_device_sn = create_string_buffer(16)
        c_device_id = c_int()
        c_device_rev = c_int()
        dwf.FDwfEnum(c_int(0), byref(c_num_devices))
        for dev in range(0, c_num_devices.value):
            dwf.FDwfEnumDeviceName(c_int(dev), c_device_name)
            dwf.FDwfEnumSN(c_int(dev), c_device_sn)
            dwf.FDwfDeviceType(c_int(dev), byref(c_device_id), byref(c_device_rev))
            instances.append(str(c_device_name.value) + ":" + str(c_device_sn.value))
        return instances

    def get_params(self, instance):
        return DwfDevice.params

    def get_param_brief(self, instance, param):
        return param_props[param]['brief']

    def get_param_default(self, instance, param):
        return param_props[param]['default']

    def get_param_options(self, instance, param):
        c_num_configs = c_int()
        if param == 'configuration':
            options = list()
            dwf.FDwfEnumConfig(c_int(instance), byref(c_num_configs))
            c_count = c_int()
            c_size = c_int()
            for config in range(0, c_num_configs.value):
                dwf.FDwfEnumConfigInfo(c_int(config), c_int(1), byref(c_count))
                dwf.FDwfEnumConfigInfo(c_int(config), c_int(7), byref(c_size))
                option = "AnalogIn: " + str(c_count.value) + "x" + str(c_size.value)
                dwf.FDwfEnumConfigInfo(c_int(config), c_int(2), byref(c_count))
                dwf.FDwfEnumConfigInfo(c_int(config), c_int(8), byref(c_size))
                option += " AnalogOut: " + str(c_count.value) + "x" + str(c_size.value)
                dwf.FDwfEnumConfigInfo(c_int(config), c_int(4), byref(c_count))
                dwf.FDwfEnumConfigInfo(c_int(config), c_int(9), byref(c_size))
                option += " DigitalIn: " + str(c_count.value) + "x" + str(c_size.value)
                dwf.FDwfEnumConfigInfo(c_int(config), c_int(5), byref(c_count))
                dwf.FDwfEnumConfigInfo(c_int(config), c_int(10), byref(c_size))
                option += " DigitalOut: " + str(c_count.value) + "x" + str(c_size.value)
                options.append(option)
            return options
        else:
            return params[param]['options']

    def configure(self, instance, config):
        c_num_devices = c_int()
        dwf.FDwfEnum(c_int(0), byref(c_num_devices))
        if instance >= c_num_device.value:
            raise ValueError('Invalid instance value')

        self.configured = True
