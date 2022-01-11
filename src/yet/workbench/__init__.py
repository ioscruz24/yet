from yet.workbench import Function
from yet.workbench.digilent import *
from yet.workbench.siglent import Sds1104xeOscilloscope

class Device(Object):
    def __init__(self):

    def confiure(self):

class Instrument(Object):
    def __init__(self):

    def configure():

class Oscilloscope(Instrument):
    classes = [DwfOscilloscope, Sds1104xeOscilloscope]
    def __init__(self):

class SpiMaster(Instrument):
    classes = [DwfSpiMaster]
