from yet.test import Script
from yet.instruments import *

if __name__ == '__main__':

    tst = Script(args, brief='Button Test', instruments=['scope', 'spi', 'la'])
    tst.step('Configure the instruments')
    tst.scope.configure(class=Oscilloscope, channels=['VbatVdc', 'VbatIdc'])
    tst.scope.VbatVdc.set_y_range(min=-1.0, max=4.0)
    tst.scope.VbatIdc.set_y_units(AMPERES)
    tst.scope.VbatIdc.set_y_gain(0.05) #Volts per Ampere
    tst.scope.set_x_range(min=-1.0, max=10.0)
    tst.scope.set_trigger(mode=NORMAL_TRIGGER_MODE, source=MANUAL_TRIGGER_SOURCE)
    tst.spi.configure(class=SpiMaster, channels=['Switcher'])
    tst.spi.Switcher.configure(class=Max17432SwitchArray, channels=['Btn0', 'Btn1'])
    tst.la.configure(class=LogicAnalyzer, channels=['RedPwm', 'GreenPwm', 'BluePwm', 'IrPwm'])
    tst.case('')
    tst.step('')
    tst.scope.setup()
    tst.meter.setup()
    tst.prompt('')
    tst.verify_step('')
    tst.end_case()
    tst.end()
