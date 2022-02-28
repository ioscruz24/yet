from yet.workbench.digilent import DwfDevice
from yet.workbench.digilent import DwfOscilloscope
from yet.workbench.siglent import Sds1kOscilloscope

class Device(Object):
    classes = [DwfDevice]
    def __init__(self):

    def configure(self, config):

class Instrument(Object):
    classes = [Oscilloscope, SpiMaster]
    def __init__(self):

    def configure(self, config):

class Oscilloscope(Instrument):
    classes = [DwfOscilloscope, Sds1kOscilloscope]
    def __init__(self):

class SpiMaster(Instrument):
    classes = [DwfSpiMaster]
