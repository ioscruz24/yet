from yet.workbench.digilent import DwfOscilloscope
from yet.workbench.siglent import Sds1kOscilloscope

class Device(Object):
    def __init__(self):

    def get_instruments():

class Instrument(Object):
    def __init__(self):

    def configure():

class Oscilloscope(Instrument):
    classes = [DwfOscilloscope, Sds1kOscilloscope]
    def __init__(self):
