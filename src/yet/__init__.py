from yet.test import Function
from yet.test.digilent import DwfOscilloscope
from yet.test.siglent import Sds1104xeOscilloscope

class Device(Object):
    def __init__(self):

class Instrument(Object):
    def __init__(self):

    def configure():

class Oscilloscope(Function):
    classes = [DwfOscilloscope, Sds1104xeOscilloscope]
    def __init__(self):
